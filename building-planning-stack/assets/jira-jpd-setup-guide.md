# Jira + JPD Setup Guide

> Пошаговая инструкция: как подключить Jira Cloud Free + Jira Product Discovery Free и настроить под двухвороночную модель (product backlog ≠ delivery backlog).

**Время на настройку:** 2-3 часа.
**Бюджет:** $0 (всё на Free tier).

---

## Что у вас получится

После настройки:
- **Jira Software Free** — для delivery (эпики, стори, спринты, как у вас сейчас).
- **JPD Free** — для product backlog (идеи, скоринг, Now/Next/Later roadmap).
- Связь между ними: Idea в JPD → Promote → Epic в Jira Software.

**Лимиты Free:**
- Jira Software: 10 users, 100 automation runs/мес.
- JPD: 3 creators + unlimited contributors, 200 automations/мес.

---

## Часть 1: Подключение JPD

### Если у вас уже есть Jira Cloud

1. Войдите в Jira Cloud admin panel.
2. Найдите **Add product** → Jira Product Discovery.
3. Выберите Free plan. Подтвердите. Установка занимает ~5 минут.
4. После установки в левом меню появится Jira Product Discovery.

### Если у вас нет Jira

1. Зарегистрируйтесь на [atlassian.com](https://atlassian.com) (бесплатно для 10 users).
2. Создайте организацию.
3. Установите Jira Software Free.
4. Затем добавьте Jira Product Discovery (см. выше).

### Назначение creators в JPD

В Free есть только **3 creator-slots**. Назначьте их:
- Фаундер (обязательно)
- CPTO / Product lead (обязательно)
- 1 senior engineer или sales-lead (опц.)

Все остальные — contributors (бесплатно). Они могут:
- Комментировать идеи
- Голосовать
- Прикреплять insights (цитаты клиентов)
- Видеть весь backlog

Не могут:
- Создавать новые идеи
- Менять статусы

---

## Часть 2: Настройка JPD

### Создание проекта

1. JPD → Create project → выбрать template **"Prioritization"** (приходит с ICE/RICE полями).
2. Назвать: например, "Product Ideas".
3. Privacy: Open (все contributors видят) или Private (только creators).

### Custom fields под ваш кейс

Template "Prioritization" даёт по умолчанию:
- Impact (1-10)
- Confidence (1-10)
- Ease (1-10)
- ICE Score (formula = Impact × Confidence × Ease)

Добавьте дополнительные fields под ваш стэк:

1. **Status** (single select): Inbox / Triage / Discovery / Validated / Promoted / Bucket
2. **Source** (multi-select): Founder / Customer / Team / Competitor / Industry / Research
3. **Linked OKR** (single select): O1 / O2 / O3 / O4
4. **Appetite** (single select, Shape Up style): 1 неделя / 2 недели / 6 недель / Epic
5. **Niche-specific field** (single select / checkbox) — что-то специфическое для вашей ниши

### Views

Создайте 4 views:

1. **Inbox** — фильтр: Status = Inbox. Сюда сыпется всё.
2. **Triage** — фильтр: Status = Triage. Что обрабатываем на PSBR.
3. **Validated (для Betting Table)** — фильтр: Status = Validated, sort by ICE Score DESC. Для betting.
4. **Roadmap Now/Next/Later** — group by Status (Now = Promoted + assigned current cycle, Next = Validated, Later = Discovery).
5. **Matrix Impact × Effort** — встроенная 2×2 матрица. Для quick visual prioritization.

### Pitch template (description)

Для идей со статусом Validated должен быть заполнен pitch. Создайте template (можно вручную как памятку):

```
## Проблема
[От кого слышали, у скольких]

## Аппетит
[1 неделя / 2 недели / 6 недель]

## Решение в общих чертах
[Без UI — это потом]

## Что НЕ входит в скоуп
[Важно!]

## Риски
[Что может пойти не так]
```

---

## Часть 3: Настройка Jira Software

Если у вас уже есть Jira с custom fields — пропустить. Если с нуля:

### Создание проекта

1. Create project → выбрать **Scrum** или **Kanban** template (зависит от вашего стэка).
2. Назвать, например "Product Delivery".

### Custom fields на Epic

Добавьте поля, чтобы можно было трассировать от Idea в JPD к Epic в Jira:

1. **Linked OKR** (single select) — какому KR служит этот Epic.
2. **Outcome / hypothesis** (text) — что ожидаем доказать.
3. **JPD Idea link** (URL) — на исходную идею.
4. **Pitch link** (URL) — на pitch-документ.

На Story:
1. **ICE Impact** / **Confidence** / **Ease** (numbers) — для приоритизации внутри Epic.
2. **Pitch link** (URL).

### Workflow

Default workflow Jira:
- To Do → In Progress → Code Review → QA → Done

Адаптируйте под себя. Главное — не усложнять, на команде 6-15 чел этого достаточно.

### Sprints

Если Scrum — длительность спринта 2 недели. Если Shape Up-гибрид — спринты остаются 2-нед, но **6-нед циклы Shape Up** трекаются через Labels или Component (каждые 3 спринта = один betting cycle).

### JQL-дашборды

Создайте 3 dashboards:

1. **«Sirот без OKR»** — Story без `Linked OKR`. JQL:
   ```
   project = "Product Delivery" AND type = Story AND "Linked OKR" is EMPTY
   ```
   Это сразу видно «осиротевшие» задачи, не привязанные к стратегии.

2. **«Прогресс по OKR O1»** — все Story и Epic, связанные с O1, по статусам.

3. **«Sprint health»** — committed vs delivered за последние 6 спринтов.

---

## Часть 4: Связка JPD ↔ Jira Software

### Promote Idea → Epic

В JPD на любой Idea со статусом Validated есть кнопка **"Convert to Jira issue"** (нативная функция):
1. Открыть Idea.
2. Найти кнопку Convert → Epic in Jira Software.
3. Выбрать project = "Product Delivery".
4. Поля автоматически копируются: description → pitch summary, links сохраняются.

После promotion:
- Idea остаётся в JPD со статусом Promoted и линком на Epic.
- Epic в Jira имеет линк обратно на Idea.
- Прогресс Epic виден в JPD через Delivery Status.

### Synchronization

JPD автоматически синхронизирует:
- Статус Epic в Jira → Delivery Status в JPD
- Прогресс Story под Epic → процент выполнения в JPD

Это nativnaya связь, не нужно настраивать webhook'и.

---

## Часть 5: Automation rules (Free = 100 runs/мес)

В JPD создайте 1-2 automation rules:

### Rule 1: Auto-assign Source = Founder

**Trigger:** Idea создана user'ом «фаундер»
**Action:** Установить Source = Founder, Status = Inbox

Это автоматически тегает идеи от фаундера.

### Rule 2: Slack notification on Validated

**Trigger:** Status changed to Validated
**Action:** Send Slack message в канал #product

Команда видит, что идея прошла триаж и готова к betting.

---

## Часть 6: Backup-вариант (если 3 creators JPD не хватает)

Если вам нужно, чтобы **более 3 человек создавали идеи**, JPD Free не подходит. Варианты:

### Вариант A: Заплатить за JPD Standard
$10/creator/мес. На команду 6-15 чел — 4-6 creators обычно достаточно ($40-60/мес).

### Вариант B: Всё в Jira Software через custom issue types

Создайте в Jira:

1. **Issue type Idea** — для сырых идей.
   - Workflow: Inbox → Triage → Discovery → Validated → Promoted → Bucket
   - Custom fields: те же, что в JPD (ICE, Source, etc.)

2. **Issue type Initiative** — для квартальных ставок (на Free нельзя над Epic, но можно через issue links).
   - Связь: Initiative `implements` Objective; Epic `implements` Initiative.

3. **Issue type Objective** — для OKR.
   - Custom fields: тип (committed/aspirational), KR-список.

4. **JQL views** заменяют JPD views:
   - `type = Idea AND status = Inbox`
   - `type = Idea AND status = Validated ORDER BY "ICE Score" DESC`
   - `type = Epic AND "Linked Initiative" = X`

**Минус:** нет визуального Now/Next/Later (только списки). Нет встроенной Matrix view. Но всё в одной системе, все 10 пользователей могут создавать.

---

## Чек-лист после настройки

- [ ] JPD подключён, Free plan активен
- [ ] 3 creators назначены
- [ ] Custom fields созданы (Status, Source, Linked OKR, Appetite)
- [ ] 4 views настроены (Inbox, Triage, Validated, Roadmap)
- [ ] Pitch template добавлен в description
- [ ] Jira Software настроен с custom fields на Epic
- [ ] Связка Idea → Epic работает (потестировать на одной идее)
- [ ] 1-2 automation rules созданы
- [ ] Команда получила доступ (creators + contributors)

---

## Поддержка

- Документация JPD: https://support.atlassian.com/jira-product-discovery/
- Community: community.atlassian.com (вопросы там обычно отвечают за 1-2 дня)
- При сложностях с миграцией — Atlassian Solution Partner

---

## Что НЕ делать при настройке

❌ Не создавать 20+ custom fields сразу. Начать с минимума, расширять по мере необходимости.
❌ Не вводить сложный workflow. 5-6 статусов = max.
❌ Не подключать Jira/JPD к 10 другим системам в первый день. Сначала научиться работать без интеграций.
❌ Не делать automation rules без понимания лимита 100/мес. Один сложный rule может съесть 50 runs.
❌ Не давать всем creator-доступ в JPD при наличии 3 slots — продумайте, кому реально нужно.
