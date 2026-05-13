# Decision Matrix — правила подбора стэка

Этот файл — главный движок выбора стэка. После сбора контекста в этапе 1 применяй эту матрицу, чтобы выбрать конкретный фреймворк/инструмент для каждого из 6 слоёв.

## TOC
- [Слой 1. Стратегия](#слой-1-стратегия-полугод-год)
- [Слой 2. Квартальные цели](#слой-2-квартальные-цели)
- [Слой 3. Исполнение](#слой-3-исполнение-спринтыциклы)
- [Слой 4. Бэклог](#слой-4-бэклог)
- [Слой 5. Приоритизация](#слой-5-приоритизация)
- [Слой 6. Инструменты](#слой-6-инструменты)
- [Override rules](#override-rules)
- [Combinations: типовые стэки](#типовые-стэки-по-сегменту)

---

## Слой 1. Стратегия (полугод-год)

| Условие | Рекомендация |
|---|---|
| Команда ≤10 чел | **V2MOM** на полгода (одна страница) |
| Команда 10-50, продуктовая | **OKR-каскад**: компания → команды (без индивидуальных OKR) |
| Команда 50-125 | **OKR с каскадом** + годовая стратегия отдельно |
| Команда 125+ | **OKR + Hoshin Kanri** для верхнего уровня |
| Lean производство / opcrew | **Hoshin Kanri** независимо от размера |
| Нон-tech mid-business | **EOS** (Vision + Rocks) |

**Дополнительные модификаторы:**
- Pre-PMF / pivot → V2MOM (легче переписать)
- Регулируемая отрасль → committed-цели без 70%-планки
- Государство / B2G → BSC (Balanced Scorecard)

---

## Слой 2. Квартальные цели

| Условие | Рекомендация |
|---|---|
| pre-PMF | 1-2 Methods из V2MOM на квартал, БЕЗ OKR |
| post-PMF | 3 OKR (Wodtke-style). Не больше |
| scale | 3-4 OKR, маркируй committed vs aspirational |
| Sales / operational team | 4DX (1-2 WIGs) |
| Нон-tech mid-business | EOS Rocks (1-7 на человека) |
| R&D / discovery-команда | OKR с outcome-KR + один learning-KR (что узнаем) |

**Не делать:**
- 5+ OKR на квартал = не приоритизировал
- OKR на 6 мес или год — это уже стратегия, не tactical
- Привязка OKR к зарплате (по Wodtke и Doerr — извращает систему)

---

## Слой 3. Исполнение (спринты/циклы)

| Условие | Рекомендация |
|---|---|
| 2-5 чел, автономная команда, продуктовая работа | **Shape Up** (6-нед циклы + 2-нед cool-down) или Kanban |
| 5-15 чел, есть зависимости с другими командами | Scrum 2-нед спринты |
| Гибрид: **уже есть Scrum, нужно добавить betting** | Scrum 2-нед + **Shape Up 6-нед betting cycle поверх** (каждые 3 спринта = betting table) |
| 15-50 чел, несколько команд | Scrum + Scrum of Scrums или LeSS |
| 50-125 чел | **SAFe PI Planning** (12-нед PI) |
| 125+ чел | SAFe + LeSS Huge |
| Регулируемые контракты с датами | Scrum с фиксированными релизами, не Shape Up |

**Override:**
- Если уже работает что-то 6+ месяцев и команда довольна — не ломай. Дополни, не замени.
- Если команда не доводит спринты до конца — не вопрос фреймворка, вопрос capacity-планирования.

---

## Слой 4. Бэклог

| Условие | Рекомендация |
|---|---|
| Команда любого размера + поток идей от фаундера | **Now/Next/Later + отдельный Idea Inbox** (product backlog ≠ delivery backlog) |
| Контрактные обязательства | Now/Next/Later + временной milestone-лейн |
| Engineering-only команда без потока идей | Sprint backlog в Jira достаточно |
| SAFe-команды | Program Backlog + Team Backlog |

**Главное правило:** идеи и задачи в разных воронках. Иначе бэклог Jira станет свалкой и команда перестанет в него смотреть.

---

## Слой 5. Приоритизация

| Условие | Рекомендация |
|---|---|
| Стартап pre-PMF / ранний post-PMF, мало данных о Reach | **ICE** (Impact × Confidence × Ease) |
| Зрелый продукт с известной аудиторией | **RICE** (с Reach) |
| Переговоры со стейкхолдерами о scope | **MoSCoW** для согласования + ICE/RICE внутри Must |
| SAFe-окружение | **WSJF** |
| Customer research, восприятие фич | **Kano** (опросный) |
| Быстрая сессия команды без подготовки | **Value vs Effort** (2×2) |

**Хаки из Avito (для команд 6-15 post-PMF):**
- Задачи ≤2 SP — без скоринга, автоматически высокий приоритет
- Одна «зелёная» (морально-командная) задача в каждый спринт, даже если ICE низкий
- PSBR — 30 мин раз в неделю / 2 недели

---

## Слой 6. Инструменты

| Условие | Idea backlog | Delivery backlog | Strategy docs |
|---|---|---|---|
| Solo founder | Apple Notes / Notion | Linear / Things | Doc |
| 2-5 чел, нет Jira | Airtable Free / Notion | Linear Free | Notion |
| 2-5 чел, есть Jira | JPD Free (если 3 creators хватает) | Jira Free | Notion / Doc |
| 6-15 чел, есть Jira | **JPD Free (default)** | **Jira Free** | Notion / Doc + опц. OKR-инструмент |
| 6-15 чел, нет Jira | Linear + Notion | Linear | Notion |
| 6-15 чел, JPD 3 creators НЕ хватает | Custom issue types Idea + Initiative в Jira + JQL | Jira Free | Notion |
| 15-50 чел | JPD Standard ($10/creator) | Jira Standard | Lattice / Mooncamp |
| 50+ чел | JPD Premium + Jira Plans | Jira Premium + SAFe | Quantive / Workboard |
| Нон-tech mid-business | Asana / Monday | Asana / Monday | Slides / Doc |
| Регулируемая отрасль | JPD Standard+ (audit) | Jira Premium (audit) | Confluence |

**Default для 6-15 tech-команды:** **JPD Free + Jira Free**. Это бесплатно, нативно, реализует двухвороночный паттерн (Cagan/Torres/Perri).

---

## Override rules

Применяй до основной матрицы. Эти правила бьют общие рекомендации.

### Override 1: Прошлый неудачный опыт
**Если фаундер пробовал X и не зашло** → не рекомендуй X. Спроси, что именно не сработало, и выбери альтернативу:
- OKR не зашёл → V2MOM
- Scrum не зашёл → Shape Up или Kanban
- Jira не зашла → Linear

### Override 2: Перегрузка команды
**Если в этапе 1 проявились признаки перегрузки** (overtime, недавние увольнения, фраза «команда устала», 2+ цели сейчас не доделаны) → план должен **разгружать**, не нагружать:
- Снизить количество OKR (1-2 вместо 3)
- НЕ добавлять новые ритуалы (только заменять существующие)
- Roadmap внедрения растянуть на 8 недель вместо 4

### Override 3: Бюджет
**Если бюджет = $0** → только Free-варианты. Не «лучше было бы Premium». Если выбор Free действительно ограничивает — назвать это явно: «есть лимит X, при росте до Y надо будет заплатить».

### Override 4: Регулируемая отрасль
**Если банк / медицина / госуслуги** →
- OKR с 70%-планкой = красный флаг (compliance не терпит «не дотянули»)
- Используй committed-only OKR
- Excel/Google Sheets для документов = compliance проблемы (audit logs нужны)
- SAFe лучше Shape Up (структурированность и трассируемость)

### Override 5: Удалённая команда в разных часовых поясах
- Асинхронные ритуалы важнее синхронных
- Friday Demo заменить на Friday Loom-видео
- Betting Table — async через документ + сонэндинг звонок

### Override 6: Контрактные обязательства / агентство
- Shape Up не подходит (не передаёт обязательств наверх)
- Timeline-роадмап нужен (с датами)
- Now/Next/Later — только для внутренних, для клиента — milestone-план

---

## Типовые стэки по сегменту

### Tech-стартап 6-15 чел, post-PMF, есть Jira
```
Стратегия:        V2MOM на полгода
Кварт. цели:      3 OKR (Wodtke-style)
Исполнение:       Scrum 2-нед + Shape Up 6-нед betting поверх
Бэклог:           Now/Next/Later + Idea Inbox
Приоритизация:    ICE (PSBR раз в 2 нед) + MoSCoW для commitments
Инструменты:      Jira Free + JPD Free + Notion для docs
```

### Tech-стартап 2-5 чел, pre-PMF
```
Стратегия:        V2MOM (1 страница, фокус на Methods)
Кварт. цели:      1-2 Methods + learning-цели
Исполнение:       Shape Up или Kanban
Бэклог:           Now/Next/Later в Linear/Notion
Приоритизация:    ICE
Инструменты:      Linear Free + Notion Free
```

### Scale-up 15-50 чел, post-PMF
```
Стратегия:        OKR-каскад (компания → команды)
Кварт. цели:      OKR компании + 2-3 командных OKR
Исполнение:       Scrum 2-нед + Scrum of Scrums
Бэклог:           Now/Next/Later в JPD Standard
Приоритизация:    RICE на портфельном уровне + ICE внутри
Инструменты:      Jira Standard + JPD Standard + Lattice (OKR)
```

### Enterprise 50+ чел
```
Стратегия:        OKR + Hoshin Kanri (для верхнего уровня)
Кварт. цели:      OKR с каскадом, committed vs aspirational
Исполнение:       SAFe PI Planning
Бэклог:           Program Backlog + Team Backlog в JPD Premium
Приоритизация:    WSJF (SAFe-стандарт)
Инструменты:      Jira Premium + JPD Premium + Workboard
```

### Нон-tech mid-business
```
Стратегия:        EOS (Vision + Rocks)
Кварт. цели:      Rocks (1-7 на человека)
Исполнение:       Level 10 Meeting weekly + проектные планы
Бэклог:           Asana / Monday lists
Приоритизация:    Value vs Effort + MoSCoW
Инструменты:      Asana / Monday + Google Workspace
```

### Sales / Customer Success команда
```
Стратегия:        OKR компании
Кварт. цели:      4DX (1-2 WIGs)
Исполнение:       WIG-sessions weekly
Бэклог:           CRM (Salesforce / Pipedrive)
Приоритизация:    Pipeline value
Инструменты:      CRM + Slack для cadence
```

---

## Финальная проверка

После применения матрицы пройди:
- Все 6 слоёв заполнены
- Override rules применены
- Стэк не противоречит сам себе (например, Shape Up в команде 6-15 + Scrum 2-нед спринты — это гибрид, не противоречие, но проверь)
- Бюджет соблюдён
- Команда не перегружена (Override 2)

После — переходи к этапу 4 (Implementation Roadmap).
