# Founder Skills

Коллекция персональных скиллов для Claude AI, заточенных под задачи фаундера — от Customer Development до запуска продукта.

## Что это?

Скиллы — это инструкции для Claude, которые превращают его в специализированного помощника для конкретных задач. Каждый скилл содержит проверенные на практике фреймворки, шаблоны и антипаттерны.

## Доступные скиллы

### custdev
**Customer Development для B2C SaaS** — полный цикл от гипотез до аналитического отчёта.

Что умеет:
- Формирование и трекинг гипотез боли
- Генерация скринер-вопросов и глубоких интервью
- Сообщения для рекрутинга (ТГ-канал, чаты, личка, Habr/VC)
- Оценка кандидатов (шкала 1–5) с обоснованием
- Анализ ответов по Mom Test (сильные/слабые/красные сигналы)
- Аналитический отчёт через 10 фреймворков (Blank, Mom Test, JTBD, Lean Startup, Sean Ellis, AARRR и др.)
- Рекомендация go / pivot / kill

Основан на: The Mom Test (Fitzpatrick), Four Steps to the Epiphany (Blank), Jobs To Be Done (Christensen/Ulwick), Lean Startup (Ries), а также на реальном опыте 20+ custdev-интервью.

### building-planning-stack
**Подбор системы планирования под команду** — собирает персональный стэк фреймворков, инструментов и ритуалов под конкретный бизнес.

Что умеет:
- Собирает контекст команды (стадия, размер, ниша, инструменты, боль) через несколько раундов вопросов
- Изучает нишу клиента с нуля через WebSearch, специализированные скиллы и фоновые Agent'ы для сложных кейсов
- Фильтрует AI-slop через E-E-A-T-критерии
- Подбирает стэк по 6 слоям: стратегия / квартальные цели / исполнение / бэклог / приоритизация / инструменты
- Даёт рекомендации в consultant-style: что выбрали, почему, что отвергли
- Учитывает Override rules: прошлые провалы фреймворков, перегрузка команды, бюджет, регуляторика
- Self-review через biases-checklist (planning fallacy, привязка OKR к зарплате, kill criteria)

Работает с любым бизнесом — SaaS, marketplaces, fintech, e-commerce, edtech, deeptech, B2C, B2B.

На выходе — 5 обязательных артефактов (готовые файлы под конкретную команду):
- `planning-stack.md` — главный документ с обоснованиями
- `strategy-draft.md` — V2MOM или OKR-каркас
- `implementation-roadmap.md` — план внедрения по неделям
- `rituals-calendar.md` — календарь ритуалов
- `idea-inbox-starter.csv` — стартовый шаблон бэклога идей

Опционально по запросу: jira-jpd setup guide, books-by-context, question log.

Основан на: Doerr (Measure What Matters), Wodtke (Radical Focus), Grove (High Output Management), Cagan (Inspired/Empowered), Perri (Escaping the Build Trap), Torres (Continuous Discovery Habits), Singer (Shape Up), Rumelt (Good Strategy Bad Strategy), Porter (Competitive Strategy), Kahneman (Thinking Fast and Slow), Duke (Thinking in Bets/Quit).

## Как использовать

### В Claude.ai (веб-чат)
1. В начале чата скопируй содержимое `custdev/SKILL.md` в промпт
2. Скажи «давай проведём custdev для [описание продукта]»
3. Claude проведёт тебя через все этапы

### В Claude Code (терминал)
1. Склонируй репозиторий:
```bash
git clone https://github.com/Infinity-Kim/founder-skills.git
```
2. Положи нужный скилл в проект:
```bash
cp -r founder-skills/custdev .claude/skills/
```
3. Claude Code автоматически подхватит скилл по контексту

## Структура

```
founder-skills/
├── README.md
├── custdev/
│   ├── SKILL.md              # Основной файл скилла (7 этапов)
│   └── references/
│       └── frameworks.md     # 10 фреймворков для анализа
├── building-planning-stack/
│   ├── SKILL.md              # Основной файл скилла (6 этапов)
│   ├── references/           # 8 файлов: фреймворки, приоритизация, инструменты,
│   │                         #   decision-matrix, ритуалы, research-методология,
│   │                         #   biases-checklist, книги
│   └── assets/               # 8 шаблонов: planning-stack, V2MOM, OKR, roadmap,
│                             #   rituals-calendar, idea-inbox, JPD setup, books
└── ...                       # Будущие скиллы
```

## Контакст

Автор: [@Infinity_Kim](https://t.me/Infinity_Kim)
Канал: [@InfinityProductive](https://t.me/InfinityProductive)

## Лицензия

MIT — используйте как хотите.