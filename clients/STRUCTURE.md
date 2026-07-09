# Стандарт структуры папки клиента

> [[index]] | [[../CLAUDE]] | [[../templates/client-readme]]

Единый канон для **новых** клиентов и для миграции старых. Приложение и Схема Б ожидают непрерывный `week` во frontmatter и файлы `week-N.md` рядом с `overview.md` мезоцикла.

---

## Канон (обязательно для новых)

```
clients/<client_id>/
├── README.md
├── questionnaire-raw.md
├── profile.md
├── macrocycle/
│   ├── overview.md
│   ├── strategy.md
│   └── progress-log.md          ← опционально, но желательно
├── mesocycle-1/
│   ├── overview.md              ← план + ротация A/B + статусы недель
│   ├── week-1.md
│   ├── week-1-filled.md         ← опционально, дневник с фактом
│   ├── week-2.md
│   └── ...
└── mesocycle-2/
    ├── overview.md
    ├── week-6.md                ← непрерывная нумерация!
    └── ...
```

### Правила

1. **`client_id`** только латиница, совпадает с именем папки и frontmatter.
2. **Нумерация недель непрерывная** на весь макроцикл (`week: 6` в mesocycle-2, не `week: 1`).
3. **Имя файла** = `week-<N>.md` где N = поле `week` во frontmatter.
4. **Не** класть недели в `program/` или `неделя-N/`.
5. В `mesocycle-N/overview.md` обязателен блок ротации изоляции A/B (или явный режим `off`/`fixed`).
6. В `profile.md` желателен блок скрининга паттернов после [[../knowledge-base/methodology/mobility-screen-intake]].
7. Запись в [[index]] сразу после создания клиента.

---

## Устаревшие раскладки (не создавать заново)

| Было | Проблема | Куда мигрировать |
|------|----------|------------------|
| `mesocycle-1/program/week-N.md` | Лишний уровень, путаница путей | `mesocycle-1/week-N.md` |
| `неделя-N/week-N.md` + кириллица в пути | Ломает client_id и парсер | `clients/<slug>/mesocycle-N/week-N.md` |
| `week: 1` во втором мезо | Коллизия в приложении | Непрерывный номер |
| Клиент без строки в index | «Не существует» для Схемы Б | Добавить в [[index]] |

### Как мигрировать (вручную, с проверкой)

1. Создать/проверить `client_id` в [[index]].
2. Перенести `week-*.md` в `mesocycle-N/` без `program/`.
3. Проверить frontmatter: `client_id`, `mesocycle`, `week`, даты, `type`.
4. Обновить ссылки в `overview.md` и `README.md`.
5. Запустить `python scripts/validate-exercises.py`.

Не удалять filled-дневники: переименовать/перенести рядом как `week-N-filled.md`.

---

## Минимальный checklist нового клиента

- [ ] Папка `clients/<client_id>/` по канону выше  
- [ ] Строка в [[index]]  
- [ ] `profile.md` с MRV + ограничения + скрининг  
- [ ] `macrocycle/overview.md` + `strategy.md`  
- [ ] `mesocycle-1/overview.md` с A/B  
- [ ] `week-1.md` с YAML  
- [ ] Имена упражнений из library  

---

## Связи

- [[../CLAUDE]] — Схемы А/Б, непрерывная нумерация  
- [[../knowledge-base/methodology/intake-workflow]]  
- [[../templates/README]]  
