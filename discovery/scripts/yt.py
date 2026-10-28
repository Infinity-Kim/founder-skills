"""YouTube: список видео из поиска или канала, либо описание и главы видео.

  python -I yt.py search "<url поиска или канала>"
  python -I yt.py video "<url видео>"

Профиль и lock общие с shot.py (PW_PROFILE).
"""
import fcntl, json, os, sys, time
from playwright.sync_api import sync_playwright

# По умолчанию без окна: не мешает работать на экране. PW_HEADFUL=1 - видимое окно
# (за пределами экрана), если сайт режет фоновый режим.
HEADFUL = os.environ.get("PW_HEADFUL") == "1"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"

PROFILE = os.environ.get("PW_PROFILE", os.path.expanduser("~/.cache/discovery-pw-profile"))
os.makedirs(PROFILE, exist_ok=True)
lock = open(PROFILE + ".lock", "w"); fcntl.flock(lock, fcntl.LOCK_EX)
mode, url = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(PROFILE, channel="chrome", headless=not HEADFUL, user_agent=UA,
        args=["--window-position=-2400,-2400", "--disable-blink-features=AutomationControlled"],
                                               viewport={"width": 1400, "height": 900}, locale="ru-RU")
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()
    pg.goto(url, wait_until="domcontentloaded", timeout=60000); time.sleep(5)
    if mode == "search":
        for _ in range(4):
            pg.mouse.wheel(0, 3000); time.sleep(1)
        items = pg.evaluate("""()=>[...document.querySelectorAll('a#video-title, a#video-title-link')].map(a=>({t:(a.title||a.innerText||'').trim(),h:a.href}))""")
        for it in items:
            if it["h"]:
                print(it["t"], "|", it["h"].split("&")[0])
    else:
        try:
            pg.click("tp-yt-paper-button#expand, #expand", timeout=5000); time.sleep(1)
        except Exception as e:
            print("noexpand", e)
        d = pg.evaluate("""()=>({title:document.title, date:(document.querySelector('#info-container')||{}).innerText||'', desc:(document.querySelector('#description-inline-expander')||document.querySelector('#description')||{}).innerText||'', chapters:[...document.querySelectorAll('ytd-macro-markers-list-item-renderer')].map(x=>x.innerText.replace(/\\n+/g,' ')).slice(0,80)})""")
        print(json.dumps(d, ensure_ascii=False, indent=1))
    ctx.close()
