# Инструменты и окружение

## Окружение

| Что | Где |
|---|---|
| Python с Playwright | venv с `pip install playwright` и установленным Chrome (`channel="chrome"`), путь - в `$PY` |
| Python с Telethon | `pip install telethon` |
| Ключи Telegram API | файл `.env` с `TG_API_ID`, `TG_API_HASH` (my.telegram.org), путь - в `$TG_ENV` |
| Сессия Telegram | создать один раз: `python3 -c "from telethon.sync import TelegramClient; TelegramClient('s', ID, HASH).start()"`, дальше работать с копией |
| Свои данные | любой read-only доступ к своей БД или выгрузкам |

## Подготовка рабочей папки

```bash
D=<scratchpad>/discovery-<slug>
mkdir -p $D/{notes,shots,text,tg-raw,tg,data,sim,artifact}
cp <путь к сессии>.session $D/tg/s.session
chmod 600 $D/tg/s.session
export DISCOVERY_DIR=$D TG_ENV=<путь к .env> TG_SESSION=$D/tg/s
```

## Playwright: shot.py

```bash
DISCOVERY_DIR=$D $PY -I ~/.claude/skills/discovery/scripts/shot.py "<url>" <имя> [--imgs] [--min 300] [--wait 4] [--selector "article"]
```

- Headful Chrome с постоянным профилем (`PW_PROFILE`, по умолчанию
  `~/.cache/discovery-pw-profile`). Профиль один - запуски сериализуются lock-файлом,
  параллельные агенты просто ждут очереди.
- Пишет `$D/shots/ru-<имя>.png`, `$D/text/ru-<имя>.txt`, с `--imgs` - картинки статьи и
  `$D/text/ru-<имя>-imgs.txt` с подписями.
- Ничего не логинит, форм не заполняет, капчи не трогает. Антибот (WB, Ozon, часть
  сайтов) - пометить и брать текст из WebFetch или кэша поисковика.

## YouTube: yt.py

```bash
$PY -I ~/.claude/skills/discovery/scripts/yt.py search "https://www.youtube.com/results?search_query=<запрос>"
$PY -I ~/.claude/skills/discovery/scripts/yt.py video "https://www.youtube.com/watch?v=<id>"
```

## Telegram: tg_*.py

Запускать из папки скриптов (импорт `tg_common`) или с `PYTHONPATH`:

```bash
cd ~/.claude/skills/discovery/scripts
python3 tg_dialogs.py [фильтр]          # id чатов аккаунта
python3 tg_search.py "финансы wb" "опиу" # публичные каналы по словам
python3 tg_fetch.py $D/tg/config.json    # выгрузка
python3 tg_comments.py @channel имя      # комментарии к постам
```

- Только чтение. Отправка сообщений - не задача discovery; если владелец просит написать
  кастдев-респонденту, писать в «Избранное» владельцу, а не человеку.
- Сессия одна: два процесса на одной копии - `database is locked`. Telegram читает один
  агент.
- FloodWait обрабатывается паузой; большие чаты (50k+) выгружать по словам, не целиком.
- Отсечка - 12 месяцев, если нет причины брать больше.

## Финансы юрлиц и трафик

- checko.ru/company/<ОГРН>, rusprofile.ru, list-org.com, audit-it.ru - выручка и прибыль по
  годам (ГИР БО). WebFetch часто проходит; если нет - shot.py.
- pr-cy.ru/a/<домен>, be1.ru/stat/<домен>, similarweb.com/website/<домен> - визиты.
## Уроки прогонов

- **Лимит WebSearch общий на сессию.** 28.10.2026 он кончился у 4 из 7 агентов посреди работы, отзывы с Отзовика и vc.ru не собрались. Отзывы и подборки снимать первыми, а сайты конкурентов - WebFetch и `shot.py`, они в лимит не входят.
- **Playwright только без окна.** Видимые окна мешают владельцу работать. После правки скрипта снять уже стоящие в очереди запуски: Python читает скрипт при старте.
- **Очередь браузера.** 7 агентов дают 20-40 запусков `shot.py` в очереди. Скриншоты тарифов снимать сразу, справку - после, а таймаут Bash ставить 300000.
- **Антибот.** dev.wildberries.ru, seller-edu.ozon.ru и docs.ozon.ru не отдаются ни Playwright, ни WebFetch. Брать заметки к релизам из выдачи поиска и SSR-ответ.
- **Симуляции.** Системный python3 без numpy, запускать через `uv run -q --with numpy python sim.py`. Сборщик артефакта - `uv run -q --python 3.13`: f-строки с кавычками внутри не работают в 3.9.
- **Профили клиента** брать из своих данных (медиана, p75, p90 платящих) до запуска агентов, иначе цены конкурентов посчитаются на выдуманных профилях.
- **Один агент на Telegram,** зато охват полный: все чаты поддержки, фокус-группы и глобальный поиск по личным перепискам.
