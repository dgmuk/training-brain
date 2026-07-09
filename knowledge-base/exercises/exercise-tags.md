---
Тема: Метаданные и теги упражнений для автоподбора
Раздел: exercises
Связи: [[exercise-library]] [[../methodology/exercise-selection]] [[../volume-landmarks/fractional-sets]] [[../contraindications/index]] [[home-equipment]]
---

# Теги упражнений (метаданные)

> [[index]] | [[exercise-library]] | [[../index]]

Спутник [[exercise-library]]. Имена здесь совпадают с библиотекой посимвольно. При подборе замен, расчёте дробного объёма и фильтрации по суставам читай теги здесь, а видео и канон имени бери из library.

## Схема тегов

| Поле | Значения | Назначение |
|------|----------|------------|
| primary | chest, lats, mid_back, quads, hamstrings, glutes, adductors, calves, side_delt, front_delt, rear_delt, biceps, triceps, forearms, abs, erectors, traps, full_body, cardio | Прямая нагрузка (1.0 к дробному объёму) |
| secondary | muscle:0.5 | Косвенный вклад синергиста |
| pattern | squat, hinge, lunge_split, horizontal_press, incline_press, vertical_press, vertical_pull, horizontal_pull, fly, curl, extension, ... | Паттерн движения |
| joints | shoulder, elbow, wrist, lumbar, hip, knee, ankle | Зоны риска для фильтров |
| sfr | high / mid / low / n/a | Stimulus-to-fatigue |
| role | compound / isolation / core / cardio | Роль в сессии |
| equip | barbell, dumbbell, cable, machine, smith, bodyweight, band, kettlebell, trx, bench, cardio_machine | Оборудование |

## Правила использования при сборке week-N

1. Имя упражнения только из [[exercise-library]].
2. При боли в суставе исключи упражнения с этим joint в теге, подбери другой pattern с тем же primary.
3. При дефиците восстановления предпочитай `sfr: high` и `role: isolation` / machine.
4. Дробный объём: primary = 1.0, secondary = 0.5 на подход, см. [[../volume-landmarks/fractional-sets]].
5. При добавлении нового упражнения в library добавь строку и сюда (или перезапусти `scripts/generate_exercise_tags.py` и поправь вручную).

## Формат строки в library (опционально)

Можно дублировать компактную строку под видео:

```
Tags: primary=chest | secondary=triceps:0.5,front_delt:0.5 | pattern=horizontal_press | joints=shoulder | sfr=high | role=compound | equip=dumbbell,bench
```

Полная таблица ниже остаётся источником правды по тегам.

