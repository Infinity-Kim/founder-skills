"""Поиск публичных каналов и чатов по словам. python tg_search.py "слово 1" "слово 2" ...
Пишет $DISCOVERY_DIR/tg-raw/_search.jsonl."""
import asyncio, json, os, sys
from telethon import errors, functions
from telethon.tl.types import Channel
from tg_common import client, raw_dir


async def main():
    c = await client()
    out = open(os.path.join(raw_dir(), "_search.jsonl"), "a")
    seen = set()
    for q in sys.argv[1:]:
        try:
            r = await c(functions.contacts.SearchRequest(q=q, limit=50))
        except errors.FloodWaitError as e:
            print("flood", e.seconds); await asyncio.sleep(e.seconds + 2); continue
        for ch in r.chats:
            if isinstance(ch, Channel) and ch.id not in seen:
                seen.add(ch.id)
                rec = dict(q=q, id=int(f"-100{ch.id}"), username=ch.username, title=ch.title,
                           count=ch.participants_count, broadcast=ch.broadcast)
                print(json.dumps(rec, ensure_ascii=False), flush=True)
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        await asyncio.sleep(2)
    await c.disconnect()

asyncio.run(main())
