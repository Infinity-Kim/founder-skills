# Research-методология (как изучать любую нишу с нуля)

Это **главный файл** для адаптации скилла под любой бизнес. Скилл не зашивает специфику конкретных ниш — он изучает их на лету.

## TOC
- [1. Стандартный набор для любой ниши](#1-стандартный-набор-для-любой-ниши)
- [2. E-E-A-T-фильтры (отсев AI-slop)](#2-e-e-a-t-фильтры-отсев-ai-slop)
- [3. Две стратегии глубины](#3-две-стратегии-глубины-light-vs-deep)
- [4. Специализированные скиллы](#4-специализированные-скиллы)
- [5. Шаблон брифа для фонового Agent](#5-шаблон-брифа-для-фонового-agent)
- [6. Что делать с результатами research](#6-что-делать-с-результатами-research)

---

## 1. Стандартный набор для любой ниши

Эти 5 категорий нужно покрыть для любого бизнеса:

### 1.1 Конкуренты и лидеры

- Кто 3-5 лидеров в нише (по доле рынка, узнаваемости, выручке)
- Какие фреймворки/процессы они **открыто описывают** (блоги, конференции, подкасты, kupasa)
- Кто из них недавно «упал» или провёл pivot — что из этого следует

**Поисковые запросы:**
- "top [niche] companies 2026"
- "[niche] market leaders product strategy"
- "best [niche] startups how they work"
- "[конкретный лидер] blog culture process"

### 1.2 Метрики и unit-экономика ниши

Каждая ниша имеет свои канонические метрики. Скилл должен их знать, чтобы рекомендовать корректные KR.

| Тип ниши | Канонические метрики |
|---|---|
| SaaS B2B | MRR, ARR, LTV/CAC, NRR, NDR, Magic Number, payback |
| SaaS B2C | DAU/MAU, retention, ARPU, conversion to paid |
| E-commerce | GMV, AOV, take rate (для marketplaces), conversion, basket size |
| Marketplaces | GMV, take rate, sellers active, buyers active, liquidity |
| Mobile consumer | DAU, MAU, session length, retention D1/D7/D30, ARPDAU |
| Fintech | AUM, transaction volume, NIM, payment success rate, regulatory metrics |
| Adtech | CPM, CTR, fill rate, viewability |
| Healthtech | Active patients, adherence, claims processed, MLR |
| DeepTech | TRL (Technology Readiness Level), grants raised, pilots signed |

**Поисковые запросы:**
- "[niche] key metrics benchmarks 2026"
- "[niche] unit economics SaaS metrics"
- "north star metric [niche] startup"

### 1.3 Регуляция и ограничения

- Платформенные правила (App Store, Google Play, маркетплейсы)
- Юридические (GDPR, ФЗ-152, CCPA, fintech-регуляторы — CFPB, FCA, ЦБ РФ)
- Compliance (HIPAA, PCI-DSS, SOC2, ISO 27001, KYC/AML)

Эти ограничения часто **определяют тип OKR** (committed vs aspirational) и **тип инструмента** (audit logs обязательны для compliance).

**Поисковые запросы:**
- "[niche] regulatory requirements 2026"
- "[niche] compliance startup"
- "[platform name] developer rules limits"

### 1.4 Книги и эксперты под нишу

- 3-5 книг именно про эту нишу
- 2-3 эксперта, чьи подкасты/блоги читают практики

Не заменяет общие книги (Cagan, Doerr, Wodtke), а **дополняет** их доменной специфики.

**Поисковые запросы:**
- "best books [niche] founder reading list"
- "[niche] product playbook"
- "must-read books [industry]"

**Канонические книги по типам ниш:**

| Ниша | Книги |
|---|---|
| SaaS B2B | "The SaaS Playbook" (Tunguz), "From Impossible to Inevitable" (Ross), "Crossing the Chasm" (Moore) |
| Marketplaces | "Platform Revolution" (Parker), "Modern Monopolies" (Moazed) |
| Consumer mobile | "Hooked" (Eyal), "Predictably Irrational" (Ariely) |
| Fintech | "The Fintech Book" (Chishti), "Bank 4.0" (King) |
| Hardware/DeepTech | "The Hardware Startup" (Lemkin), "Make: Hardware Startup" |
| B2C/Growth | "Traction" (Weinberg), "Growth Hacker Marketing" (Holiday) |
| Marketplaces, Network effects | "Cold Start Problem" (Chen), "Crossing the Chasm" |

### 1.5 Industry insights и тренды

- Что происходит в нише за последние 6-12 месяцев
- Какие новые тренды влияют на стратегию
- Что обсуждают thought leaders

**Источники E-E-A-T:**

| Тип | Конкретные источники |
|---|---|
| Tech industry | Stratechery (Thompson), a16z newsletter, First Round Review, Lenny's Newsletter |
| Подкасты | Acquired, Invest Like the Best, How I Built This, The Tim Ferriss Show |
| SaaS | SaaStr blog, ChartMogul blog, OpenView |
| Fintech | TechCrunch Fintech, The Pomp Letter, Finlance Podcast |
| E-com / Marketplaces | Modern Retail, Marketplace Pulse |
| Российский tech | vc.ru, Habr (компании), РБК Pro, podcasts «Соль» / «Запуск» |

**Поисковые запросы:**
- "[niche] trends 2026"
- "[niche] industry analysis 2026"
- "podcast [niche] founders interview"

---

## 2. E-E-A-T-фильтры (отсев AI-slop)

Google использует E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) для ранжирования. То же — для нас.

### Что отсеивать

| Red flag | Признак |
|---|---|
| Generic AI-slop | Бесцветный текст, нет конкретных цифр, нет автора, дублирующиеся фразы |
| Контент без автора | Нет имени автора и его credentials |
| Дублирующиеся «топ-10» | Сравнительные обзоры без оригинальных данных, одинаковые во всех источниках |
| Hallucinated stats | Цифры без ссылки на источник, статистика «90% компаний...» без раскрытия выборки |
| Outdated | Контент >2 лет старого без явной маркировки актуальности |

### Что приоритезировать

| Источник | Почему доверять |
|---|---|
| Оригинальные исследования | С собственными данными, методологией, выборкой |
| Прямой контент от практиков | Блоги CEO/CPTO своих компаний |
| Академические работы | Peer-reviewed журналы |
| Изданные книги | Прошли редакторский фильтр |
| Подкасты-интервью с лидерами | Сам лидер говорит, не пересказчик |
| Industry reports от консультантов | McKinsey, BCG, Bain — обзоры рынков |
| Verified data sources | Statista, Crunchbase, Pitchbook, App Annie |

### Тест на качество источника

Перед использованием источника спроси:
1. Есть ли автор и его credentials?
2. Есть ли в тексте оригинальные данные или только пересказ?
3. Указаны ли источники цифр?
4. Дата публикации видна?
5. Если бы фаундер прочитал это — нашёл бы что-то новое или это «вода»?

Если хотя бы один ответ «нет/неясно» — не использовать как primary source. Использовать только как дополнительный signal.

---

## 3. Две стратегии глубины (Light vs Deep)

Выбор зависит от того, насколько ниша «mainstream» (много готовой информации) vs «специфическая» (нужно глубокое погружение).

### Light Research (≤5 минут)

**Для каких ниш:** SaaS, e-commerce, fintech, marketplaces, mobile consumer — широко документированные сегменты.

**Как:**
1. 2-3 WebSearch с конкретными запросами по 1.1-1.5
2. 1-2 WebFetch топовых E-E-A-T статей
3. Если есть `wb-docs` / `[platform]-docs` скилл — invoke

**Когда хватает Light:**
- Ниша описана в множестве authoritative sources
- Метрики стандартные (SaaS = MRR/LTV/CAC)
- Регуляция понятна без углубления

### Deep Research (10-15 минут, параллельно)

**Для каких ниш:** DeFi, биотех, регулируемые отрасли (фарма, банки), новые AI-категории, нишевые B2B (например, аналитика для конкретного маркетплейса), госсектор.

**Как:**
1. Спавнить фоновый Agent (`subagent_type=general-purpose`, `run_in_background=true`) с брифом (см. раздел 5)
2. Параллельно начать этап 3 (Stack Selection) на основе общих принципов
3. Когда Agent вернётся (нотификация) — обогатить рекомендации специфическими insights

**Когда нужен Deep:**
- Ниша редко описана
- Регуляция специфическая
- Лидеры не публичные, нужно копать
- Контекст клиента уникален (типа «авторизованный сервис WB» — нужно понять что это такое и какие обязательства)

---

## 4. Специализированные скиллы

Если в системе Claude Code установлен скилл, релевантный нише — invoke его. Это даёт **свежие, локальные данные** без зависимости от WebSearch.

### Известные специализированные скиллы

- `wb-docs` — Wildberries API и документация
- (потенциально) `ozon-docs` — Ozon API
- (потенциально) `aws-docs`, `gcp-docs` — для cloud-стартапов
- (потенциально) `stripe-docs`, `paddle-docs` — для SaaS-billing
- (потенциально) `appstore-docs`, `googleplay-docs` — для mobile

### Как использовать

1. Проверь, есть ли скилл в текущей сессии (системные напоминания в начале)
2. Если есть — invoke с конкретным запросом по нише (не общим)
3. Проверь актуальность метаданных скилла (дата последнего обновления). Если >3-6 месяцев — попроси скилл обновиться (если у него есть такая опция).
4. Объедини данные из скилла с WebSearch для свежих industry trends

### Если специализированного скилла нет

- Не пытаться «придумать» что есть. Если нет скилла для X — стандартный WebSearch.
- Если research показывает, что специализированный скилл был бы полезен — отметь в финальном артефакте «рекомендую установить/создать скилл `[name]-docs`».

---

## 5. Шаблон брифа для фонового Agent

Используй этот шаблон при спавне Deep Research Agent. Адаптируй [НИША] и любые специфичные пункты.

```
Исследуй нишу [НИША] для подбора системы планирования продуктовой команде.

Команда клиента:
- Стадия: [pre-PMF / post-PMF / scale / pivot]
- Размер: [N человек]
- Главная боль: [короткое описание]

Нужно собрать:

1. **3-5 лидеров рынка** в этой нише
   - Названия компаний
   - Что публично известно об их подходе к планированию / процессам / продуктовой разработке
   - Если есть блоги CEO/CPTO — прямые ссылки

2. **Ключевые метрики ниши**
   - Какие 3-5 метрик считаются north star
   - Какие benchmark'и существуют (например, «хороший LTV/CAC для SaaS — 3+»)
   - Что измеряют лидеры

3. **Регуляторные ограничения**
   - Платформенные правила (если применимо)
   - Юридические требования
   - Compliance frameworks

4. **3-5 книг именно про эту нишу**
   - Авторы, годы, ключевые тезисы
   - Каноническая ли это книга в нише?

5. **Industry insights и тренды последних 6-12 месяцев**
   - Что происходит на рынке
   - Какие сдвиги повлияли на стратегии лидеров
   - Какие новые сегменты появились

**Критерии источников (E-E-A-T):**
- Только: оригинальные данные с авторами и credentials, изданные книги, peer-reviewed работы, подкасты-интервью с лидерами, industry reports McKinsey/BCG/Bain
- НЕ брать: generic top-10 SEO-статьи, AI-slop, контент без указания автора, hallucinated stats

**Формат вывода:** структурированный markdown под 2 страницы. Каждое утверждение — со ссылкой на источник. Цифры — с указанием года и методологии.

Если ниша редкая и достоверных источников <5 — честно отметить «ограниченные данные» и указать какие сделаны допущения.
```

---

## 6. Что делать с результатами research

После того как research завершён (Light или Deep), используй данные в этапах 3-5:

### Этап 3 (Stack Selection)
- Метрики ниши → конкретные KR в OKR draft
- Подходы лидеров → валидация выбора (например, «Stripe тоже использует Shape Up — это поддерживает наш выбор»)
- Регуляция → Override rules (committed-only OKR для регулируемой)

### Этап 4 (Roadmap)
- Тренды → срочность некоторых пунктов roadmap (например, «AI становится must-have в нише — заложить research-цикл»)

### Этап 5 (Artifacts)
- Книги под нишу → отдельный артефакт `books-by-context.md`
- Регуляция → отдельный пункт в `planning-stack.md` («Compliance: что учесть»)
- Лидеры → опционально упомянуть в `planning-stack.md` как референс («лидер ниши X использует подход Y, это валидирует наш выбор»)

### Этап 6 (Self-review)
- Проверь: рекомендации не противоречат регуляции
- Проверь: метрики ниши попали в KR

---

## Anti-patterns research

1. **Не выдумывать данные.** Если ниша редкая и данных мало — честно сказать «ограниченные источники».

2. **Не цитировать AI-slop как авторитет.** Generic «10 best SaaS tools 2026» статьи — не source.

3. **Не делать research ради research.** Цель — собрать данные для подбора стэка, не для импрессии клиента.

4. **Не углубляться в нишу больше 15 минут.** Если за 15 минут не нашёл достаточно — переходить к Stack Selection с допущениями.

5. **Не путать факты ниши и facts продукта клиента.** Research — про нишу в целом. Контекст клиента — из этапа 1.
