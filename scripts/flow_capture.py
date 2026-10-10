"""Walk a feature flow step by step and screenshot each step (Playwright).

Usage:
  python -I flow_capture.py flows.json OUT_DIR [--desktop-only] [--mobile-only] [--headed]

flows.json: a list of flows, one per product:
  [{"name": "airbnb",
    "steps": [
      {"do": "goto",  "url": "https://www.airbnb.com/"},
      {"do": "shot",  "label": "01_entry"},
      {"do": "click", "text": "Search"},                 # by visible text (role button/link first), or "selector"
      {"do": "fill",  "selector": "input[name=query]", "value": "Lisbon"},
      {"do": "press", "key": "Enter"},
      {"do": "wait",  "ms": 2500},
      {"do": "shot",  "label": "02_results", "full": true},
      {"do": "scroll","to": "Filters"},                   # scroll text/heading into view
      {"do": "click", "text": "Reserve", "confirmed": true}  # submit-like: only with the user's explicit yes
    ]}]

Safety:
- Declines non-essential cookies when a decline button exists; never clicks Accept.
- Stops a flow (status "blocked") when a human check / CAPTCHA appears; never solves it.
- Refuses to fill password, card or one-time-code fields.
- Refuses clicks whose target text looks like submit/pay/book/send/post/delete unless the step has
  "confirmed": true, which must only be set after the user said yes to that exact action. The flow stops
  there and captures the screen instead, so the last step before submission is always recorded.
- Use dummy data only.

Writes OUT_DIR/<name>_<label>_<d|m>.jpg and OUT_DIR/flows_result.json with per-step status, URL,
elapsed seconds and counts (steps, clicks, fills) for the report.
Requires: pip install playwright && python -m playwright install chromium
"""
import sys, os, json, re, time

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
DECLINE = ["Reject all", "Reject All", "Decline all", "Decline", "Reject", "Only necessary", "Necessary only"]
HUMAN_CHECK = ["verify you are human", "i'm not a robot", "checking your browser", "are you a robot"]
RISKY = re.compile(r"\b(submit|pay|place order|buy|purchase|checkout now|book|reserve|confirm|send|post|publish|delete|remove|sign up|create account|subscribe)\b", re.I)
SENSITIVE = re.compile(r"password|passwd|card|cc-|cvc|cvv|otp|one-time|iban|ssn", re.I)


def locate(pg, step):
    if step.get("selector"): return pg.locator(step["selector"]).first
    t = step["text"]
    for role in ("button", "link", "tab", "menuitem"):
        loc = pg.get_by_role(role, name=t)
        if loc.count(): return loc.first
    return pg.get_by_text(t, exact=False).first


def target_text(loc):
    try:
        return " ".join(filter(None, [loc.inner_text(timeout=1500), loc.get_attribute("value") or "", loc.get_attribute("aria-label") or ""]))
    except Exception: return ""


def decline_cookies(pg):
    for t in DECLINE:
        try:
            b = pg.get_by_role("button", name=t, exact=True)
            if b.count(): b.first.click(timeout=1500); return
        except Exception: pass


def run_flow(ctx, flow, out, tag):
    pg = ctx.new_page(); t0 = time.time(); log = []; counts = {"steps": 0, "clicks": 0, "fills": 0}; status = "ok"
    for i, st in enumerate(flow["steps"]):
        do = st["do"]; entry = {"i": i, "do": do}
        try:
            if do == "goto":
                pg.goto(st["url"], wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(3500)
                decline_cookies(pg); pg.keyboard.press("Escape")
            elif do == "click":
                loc = locate(pg, st); txt = st.get("text", "") + " " + target_text(loc)
                if RISKY.search(txt) and not st.get("confirmed"):
                    entry["note"] = f"stopped before submit-like action: {txt.strip()[:60]}"; status = "stopped-before-submit"
                    pg.screenshot(path=f"{out}/{flow['name']}_before_submit_{tag}.jpg", type="jpeg", quality=62)
                    log.append(entry); break
                loc.click(timeout=8000); pg.wait_for_timeout(st.get("after_ms", 1500)); counts["clicks"] += 1
            elif do == "fill":
                loc = locate(pg, st)
                attrs = " ".join(filter(None, [st.get("selector", ""), loc.get_attribute("type") or "", loc.get_attribute("name") or "", loc.get_attribute("autocomplete") or ""]))
                if SENSITIVE.search(attrs):
                    entry["note"] = "refused: sensitive field"; status = "refused-sensitive-field"; log.append(entry); break
                loc.fill(st["value"], timeout=8000); counts["fills"] += 1
            elif do == "press": pg.keyboard.press(st["key"]); pg.wait_for_timeout(st.get("after_ms", 1200))
            elif do == "wait": pg.wait_for_timeout(st.get("ms", 1500))
            elif do == "scroll":
                loc = pg.get_by_text(st["to"], exact=False).first
                loc.scroll_into_view_if_needed(timeout=5000); pg.evaluate("window.scrollBy(0,-40)"); pg.wait_for_timeout(800)
            elif do == "shot":
                path = f"{out}/{flow['name']}_{st['label']}_{tag}.jpg"
                pg.screenshot(path=path, full_page=bool(st.get("full")), type="jpeg", quality=62); entry["file"] = os.path.basename(path)
            if do != "shot" and do != "wait": counts["steps"] += 1
            body = pg.inner_text("body", timeout=3000)[:4000].lower()
            if any(h in body for h in HUMAN_CHECK):
                entry["note"] = "human check shown: ask the user to complete it"; status = "blocked"; log.append(entry); break
        except Exception as e:
            entry["error"] = str(e)[:160]; status = "error"; log.append(entry); break
        entry["url"] = pg.url; entry["t"] = round(time.time() - t0, 1); log.append(entry)
    pg.close(); print(flow["name"], tag, status, counts, flush=True)
    return {"name": flow["name"], "viewport": tag, "status": status, "counts": counts, "log": log}


def main():
    a = sys.argv[1:]
    if len(a) < 2: print(__doc__); sys.exit(1)
    flows = json.load(open(a[0], encoding="utf-8")); out = a[1]; os.makedirs(out, exist_ok=True)
    vps = []
    if "--mobile-only" not in a: vps.append(({"width": 1440, "height": 900}, "d"))
    if "--desktop-only" not in a: vps.append(({"width": 390, "height": 844}, "m"))
    from playwright.sync_api import sync_playwright
    results = []
    with sync_playwright() as p:
        b = p.chromium.launch(headless="--headed" not in a)
        for vp, tag in vps:
            for f in flows:
                ctx = b.new_context(viewport=vp, is_mobile=(tag == "m"), has_touch=(tag == "m"), user_agent=UA)
                results.append(run_flow(ctx, f, out, tag)); ctx.close()
        b.close()
    json.dump(results, open(f"{out}/flows_result.json", "w", encoding="utf-8"), indent=1)
    print("wrote", f"{out}/flows_result.json")


if __name__ == "__main__":
    main()
