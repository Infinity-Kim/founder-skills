# Инструменты для планирования и бэклога

## TOC
- [Принцип двух воронок](#принцип-двух-воронок-product-vs-delivery)
- [Jira Cloud](#jira-cloud)
- [Jira Product Discovery (JPD)](#jira-product-discovery-jpd)
- [Linear](#linear)
- [Notion](#notion)
- [Airtable](#airtable)
- [Excel / Google Sheets](#excel--google-sheets)
- [Asana / Monday / ClickUp](#asana--monday--clickup)
- [Матрица «размер команды × инструмент»](#матрица-размер-команды--инструмент)
- [Default рекомендации](#default-рекомендации)

---

## Принцип двух воронок (Product vs Delivery)

Главный паттерн 2024-2026 (Cagan, Torres, Perri, Atlassian docs):

```
PRODUCT BACKLOG (идеи)              DELIVERY BACKLOG (задачи)
─────────────────────               ──────────────────────
Где: JPD / Notion / Airtable        Где: Jira / Linear
Кто: PM + фаундер + stakeholders    Кто: команда разработки
Статусы: Inbox→Triage→Discovery→    Статусы: Backlog→To Do→In
         Validated                            Progress→Review→Done
Метрика: количество гипотез,         Метрика: velocity, lead time,
         конверсия валидации                 predictability
```

68% продуктовых команд застревают на смешивании этих воронок (ProductPlan State of PM). Не смешивай. Граница — момент «promotion»: идея провалидирована → создаётся Epic в delivery-системе.

---

## Jira Cloud

Стандарт IT-команд. Иерархия: Project → Epic → Story → Task → Sub-task.

### Free
- 10 users
- 100 automation runs / месяц
- 1 project для automation rules
- Custom fields, custom issue types, JQL, workflows
- 2 GB файлов
- Неограниченно projects и issues
- **НЕТ** custom hierarchy выше Epic (Initiative/Theme — только Premium)

### Standard ($8.60/user/мес)
- 50,000 users
- Unlimited automation, multi-project
- Audit logs, role-based permissions

### Premium ($17/user/мес)
- **Plans / Advanced Roadmaps** — Initiative > Epic > Story иерархия
- Cross-project planning, capacity, dependency mapping

### Когда подходит
- Команда разработки 5+ человек
- Уже привыкли к Scrum/Kanban
- Нужны автоматизации, отчётность

### Когда НЕ подходит
- Команда <5 человек (overhead настройки)
- Не-tech команды (Asana проще)

---

## Jira Product Discovery (JPD)

Atlassian создал JPD специально для product backlog (отдельно от Jira Software).

### Free
- **3 creators** + unlimited contributors (комментаторы, голосователи)
- 200 automations / месяц
- 2 GB
- Pre-built templates: Prioritization, Customer Feedback, Roadmap

### Standard ($10/creator/мес, contributors бесплатны)

### Возможности
- Custom fields для ICE/RICE/Impact/Effort встроены
- Views: Roadmap (Now/Next/Later), Matrix (2×2), Board, List
- Нативная связь с Jira Software: Idea → Epic в один клик
- Insights — прикрепление цитат клиентов, ссылок, файлов к идее

### Когда подходит
- Команды 6-50 человек с Jira Software
- Нужно разделение product/delivery backlog
- 3 creators хватает (фаундер + PM/CPTO + senior)

### Когда НЕ подходит
- >3 человек должны заводить идеи (нужен Standard)
- Нет Jira — JPD без неё имеет ограниченный смысл

---

## Linear

Современная альтернатива Jira. Быстрая, красивая, минимум overhead.

### Free
- 250 issues active
- 2 teams
- Unlimited users

### Standard ($8/user/мес)
- Unlimited issues
- 6 months history

### Когда подходит
- Tech-команды 2-50 человек, ценящие скорость и UX
- Дискаверти-фаза, где Jira избыточен

### Когда НЕ подходит
- Нужны мощные кастомизации (Linear их не любит)
- Большие enterprise-процессы

---

## Notion

Универсальный workspace: documents + databases + wiki.

### Free
- Unlimited blocks для personal
- 10 guests
- 7 days page history

### Plus ($10/user/мес), Business, Enterprise

### Применение для планирования
- Strategy docs (V2MOM, OKR)
- Idea Inbox через database
- Wiki / Process documentation

### Когда подходит
- Маленькие команды (2-5 чел), где нет Jira
- Документация и базы данных идей в одном месте

### Когда НЕ подходит
- 200+ идей в базе — Notion начинает тормозить
- Команды разработки 10+ — нужна Jira/Linear для delivery

---

## Airtable

База данных в виде spreadsheet с views, формулами, API.

### Free
- **1,000 records на base** (узкое горло на 6-12 мес)
- 5 editors maximum
- 1 GB на base
- 100 automations / месяц
- 1 interface на base
- 1,000 API calls / месяц
- AI credits 250/editor/мес

### Team ($20/user/мес)
- 50k records, 5 GB

### Когда подходит
- Нужны гибкие views (Kanban, Calendar, Grid, Form)
- Мощные формулы
- Low-code workflows
- 1,000 записей достаточно

### Когда НЕ подходит
- Деливерти-задачи (Jira/Linear лучше)
- Нужна нативная связь с разработкой
- Бэклог идей превысит 1000 — нужно платить

---

## Excel / Google Sheets

### Когда подходит
- **Разовые расчёты:** knapsack-планирование квартала, OKR grading, капасити
- **ICE/RICE-сессии** когда команда сидит вместе
- Quick analysis

### Когда НЕ подходит
- Постоянный бэклог (нет workflow, ручные статусы)
- Командное использование (конфликты при правке, версионирование плохое)
- Линковка с источниками (всё текстом)
- >200 строк — становится больно

---

## Asana / Monday / ClickUp

Универсальные project management для нон-tech.

### Когда подходит
- Маркетинговые команды, операции, контентные
- Mid-business без сильной IT-составляющей
- 10-50 человек

### Когда НЕ подходит
- Tech-команды с нативной IDE-интеграцией (Jira/Linear лучше)

---

## Матрица «размер команды × инструмент»

| Команда | Идеи (product backlog) | Задачи (delivery) | Стратегия |
|---|---|---|---|
| Solo (1) | Notion / Apple Notes | Linear / Things / Todoist | Doc |
| 2-5 | **Airtable Free** или **JPD Free** | Linear Free / Jira Free | Notion / Doc |
| 6-15 | **JPD Free + Jira Free** | **Jira Free** | Notion / Doc + OKR-инструмент опционально |
| 15-50 | JPD Standard | Jira Standard | Lattice / Workboard / встроенно в Jira |
| 50-125 | JPD Standard / Premium | Jira Premium | OKR-софт (Lattice, Mooncamp, Workboard) |
| 125+ | JPD Premium + Jira Plans | Jira Premium + SAFe | Enterprise OKR (Quantive, Workboard) |

---

## Default рекомендации

### Команда 2-5 без существующих инструментов
**Linear Free + Notion Free.** Самый низкий overhead, обе платформы быстрые.

### Команда 6-15 с существующей Jira
**Jira Free (есть) + JPD Free (добавить).** Бесплатно, нативная интеграция, реализует разделение product/delivery backlog. Backup если 3 creators не хватает — всё в Jira через custom issue types Idea + Initiative + JQL-дашборды.

### Команда 6-15 без существующей Jira
Два варианта:
- **Linear + Notion** (если культура продукт-команды, минимум процессов)
- **Jira Free + JPD Free** (если нужны процессы Scrum/Kanban с самого начала)

### Команда 15-50
**Jira Standard + JPD Standard.** Платят 8-10 баксов с человека, но получают всё необходимое.

### Команда 50+
**Jira Premium с Plans + JPD Premium + отдельный OKR-софт.** Lattice / Mooncamp / Quantive.

### Нон-tech mid-business
**Asana / Monday + EOS-track для Rocks.**

### Регулируемые отрасли
**Jira Premium (audit logs обязательны) + JPD Standard.** Excel — никогда (compliance проблемы).

---

## Override rules для выбора инструмента

- Если у команды **уже работает что-то** — не предлагай миграцию, разве что текущее ломается. Стоимость миграции почти всегда выше выгоды.
- Если **бюджет = $0** — только Free-варианты. Не намекать на «лучше было бы Premium».
- Если **есть compliance** (банки, медицина) — Excel/Google Sheets никогда.
- Если **команда удалённая в разных часовых поясах** — Linear / Jira / JPD (асинхронность встроена), не Excel/Notion как primary delivery.
