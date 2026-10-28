"""Выгрузка чатов и каналов: целиком и/или поиском по словам, до даты отсечки.

  python tg_fetch.py config.json [имя_чата ...]

config.json:
  {"cut": "2025-10-28",
   "cap": 1500,                       # максимум сообщений на одно слово
   "chats": {"-1001234567890": "имя", "@username": "имя2"},
   "full": ["имя"],                   # выгрузить целиком (до cut)
   "keywords": ["слово", "Конкурент"]}

Пишет $DISCOVERY_DIR/tg-raw/<имя>.jsonl (одна строка - сообщение, поле kw - какие слова
нашли) и _stats_<имя>.json. Уже выгруженные чаты пропускает, если имя не указано явно.
"""
import asyncio, datetime, json, os, sys
from telethon.tl.types import User
from tg_common import client, iter_safe, raw_dir


def sname(s):
    if s is None:
        return None, None
    if isinstance(s, User):
        return s.username, " ".join(x for x in [s.first_name, s.last_name] if x)
    return getattr(s, "username", None), getattr(s, "title", None)


def rec(m, name, kw):
    u, n = sname(m.sender)
    return dict(chat=name, id=m.id, date=m.date.isoformat(), sender_id=m.sender_id, username=u, name=n,
                text=m.message or "", reply_to=getattr(m.reply_to, "reply_to_msg_id", None),
                views=m.views, replies=(m.replies.replies if m.replies else None), kw=[kw] if kw else [])


async def main():
    cfg = json.load(open(sys.argv[1]))
    only = sys.argv[2:]
    cut = datetime.datetime.fromisoformat(cfg["cut"]).replace(tzinfo=datetime.timezone.utc)
    cap = cfg.get("cap", 1500)
    out = raw_dir()
    c = await client()
    for key, name in cfg["chats"].items():
        if only and name not in only:
            continue
        fn = f"{out}/{name}.jsonl"
        if os.path.exists(fn) and not only:
            print("skip", name); continue
        ent = await c.get_entity(int(key) if key.lstrip("-").isdigit() else key)
        msgs, st = {}, {}
        if name in cfg.get("full", []):
            async for m in iter_safe(c, ent, limit=50000):
                if m.date < cut:
                    break
                if m.message:
                    msgs[m.id] = rec(m, name, None)
            st["_full"] = len(msgs)
        for kw in cfg.get("keywords", []):
            n = 0
            async for m in iter_safe(c, ent, search=kw, limit=cap):
                if m.date < cut:
                    break
                n += 1
                if m.id in msgs:
                    if kw not in msgs[m.id]["kw"]:
                        msgs[m.id]["kw"].append(kw)
                else:
                    msgs[m.id] = rec(m, name, kw)
            st[kw] = n
            await asyncio.sleep(0.3)
        with open(fn, "w") as f:
            for r in sorted(msgs.values(), key=lambda r: r["id"]):
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        json.dump(st, open(f"{out}/_stats_{name}.json", "w"), ensure_ascii=False)
        print(name, len(msgs), json.dumps({k: v for k, v in st.items() if v}, ensure_ascii=False), flush=True)
    await c.disconnect()

asyncio.run(main())
