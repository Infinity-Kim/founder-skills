"""Список диалогов аккаунта: id, тип, username, название, участники. python tg_dialogs.py [фильтр]"""
import asyncio, sys
from telethon.tl.types import Channel, Chat, User
from tg_common import client


async def main():
    c = await client()
    f = (sys.argv[1] if len(sys.argv) > 1 else "").lower()
    async for d in c.iter_dialogs():
        e = d.entity
        kind = "user" if isinstance(e, User) else ("channel" if isinstance(e, Channel) and e.broadcast else "group")
        title = d.name or ""
        if f and f not in title.lower() and f not in (getattr(e, "username", "") or "").lower():
            continue
        print(f"{d.id}\t{kind}\t@{getattr(e, 'username', '') or '-'}\t{getattr(e, 'participants_count', '') or ''}\t{title}")
    await c.disconnect()

asyncio.run(main())
