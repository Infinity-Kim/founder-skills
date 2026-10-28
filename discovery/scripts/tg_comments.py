"""Комментарии к постам канала (у которых replies > 0) из уже выгруженного <имя>.jsonl.

  python tg_comments.py <id или @username канала> <имя>

Пишет $DISCOVERY_DIR/tg-raw/replies_<имя>.jsonl, продолжает с места остановки.
"""
import asyncio, json, os, sys
from tg_common import client, iter_safe, raw_dir


async def main():
    key, name = sys.argv[1], sys.argv[2]
    d = raw_dir()
    posts = [json.loads(l) for l in open(f"{d}/{name}.jsonl")]
    ids = sorted({p["id"] for p in posts if (p.get("replies") or 0) > 0}, reverse=True)
    out = f"{d}/replies_{name}.jsonl"
    done = set()
    if os.path.exists(out):
        done = {json.loads(l)["post"] for l in open(out)}
    c = await client()
    ch = await c.get_entity(int(key) if key.lstrip("-").isdigit() else key)
    f = open(out, "a"); n = 0
    for pid in ids:
        if pid in done:
            continue
        async for m in iter_safe(c, ch, reply_to=pid, limit=300):
            if m.message:
                f.write(json.dumps({"post": pid, "id": m.id, "date": m.date.isoformat(), "text": m.message}, ensure_ascii=False) + "\n"); n += 1
        f.write(json.dumps({"post": pid, "id": None}) + "\n"); f.flush()
        await asyncio.sleep(2)
    print("posts", len(ids), "comments", n)
    await c.disconnect()

asyncio.run(main())
