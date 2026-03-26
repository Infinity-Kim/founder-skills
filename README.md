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
└── ...                       # Будущие скиллы
```

## Контакст

Автор: [@Infinity_Kim](https://t.me/Infinity_Kim)
Канал: [@InfinityProductive](https://t.me/InfinityProductive)

## Лицензия

MIT — используйте как хотите.