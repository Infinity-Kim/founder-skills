"""Общее для Telethon-скриптов: ключи и сессия из окружения.

TG_ENV      - файл с TG_API_ID и TG_API_HASH (формат KEY=VALUE)
TG_SESSION  - путь к файлу сессии БЕЗ .session (копия, не оригинал: sqlite одной сессии
              не терпит двух процессов)
DISCOVERY_DIR - рабочая папка, выгрузки в $DISCOVERY_DIR/tg-raw/
Только чтение: скрипты ничего не отправляют.
"""
import asyncio, os, sys
from telethon import TelegramClient, errors


def env():
    path = os.environ.get("TG_ENV") or sys.exit("TG_ENV не задан")
    out = {}
    for line in open(path).read().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def raw_dir():
    base = os.environ.get("DISCOVERY_DIR") or sys.exit("DISCOVERY_DIR не задан")
    d = os.path.join(base, "tg-raw")
    os.makedirs(d, exist_ok=True)
    return d


async def client():
    e = env()
    sess = os.environ.get("TG_SESSION") or sys.exit("TG_SESSION не задан")
    c = TelegramClient(sess, int(e["TG_API_ID"]), e["TG_API_HASH"], timeout=20)
    await asyncio.wait_for(c.connect(), 60)
    if not await c.is_user_authorized():
        sys.exit("сессия не авторизована")
    return c


async def iter_safe(c, ent, **kw):
    """iter_messages с паузой на FloodWait и продолжением с места остановки."""
    offset = kw.pop("offset_id", 0)
    while True:
        try:
            async for m in c.iter_messages(ent, offset_id=offset, **kw):
                offset = m.id
                yield m
            return
        except errors.FloodWaitError as e:
            print("flood", e.seconds, flush=True)
            await asyncio.sleep(e.seconds + 3)