## 🛡️ Грудные

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Жим в тренажере узким нейтральным хватом | chest | triceps:0.5 | horizontal_press | shoulder | high | compound | machine |
| Жим штанги лежа в тренажере Смита | chest | triceps:0.5 | horizontal_press | shoulder | high | compound | barbell,machine,smith |
| Жим штанги в тренажере Смита на наклонной скамье | chest | triceps:0.5 | incline_press | shoulder | high | compound | barbell,bench,machine,smith |
| Жим от груди в рычажном тренажере сидя | chest | triceps:0.5 | horizontal_press | shoulder | high | compound | machine |
| Жим гантелей лежа на горизонтальной скамье | chest | triceps:0.5,front_delt:0.5 | horizontal_press | shoulder | mid | compound | bench,dumbbell |
| Жим гантелей лежа на наклонной скамье | chest | triceps:0.5,front_delt:0.5 | incline_press | shoulder | mid | compound | bench,dumbbell |
| Жим штанги на скамье с отрицательным наклоном | chest | triceps:0.5,front_delt:0.5 | decline_press | shoulder | mid | compound | barbell,bench |
| Жим сидя в блочном тренажере на грудь | chest | triceps:0.5 | horizontal_press | shoulder | high | compound | machine |
| Жим в кроссовере стоя от среднего блока | chest | triceps:0.5,front_delt:0.5 | horizontal_press | shoulder | mid | compound | cable |
| Жим штанги лежа на горизонтальной скамье | chest | triceps:0.5,front_delt:0.5 | horizontal_press | shoulder | mid | compound | barbell,bench |
| Жим штанги лежа на наклонной скамье | chest | triceps:0.5,front_delt:0.5 | incline_press | shoulder | mid | compound | barbell,bench |
| Отжимания от перекладины | chest | triceps:0.5,front_delt:0.5 | pushup | shoulder,wrist | high | compound | bodyweight |
| Отжимания в подвесных петлях TRX | chest | triceps:0.5,front_delt:0.5 | pushup | shoulder,wrist | high | compound | bodyweight,trx |
| Отжимания на брусьях с акцентом на грудные | chest | triceps:0.5,front_delt:0.5 | dip | shoulder,elbow | mid | compound | bodyweight |
| Отжимания на брусьях в гравитроне | chest | triceps:0.5,front_delt:0.5 | dip | shoulder,elbow | mid | compound | bodyweight,machine |
| Отжимания от пола на рукоятках | chest | triceps:0.5,front_delt:0.5 | pushup | shoulder,wrist | high | compound | bodyweight |
| Отжимания в тренажере сидя | chest | triceps:0.5,front_delt:0.5 | pushup | shoulder,wrist | high | compound | bodyweight,machine |
| Пуловер с верхнего блока лежа на скамье | chest,lats | lats:0.5 | pullover | shoulder | high | isolation | bench,cable |
| Разведение рук с гантелями лёжа | chest | front_delt:0.5 | fly | shoulder | high | isolation | dumbbell |
| Разведение рук с гантелями лежа 30-45 гр | chest | front_delt:0.5 | fly | shoulder | high | isolation | dumbbell |
| Сведение рук в кроссовере лежа на скамье | chest | front_delt:0.5 | fly | shoulder | high | isolation | bench,cable |
| Сведение рук в кроссовере с верхних блоков | chest | front_delt:0.5 | fly | shoulder | high | isolation | cable |
| Сведение рук в кроссовере с нижних блоков | chest | front_delt:0.5 | fly | shoulder | high | isolation | cable |
| Сведение рук в кроссовере сидя на скамье | chest | front_delt:0.5 | fly | shoulder | high | isolation | bench,cable |
| Сведение рук в кроссовере стоя (со средних блоков) | chest | front_delt:0.5 | fly | shoulder | high | isolation | cable |
| Сведение рук в тренажере «Бабочка» (Pec-Deck) | chest | front_delt:0.5 | fly | shoulder | high | isolation | machine |
## 🛶 Спина

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Австралийские подтягивания | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | mid | compound | bodyweight |
| Вертикальная тяга одной рукой в тренажере | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | high | compound | machine |
| Вертикальная тяга за голову широким хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | mid | compound | mixed |
| Вертикальная тяга к груди обратным хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | mid | compound | mixed |
| Вертикальная тяга блока параллельным хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | high | compound | cable |
| Вертикальная тяга блока узким хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | high | compound | cable |
| Вертикальная тяга широким нейтральным хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | mid | compound | mixed |
| Вертикальная тяга к груди средним хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | mid | compound | mixed |
| Вертикальная тяга в рычажном тренажере | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | high | compound | machine |
| Вертикальная тяга средним прямым хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | mid | compound | mixed |
| Высокая тяга стоя | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | mixed |
| Высокая тяга сидя | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | mixed |
| Гиперэкстензия под углом 45 градусов | erectors | glutes:0.5,hamstrings:0.5 | extension | lumbar | high | isolation | mixed |
| Горизонтальная гиперэкстензия | erectors | glutes:0.5,hamstrings:0.5 | extension | lumbar | high | isolation | mixed |
| Горизонтальная тяга к поясу обратным хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | mixed |
| Горизонтальная тяга нейтральным хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | mixed |
| Горизонтальная тяга блока широким хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | cable |
| Горизонтальная тяга в тренажере сидя | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | machine |
| Горизонтальная тяга в рычажном тренажере сидя | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | machine |
| Горизонтальная тяга в рычажном нейтральный хват | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | machine |
| Горизонтальная тяга одной рукой в тренажере | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | machine |
| Горизонтальная тяга к поясу узким хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | mixed |
| Подтягивания в гравитроне нейтральным хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | high | compound | bodyweight,machine |
| Подтягивания в гравитроне прямым хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | high | compound | bodyweight,machine |
| Подтягивания на перекладине обратным хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | vertical_pull | shoulder,elbow | mid | compound | bodyweight |
| Приведение локтей с верхнего блока | rear_delt | mid_back:0.5 | rear_delt | shoulder,elbow | high | isolation | cable |
| Пуловер в блочном тренажере стоя | lats | chest:0.5 | pullover | shoulder,elbow | high | isolation | machine |
| Становая тяга с гантелями | hamstrings,glutes | lats:0.5,erectors:0.5,traps:0.5 | hinge | lumbar,hip | low | compound | dumbbell |
| Становая тяга со штангой с пола | hamstrings,glutes | lats:0.5,erectors:0.5,traps:0.5 | hinge | lumbar,hip | low | compound | barbell |
| Тяга гантели в наклоне | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | dumbbell |
| Тяга гантелей в наклоне с упором в скамью | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | bench,dumbbell |
| Тяга гантелей стоя в наклоне | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | dumbbell |
| Тяга нижнего блока одной рукой | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,elbow | high | compound | cable |
| Тяга Т-грифа узким хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | barbell |
| Тяга Т-грифа широким хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | barbell |
| Тяга штанги в наклоне обратным хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | barbell |
| Тяга штанги в наклоне | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | barbell |
| Тяга штанги в наклоне широким хватом | lats | biceps:0.5,rear_delt:0.5,mid_back:0.5 | horizontal_pull | shoulder,lumbar,elbow | mid | compound | barbell |
## 🦵 Ноги (квадрицепсы, ягодицы, бицепс бедра, задняя цепь)

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Выпады вперед со штангой на плечах | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | barbell |
| Обратные выпады с гирей | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | kettlebell |
| Обратные выпады со штангой на плечах | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | barbell |
| Гоблет-приседания | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | mixed |
| Жим платформы одной ногой | quads | glutes:0.5 | leg_press | knee,hip | high | compound | machine |
| Жим ногами в тренажере | quads | glutes:0.5 | leg_press | knee,hip | high | compound | machine |
| Зашагивание на тумбу с гантелью | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | dumbbell |
| Поочередное зашагивание на тумбу | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Тяга одной ногой с гантелью Ласточка | hamstrings | glutes:0.5,erectors:0.5 | hinge | hip | high | compound | dumbbell |
| Тяга одной ногой с гантелями Ласточка | hamstrings | glutes:0.5,erectors:0.5 | hinge | hip | high | compound | dumbbell |
| Румынская тяга с гантелями | hamstrings | glutes:0.5,erectors:0.5 | hinge | lumbar,hip | high | compound | dumbbell |
| Румынская тяга со штангой | hamstrings | glutes:0.5,erectors:0.5 | hinge | lumbar,hip | high | compound | barbell |
| Румынская тяга на одной ноге | hamstrings | glutes:0.5,erectors:0.5 | hinge | hip | high | compound | mixed |
| Гакк-приседания в тренажере | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | machine |
| Приседания со штангой | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip,lumbar | mid | compound | barbell |
| Приседания в тренажере Смита | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | machine,smith |
| Приседания с фитнес-резинкой | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | band |
| Приседания с гирей (приседания-плие) | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | kettlebell |
| Разведение ног в тренажере сидя | glutes | — | abduction | hip | high | isolation | machine |
| Разгибание бедра в тренажере стоя | glutes | — | hip_extension | hip | high | isolation | machine |
| Разгибание ног сидя в тренажере | quads | — | leg_extension | knee | high | isolation | machine |
| Сведение ног в тренажере сидя | adductors | — | adduction | hip | high | isolation | machine |
| Сгибание ног в тренажере лежа | hamstrings | — | leg_curl | knee | high | isolation | machine |
| Сгибание ног сидя | hamstrings | — | leg_curl | knee | high | isolation | mixed |
| Болгарские сплит приседания | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Сплит приседания в тренажере Смита | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | machine,smith |
| Сплит приседания с одной гантелью | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | dumbbell |
| Сплит-приседания с гантелями | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | dumbbell |
| Сплит приседания со штангой на плечах | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | barbell |
| Фронтальные приседания в блоке | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | cable |
| Фронтальные приседания с гирями | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | kettlebell |
| Фронтальные приседания со штангой | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip,lumbar | mid | compound | barbell |
| Ягодичный мост в тренажере | glutes | hamstrings:0.5 | hip_thrust | hip | high | isolation | machine |
| Ягодичный мост на одной ноге | glutes | hamstrings:0.5 | hip_thrust | hip | high | isolation | mixed |
| Ягодичный мост на полу | glutes | hamstrings:0.5 | hip_thrust | hip | high | isolation | mixed |
| Ягодичный мост со штангой | glutes | hamstrings:0.5 | hip_thrust | hip | high | isolation | barbell |
| Обратные выпады с платформы | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | machine |
| Жим носками в блочном тренажере | calves | — | calf_raise | ankle | high | isolation | machine |
| Обратная гиперэкстензия на скамье | glutes,erectors | hamstrings:0.5 | extension | lumbar,hip | high | compound | bench |
| Румынская тяга в блоке | hamstrings | glutes:0.5,erectors:0.5 | hinge | lumbar,hip | high | compound | cable |
| Разгибание бедра в кроссовере | glutes | — | hip_extension | hip | high | isolation | cable |
## 🦵 Икры

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Жим носками в тренажере | calves | — | calf_raise | ankle | high | isolation | machine |
| Подъемы на носки стоя в тренажере | calves | — | calf_raise | ankle | high | isolation | machine |
| Подъемы на носки сидя в тренажере | calves | — | calf_raise | ankle | high | isolation | machine |
| Жим носками в блочном тренажере | calves | — | calf_raise | ankle | high | isolation | machine |
| Подъемы на носки на одной ноге | calves | — | calf_raise | ankle | high | isolation | mixed |
## 🏋️ Плечи

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Жим Арнольда | side_delt,front_delt | triceps:0.5 | vertical_press | shoulder | high | compound | mixed |
| Вертикальный жим в тренажере | side_delt,front_delt | triceps:0.5 | vertical_press | shoulder | high | compound | machine |
| Жим гантелей сидя | side_delt,front_delt | triceps:0.5 | vertical_press | shoulder | high | compound | dumbbell |
| Жим гантелей стоя | side_delt,front_delt | triceps:0.5 | vertical_press | shoulder | mid | compound | dumbbell |
| Жим гантелей сидя нейтральный хват | side_delt,front_delt | triceps:0.5 | vertical_press | shoulder | high | compound | dumbbell |
| Жим штанги стоя | side_delt,front_delt | triceps:0.5 | vertical_press | shoulder | mid | compound | barbell |
| Жим в тренажере Смита сидя | side_delt,front_delt | triceps:0.5 | vertical_press | shoulder | high | compound | machine,smith |
| Отведение руки в кроссовере | side_delt | — | lateral_raise | shoulder | high | isolation | cable |
| Отведение руки с гантелью с наклоном | side_delt | — | lateral_raise | shoulder | high | isolation | dumbbell |
| Подъем рук перед собой с канатом | front_delt | — | front_raise | shoulder | mid | isolation | cable |
| Подъем рук перед собой с рукоятью | front_delt | — | front_raise | shoulder | mid | isolation | mixed |
| Махи с гантелями в наклоне | rear_delt | mid_back:0.5 | rear_delt | shoulder | high | isolation | dumbbell |
| Поочередный подъем гантелей перед собой | front_delt | — | front_raise | shoulder | mid | isolation | dumbbell |
| Махи с гантелями сидя | side_delt | — | lateral_raise | shoulder | high | isolation | dumbbell |
| Махи гантелей в стороны стоя | side_delt | — | lateral_raise | shoulder | high | isolation | dumbbell |
| Тяга к подбородку из нижнего блока | side_delt,traps | front_delt:0.5 | upright_row | shoulder | low | compound | cable |
| Тяга к подбородку в тренажере Смита | side_delt,traps | front_delt:0.5 | upright_row | shoulder | low | compound | machine,smith |
| Тяга EZ грифа к груди стоя протяжка | side_delt,traps | front_delt:0.5 | upright_row | shoulder | low | compound | barbell |
| Тяга штанги к подбородку стоя (протяжка) | side_delt,traps | front_delt:0.5 | upright_row | shoulder | low | compound | barbell |
| Face Pulls | rear_delt | mid_back:0.5 | rear_delt | shoulder | high | isolation | mixed |
| Обратные разведения в тренажере «Бабочка» | rear_delt | mid_back:0.5 | rear_delt | shoulder | high | isolation | machine |
## 💪 Бицепс

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Сгибание руки с гантелью на скамье Скотта | biceps | — | curl | elbow | high | isolation | bench,dumbbell |
| Концентрированное сгибание руки с гантелью сидя | biceps | — | curl | elbow | high | isolation | dumbbell |
| Сгибание рук на бицепс в рычажном тренажере сидя | biceps | — | curl | elbow | high | isolation | machine |
| Сгибание кистей с гантелями | forearms | — | wrist_curl | wrist | high | isolation | dumbbell |
| Сгибание кистей со штангой | forearms | — | wrist_curl | wrist | high | isolation | barbell |
| Сгибание рук с EZ грифом обратным хватом | biceps | forearms:0.5 | curl | elbow | high | isolation | barbell |
| Сгибание рук с EZ грифом широким хватом | biceps | — | curl | elbow | high | isolation | barbell |
| Сгибание рук с EZ грифом узким хватом | biceps | — | curl | elbow | high | isolation | barbell |
| Сгибание рук с верхнего блока с канатной рукоятью | biceps | — | curl | elbow | high | isolation | cable |
| Подъем штанги (грифа) на бицепс стоя | biceps | — | curl | elbow | high | isolation | barbell |
| Сгибание рук на нижнем блоке с W образной рукоятью | biceps | — | curl | elbow | high | isolation | cable |
| Сгибание рук на скамье Скотта в нижнем блоке | biceps | — | curl | elbow | high | isolation | bench,cable |
| Сгибание рук на нижнем блоке с канатной рукоятью | biceps | — | curl | elbow | high | isolation | cable |
| Сгибание рук со штангой стоя | biceps | — | curl | elbow | high | isolation | barbell |
| Сгибание рук с эспандером | biceps | — | curl | elbow | high | isolation | band |
| Сгибание руки на нижнем блоке | biceps | — | curl | elbow | high | isolation | cable |
| Сгибание руки на нижнем блоке в наклоне | biceps | — | curl | elbow | high | isolation | cable |
| Сгибание рук со штангой EZ грифом на скамье | biceps | — | curl | elbow | high | isolation | barbell,bench |
| Одновременное сгибание рук с гантелями стоя | biceps | — | curl | elbow | high | isolation | dumbbell |
| Сгибание рук с гантелями сидя хватом «Молот» | biceps | forearms:0.5 | curl | elbow | high | isolation | dumbbell |
| Одновременное сгибание рук с гантелями сидя | biceps | — | curl | elbow | high | isolation | dumbbell |
| Попеременное сгибание рук с гантелями сидя | biceps | — | curl | elbow | high | isolation | dumbbell |
| Одновременное сгибание рук стоя хватом Молот | biceps | forearms:0.5 | curl | elbow | high | isolation | mixed |
| Одновременное сгибание рук с гантелями стоя с супинацией | biceps | — | curl | elbow | high | isolation | dumbbell |
| Сгибание рук попеременно с гантелями стоя с супинацией | biceps | — | curl | elbow | high | isolation | dumbbell |
| Сгибание рук на верхних блоках | biceps | — | curl | elbow | high | isolation | cable |
## 💪 Трицепс

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Жим штанги узким хватом | triceps | chest:0.5,front_delt:0.5 | close_grip_press | elbow,shoulder | mid | compound | barbell |
| Отжимания от скамьи | triceps | chest:0.5,front_delt:0.5 | dip | elbow,shoulder | mid | compound | bench,bodyweight |
| Отжимания в гравитроне | triceps | chest:0.5,front_delt:0.5 | dip | elbow,shoulder | mid | compound | bodyweight,machine |
| Отжимания на брусьях на трицепс | triceps | chest:0.5,front_delt:0.5 | dip | elbow,shoulder | mid | compound | bodyweight |
| Узкие отжимания на рукоятках | triceps | chest:0.5,front_delt:0.5 | dip | elbow,shoulder | mid | compound | bodyweight |
| Разгибание руки на блоке в наклоне кикбэк | triceps | — | extension | elbow | high | isolation | cable |
| Разгибание руки обратным хватом | triceps | — | extension | elbow | high | isolation | mixed |
| Разгибание рук на верхнем блоке | triceps | — | extension | elbow | high | isolation | cable |
| Разгибание рук на верхнем блоке с W-рукоятью | triceps | — | extension | elbow | high | isolation | cable |
| Разгибание рук на верхнем блоке в наклоне | triceps | — | extension | elbow | high | isolation | cable |
| Разгибание рук на верхнем блоке обратным хватом | triceps | — | extension | elbow | high | isolation | cable |
| Разгибание рук на верхнем блоке с канатом | triceps | — | extension | elbow | high | isolation | cable |
| Разгибание рук с гантелью из за головы сидя | triceps | — | overhead_extension | elbow,shoulder | high | isolation | dumbbell |
| Разгибание рук на блоке лежа | triceps | — | extension | elbow | high | isolation | cable |
| Разгибание руки с гантелью в наклоне Кикбэк | triceps | — | extension | elbow | high | isolation | dumbbell |
| Разгибание одной руки с гантелью из за головы | triceps | — | overhead_extension | elbow,shoulder | high | isolation | dumbbell |
| Французский жим с гантелями лежа | triceps | — | overhead_extension | elbow,shoulder | high | isolation | dumbbell |
| Французский жим лежа с EZ грифом | triceps | — | overhead_extension | elbow,shoulder | high | isolation | barbell |
## 🧱 Пресс, многосуставные / функциональные

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Алмазные отжимания | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Берпи | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Отжимания «Лучник» | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Выпады в сторону | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Прямой выпад с ударом коленом | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Выпады в прыжке | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Выпады в прыжке + присед с прыжком | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Обратный выпад с махом ногой вперед | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Гоблет приседания + французский жим с гирей | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | kettlebell |
| Джампинг Джек | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Жим гантелей лежа на полу | quads | glutes:0.5 | squat | knee,hip | mid | compound | dumbbell |
| Разгибание руки с гантелью в наклоне | quads | glutes:0.5 | squat | knee,hip | mid | compound | dumbbell |
| Конькобежец | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Краб + отжимания | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Ласты | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Лечь встать | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Махи гирей перед собой | quads | glutes:0.5 | squat | knee,hip | mid | compound | kettlebell |
| Мега выпады | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Классические отжимания от пола | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Отжимания с колен с прогибом | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Отжимания Кобра с касанием плеча | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Шагающие отжимания | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Перебросы гири | quads | glutes:0.5 | squat | knee,hip | mid | compound | kettlebell |
| Перебросы мяча сидя | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Перекрестные махи ногами стоя | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Перехваты гантели лежа | quads | glutes:0.5 | squat | knee,hip | mid | compound | dumbbell |
| Планка на локтях | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Поочередные выпады вперед | quads,glutes | hamstrings:0.5 | lunge_split | knee,hip | high | compound | mixed |
| Скручивания на пресс в тренажере сидя | quads | glutes:0.5 | squat | knee,hip | mid | compound | machine |
| Приседания | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | mixed |
| Проходка на руках с отжиманием | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Проходка на руках с переходом в планку | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Бег на месте с касанием колен | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Прыжки из приседа, выпрыгивания | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | mixed |
| Приседания с касанием пола и выпрыгиванием | quads | glutes:0.5,hamstrings:0.5 | squat | knee,hip | high | compound | mixed |
| Пуловер с гантелью лежа на полу | quads | glutes:0.5 | squat | knee,hip | mid | compound | dumbbell |
| Разведение гантелей стоя в наклоне | quads | glutes:0.5 | squat | knee,hip | mid | compound | dumbbell |
| Сгибание ног с гантелью лежа | hamstrings | — | leg_curl | knee | high | isolation | dumbbell |
| Подъем коленей в упоре на брусьях | quads | glutes:0.5 | squat | knee,hip | mid | compound | bodyweight |
| Смена позиции | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Ягодичный мост на одной ноге | glutes | hamstrings:0.5 | hip_thrust | hip | high | isolation | mixed |
| Скручивания на полусфере Bosu | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
| Обратные скручивания | quads | glutes:0.5 | squat | knee,hip | mid | compound | mixed |
## 🏃 Кардио

| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |
|------------|---------|-----------|---------|--------|-----|------|-------|
| Ходьба | cardio | — | cardio | — | n/a | cardio | cardio_machine |
| Велотренажёр | cardio | — | cardio | — | n/a | cardio | machine |
| Эллипс | cardio | — | cardio | — | n/a | cardio | cardio_machine |
| Гребной тренажёр | cardio | — | cardio | — | n/a | cardio | machine |
| Беговая дорожка интервалы (HIIT) | cardio | — | cardio | knee,ankle | n/a | cardio | cardio_machine |

*Всего упражнений с тегами: 223*

## Связи

- [[exercise-library]] — канонические имена и видео
- [[../methodology/exercise-selection]] — алгоритм SFR
- [[../methodology/mobility-screen-intake]] — фильтр по joints после скрининга
- [[../contraindications/index]] — протоколы суставов
