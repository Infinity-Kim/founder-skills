"""Скриншот публичной страницы + текст + картинки статьи.

Использование:
  python -I shot.py <url> <name> [--imgs] [--min 300] [--wait 4] [--selector CSS]

Пишет:
  shots/ru-<name>.png           full-page скриншот
  text/ru-<name>.txt            innerText страницы (для чтения)
  shots/ru-<name>-img-N.png     картинки из статьи (если --imgs), ширина >= --min
  text/ru-<name>-imgs.txt       список: файл, src, alt, размеры, ближайший заголовок/подпись

Профиль Chrome один (PW_PROFILE, по умолчанию ~/.cache/discovery-pw-profile), запуски
сериализуются через lock-файл. Папка вывода - DISCOVERY_DIR.
Ничего не логинит, не заполняет формы, капчи не трогает.
"""
import argparse
import fcntl
import os
import sys
import time
import urllib.request

from playwright.sync_api import sync_playwright

# По умолчанию без окна: не мешает работать на экране. PW_HEADFUL=1 - видимое окно
# (за пределами экрана), если сайт режет фоновый режим.
HEADFUL = os.environ.get("PW_HEADFUL") == "1"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"

BASE = os.environ.get("DISCOVERY_DIR") or sys.exit("DISCOVERY_DIR не задан")
PROFILE = os.environ.get("PW_PROFILE", os.path.expanduser("~/.cache/discovery-pw-profile"))
SHOTS = BASE + "/shots"
TEXT = BASE + "/text"

ap = argparse.ArgumentParser()
ap.add_argument("url")
ap.add_argument("name")
ap.add_argument("--imgs", action="store_true")
ap.add_argument("--min", type=int, default=300)
ap.add_argument("--wait", type=float, default=4)
ap.add_argument("--selector", default="")
ap.add_argument("--maximg", type=int, default=25)
a = ap.parse_args()

os.makedirs(SHOTS, exist_ok=True)
os.makedirs(TEXT, exist_ok=True)
os.makedirs(PROFILE, exist_ok=True)
lock = open(PROFILE + ".lock", "w")
fcntl.flock(lock, fcntl.LOCK_EX)

JS_IMGS = """(sel) => {
  const root = (sel && document.querySelector(sel)) || document.querySelector('article, main, .content, #content, .page-content') || document.body;
  const out = [];
  root.querySelectorAll('img').forEach((im) => {
    const r = im.getBoundingClientRect();
    let h = '';
    let el = im;
    for (let i = 0; i < 40 && el; i++) {
      el = el.previousElementSibling || el.parentElement;
      if (el && /^H[1-4]$/.test(el.tagName)) { h = el.innerText.trim(); break; }
    }
    const fig = im.closest('figure');
    const cap = fig ? (fig.querySelector('figcaption') || {}).innerText || '' : '';
    let near = '';
    const p = im.closest('p, div, li');
    if (p) near = (p.innerText || '').trim().slice(0, 200);
    out.push({src: im.currentSrc || im.src, alt: im.alt || '', w: im.naturalWidth, h: im.naturalHeight, head: h, cap: cap, near: near});
  });
  return out;
}"""

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        PROFILE, channel="chrome", headless=not HEADFUL, user_agent=UA,
        args=["--window-position=-2400,-2400", "--disable-blink-features=AutomationControlled"], viewport={"width": 1440, "height": 900},
        locale="ru-RU",
    )
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    try:
        page.goto(a.url, wait_until="domcontentloaded", timeout=60000)
    except Exception as e:
        print("goto error:", e)
    time.sleep(a.wait)
    # прокрутка для ленивых картинок
    try:
        h = page.evaluate("document.body.scrollHeight")
        y = 0
        while y < min(h, 40000):
            y += 800
            page.evaluate(f"window.scrollTo(0,{y})")
            time.sleep(0.25)
        page.evaluate("window.scrollTo(0,0)")
        time.sleep(1)
    except Exception as e:
        print("scroll error:", e)
    print("final url:", page.url, "title:", page.title())
    shot = f"{SHOTS}/ru-{a.name}.png"
    try:
        page.screenshot(path=shot, full_page=True, timeout=60000)
    except Exception as e:
        print("full shot error, fallback viewport:", e)
        page.screenshot(path=shot)
    print("shot:", shot)
    try:
        txt = page.evaluate("document.body.innerText")
    except Exception:
        txt = ""
    with open(f"{TEXT}/ru-{a.name}.txt", "w") as f:
        f.write(page.url + "\n\n" + txt)
    print("text chars:", len(txt))
    if a.imgs:
        imgs = page.evaluate(JS_IMGS, a.selector)
        lines = []
        n = 0
        seen = set()
        for im in imgs:
            src = im["src"]
            if not src or src in seen or src.startswith("data:"):
                continue
            seen.add(src)
            if (im["w"] or 0) < a.min:
                continue
            n += 1
            if n > a.maximg:
                break
            ext = ".png"
            low = src.lower().split("?")[0]
            for e in (".jpg", ".jpeg", ".webp", ".gif", ".svg"):
                if low.endswith(e):
                    ext = e
            fn = f"{SHOTS}/ru-{a.name}-img-{n}{ext}"
            try:
                resp = page.request.get(src, timeout=30000)
                if resp.ok:
                    open(fn, "wb").write(resp.body())
                else:
                    fn = "HTTP %s" % resp.status
            except Exception as e:
                fn = f"ERR {e}"
            lines.append(f"{n}\t{fn}\t{src}\t{im['w']}x{im['h']}\talt={im['alt']}\thead={im['head']}\tcap={im['cap']}\tnear={im['near'][:150]!r}")
        with open(f"{TEXT}/ru-{a.name}-imgs.txt", "w") as f:
            f.write("\n".join(lines))
        print("images saved:", n)
    ctx.close()
