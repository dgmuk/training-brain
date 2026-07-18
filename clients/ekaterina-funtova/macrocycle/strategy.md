# Стратегия макроцикла: Фунтова Екатерина

> [[overview]] | [[../profile]] | [[../../../knowledge-base/methodology/comfort-bank-rotation]] | [[../../../knowledge-base/periodization/models]]

---

## Принятые решения и обоснование

### programming_mode: comfort_bank

**Почему:** Клиентка явно не хочет больших весов и сильной нагрузки. Стандартные модели (LP/DUP с пиком RIR 0–1 и ростом тоннажа) конфликтуют с её предпочтениями и убьют adherence.

**Следствие:**  
- KPI = посещаемость + комфорт + ощущение новизны  
- Не KPI = 1RM, MRV, отказные подходы  
- `progression-rules` (standard) **перекрыты** [[../../../knowledge-base/methodology/comfort-bank-rotation]]

### Сплит: 3× mixed Full Body (из банка)

**Почему:** Уже есть 4 рабочие недели × 3 дня с подобранными весами. Ломать на PPL/UL бессмысленно: банк = доказанный комфортный формат.

**Структура микроцикла (любая неделя банка):**
- День 1: mixed (часто hinge/ноги + upper)
- День 2: mixed (часто ягодицы/ноги + pull/push)
- День 3: mixed (часто hinge/split + upper/accessory)

Точные упражнения зависят от template W1–W4 (см. mesocycle overview).

### Модель «периодизации»: ротация банка, не пик интенсивности

| Классика | У Екатерины |
|----------|-------------|
| Нед 1–4: RIR 3→1, объём ↑ | RIR **плоско 3–4** |
| Нед 5: делоад | Делоад **по самочувствию**, не по календарю |
| Прогрессия весом | Hold + новизна template |
| Isolation A/B | Week bank W1–W4 |

### Длина макроцикла: открытый 6+ месяцев

Нет дедлайна «выйти на пик к дате».  
Мезо = **4 continuous weeks** (полный проход банка), затем следующий мезо с тем же банком или перетасовкой порядка.

### Стартовая точка

- Мезо 1: 4 уже существующие недели (история + банк)  
- Мезо 2 нед 5: повтор W1 hold, выдача в GitHub/приложение  
- Калибровка 0/0/0 **не нужна**: веса известны

### Приоритет стимула (мягкий)

1. **Ягодицы / ноги** (часто в банке)  
2. **Задняя цепь (hinge)**  
3. **Тяги спины**  
4. **Жимы / руки** (поддерживающий объём)

Без specialization-phase и без weak-point playbook «на максимум», пока цель comfort.

---

## Как ИИ выбирает решения (кратко)

```
IF programming_mode != comfort_bank → STOP (не тот клиент)
ELSE:
  pick template W* by continuous week calendar
  copy exercises from bank file
  apply hold/ease table from profile
  NEVER plan RIR < 2
  NEVER force +weight every week
  write week-N in standard parser format
  report signals + adherence to trainer
```

---

## Ключевые риски и митигация

| Риск | Митигация |
|------|-----------|
| Модель применит standard progression | Явный `programming_mode` в profile + frontmatter каждой недели |
| Скука от «одних весов» | Ротация W1–W4, перетасовка порядка, точечный микс 1–2 упражнений |
| Клиентка просит легче | Ease −10–15%, не спорить «наукой» |
| Боль сустава | Замена из library/банка, hold/ease |
| Пропуски | adherence-protocols; без удвоения объёма |
| Путаница client_id | Только `ekaterina-funtova`, не кириллица |

---

## Связанные документы

| Документ | Зачем |
|----------|-------|
| [[../profile]] | Полный операционный контракт для ИИ |
| [[../questionnaire-raw]] | Сырые вводные тренера |
| [[../mesocycle-1/overview]] | Банк W1–W4 |
| [[../mesocycle-2/overview]] | Текущая ротация, нед 5+ |
| [[../../../knowledge-base/methodology/comfort-bank-rotation]] | Методика |
| [[../../../CLAUDE.md]] | Схема Б, формат week-N, правила 1–6 |
