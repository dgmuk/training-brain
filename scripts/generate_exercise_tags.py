# -*- coding: utf-8 -*-
"""Generate knowledge-base/exercises/exercise-tags.md from exercise-library.md."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "knowledge-base" / "exercises" / "exercise-library.md"
OUT = ROOT / "knowledge-base" / "exercises" / "exercise-tags.md"


def parse_exercises(text: str):
    section = None
    exercises = []
    skip_sections = {
        "🚨 Правила работы с библиотекой",
        "📝 Формат записи",
        "➕ Как добавить новое упражнение",
    }
    for line in text.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            section = m.group(1).strip()
            continue
        m2 = re.match(r"^### (.+)$", line)
        if m2:
            name = m2.group(1).strip()
            if name == "Точное имя упражнения":
                continue
            if section in skip_sections:
                continue
            exercises.append((section, name))
    return exercises


def sec_key(s: str) -> str:
    s = s.lower()
    if "груд" in s:
        return "chest"
    if "спин" in s:
        return "back"
    if "ног" in s or "ягодиц" in s or "квадр" in s:
        return "legs"
    if "икр" in s:
        return "calves"
    if "плеч" in s:
        return "shoulders"
    if "бицепс" in s:
        return "biceps"
    if "трицепс" in s:
        return "triceps"
    if "пресс" in s or "функционал" in s:
        return "core_func"
    if "кардио" in s:
        return "cardio"
    return "other"


def equip(name: str, section: str) -> str:
    n = name.lower()
    tags = []
    if "штан" in n or "ez" in n or "гриф" in n or "т-гриф" in n:
        tags.append("barbell")
    if "гантел" in n:
        tags.append("dumbbell")
    if "гир" in n:
        tags.append("kettlebell")
    if "смит" in n:
        tags.append("smith")
    if "блок" in n or "кроссовер" in n or "канат" in n:
        tags.append("cable")
    if (
        "тренаж" in n
        or "гравитрон" in n
        or "платформ" in n
        or "гакк" in n
        or "бабочка" in n
        or "рычаж" in n
    ):
        tags.append("machine")
    if "trx" in n or "петл" in n:
        tags.append("trx")
    if "резин" in n or "эспандер" in n:
        tags.append("band")
    if (
        "брусь" in n
        or "перекладин" in n
        or "подтягив" in n
        or "отжиман" in n
        or "планка" in n
        or "берпи" in n
    ):
        tags.append("bodyweight")
    if "скамь" in n:
        tags.append("bench")
    if not tags:
        if sec_key(section) == "cardio":
            tags.append("cardio_machine")
        else:
            tags.append("mixed")
    return ",".join(sorted(set(tags)))


def pattern_and_muscles(name: str, section: str) -> dict:
    n = name.lower()
    sk = sec_key(section)
    primary = []
    secondary = []
    pattern = "other"
    joints = []
    sfr = "mid"
    role = "compound"

    if sk == "chest":
        primary = ["chest"]
        secondary = ["triceps:0.5", "front_delt:0.5"]
        pattern = "horizontal_press"
        joints = ["shoulder"]
        if "наклон" in n and "отрицат" not in n:
            pattern = "incline_press"
        if "отрицат" in n:
            pattern = "decline_press"
        if "разведен" in n or "сведен" in n or "бабочка" in n or "пуловер" in n:
            role = "isolation"
            secondary = ["front_delt:0.5"] if "пуловер" not in n else ["lats:0.5"]
            if "пуловер" in n:
                primary = ["chest", "lats"]
                pattern = "pullover"
            else:
                pattern = "fly"
            sfr = "high"
            joints = ["shoulder"]
        elif "брусь" in n:
            pattern = "dip"
            joints = ["shoulder", "elbow"]
            sfr = "mid"
        elif "отжиман" in n:
            pattern = "pushup"
            joints = ["shoulder", "wrist"]
            sfr = "high"
        elif "тренаж" in n or "смит" in n or "рычаж" in n:
            sfr = "high"
            secondary = ["triceps:0.5"]
        else:
            sfr = "mid"
            joints = ["shoulder"]

    elif sk == "back":
        primary = ["lats"]
        secondary = ["biceps:0.5", "rear_delt:0.5", "mid_back:0.5"]
        joints = ["shoulder", "elbow"]
        if "становая" in n:
            primary = ["hamstrings", "glutes"]
            secondary = ["lats:0.5", "erectors:0.5", "traps:0.5"]
            pattern = "hinge"
            joints = ["lumbar", "hip"]
            sfr = "low"
            role = "compound"
        elif "гипер" in n:
            primary = ["erectors"]
            secondary = ["glutes:0.5", "hamstrings:0.5"]
            pattern = "extension"
            joints = ["lumbar"]
            sfr = "high"
            role = "isolation"
        elif "вертикаль" in n or "подтягив" in n or "австралий" in n:
            pattern = "vertical_pull"
            sfr = (
                "high"
                if "тренаж" in n or "блок" in n or "гравитрон" in n
                else "mid"
            )
        elif "face" in n or "приведение локтей" in n:
            primary = ["rear_delt"]
            secondary = ["mid_back:0.5"]
            pattern = "rear_delt"
            role = "isolation"
            sfr = "high"
        elif "пуловер" in n:
            primary = ["lats"]
            secondary = ["chest:0.5"]
            pattern = "pullover"
            role = "isolation"
            sfr = "high"
        else:
            pattern = "horizontal_pull"
            if "горизонтал" in n or "сидя" in n or "рычаж" in n or "блок" in n:
                sfr = "high"
            else:
                sfr = "mid"
                joints = ["shoulder", "lumbar", "elbow"]

    elif sk == "legs":
        joints = ["knee", "hip"]
        if "румын" in n or "ласточк" in n or ("тяга одной" in n and "ног" in n):
            primary = ["hamstrings"]
            secondary = ["glutes:0.5", "erectors:0.5"]
            pattern = "hinge"
            joints = (
                ["lumbar", "hip"]
                if "одной" not in n and "ласточ" not in n
                else ["hip"]
            )
            sfr = "high"
        elif "ягодичн" in n or "мост" in n:
            primary = ["glutes"]
            secondary = ["hamstrings:0.5"]
            pattern = "hip_thrust"
            joints = ["hip"]
            sfr = "high"
            role = "isolation"
        elif "сгибание ног" in n:
            primary = ["hamstrings"]
            secondary = []
            pattern = "leg_curl"
            joints = ["knee"]
            role = "isolation"
            sfr = "high"
        elif "разгибание ног" in n:
            primary = ["quads"]
            secondary = []
            pattern = "leg_extension"
            joints = ["knee"]
            role = "isolation"
            sfr = "high"
        elif "разведение ног" in n:
            primary = ["glutes"]
            secondary = []
            pattern = "abduction"
            joints = ["hip"]
            role = "isolation"
            sfr = "high"
        elif "сведение ног" in n:
            primary = ["adductors"]
            secondary = []
            pattern = "adduction"
            joints = ["hip"]
            role = "isolation"
            sfr = "high"
        elif "разгибание бедра" in n:
            primary = ["glutes"]
            secondary = []
            pattern = "hip_extension"
            joints = ["hip"]
            role = "isolation"
            sfr = "high"
        elif "гипер" in n:
            primary = ["glutes", "erectors"]
            secondary = ["hamstrings:0.5"]
            pattern = "extension"
            joints = ["lumbar", "hip"]
            sfr = "high"
        elif "жим носками" in n or "носок" in n:
            primary = ["calves"]
            secondary = []
            pattern = "calf_raise"
            joints = ["ankle"]
            role = "isolation"
            sfr = "high"
        elif "болгар" in n or "сплит" in n or "выпад" in n or "зашагив" in n:
            primary = ["quads", "glutes"]
            secondary = ["hamstrings:0.5"]
            pattern = "lunge_split"
            joints = ["knee", "hip"]
            sfr = "high"
        elif "жим ног" in n or "платформ" in n:
            primary = ["quads"]
            secondary = ["glutes:0.5"]
            pattern = "leg_press"
            joints = ["knee", "hip"]
            sfr = "high"
        elif "гакк" in n or "фронталь" in n or "гоблет" in n or "присед" in n:
            primary = ["quads"]
            secondary = ["glutes:0.5", "hamstrings:0.5"]
            pattern = "squat"
            joints = (
                ["knee", "hip", "lumbar"]
                if "штан" in n and "смит" not in n and "гоблет" not in n
                else ["knee", "hip"]
            )
            sfr = "mid" if "штан" in n and "смит" not in n else "high"
        else:
            primary = ["quads"]
            secondary = ["glutes:0.5"]
            pattern = "squat"
            joints = ["knee", "hip"]
            sfr = "mid"

    elif sk == "calves":
        primary = ["calves"]
        secondary = []
        pattern = "calf_raise"
        joints = ["ankle"]
        role = "isolation"
        sfr = "high"

    elif sk == "shoulders":
        joints = ["shoulder"]
        if (
            "face" in n
            or "обратн" in n
            or ("наклон" in n and "мах" in n)
            or "махи с гантелями в наклоне" in n
        ):
            primary = ["rear_delt"]
            secondary = ["mid_back:0.5"]
            pattern = "rear_delt"
            role = "isolation"
            sfr = "high"
        elif "в сторон" in n or "отведение" in n or (
            "махи" in n and "наклон" not in n
        ):
            primary = ["side_delt"]
            secondary = []
            pattern = "lateral_raise"
            role = "isolation"
            sfr = "high"
        elif "перед" in n:
            primary = ["front_delt"]
            secondary = []
            pattern = "front_raise"
            role = "isolation"
            sfr = "mid"
        elif "подбород" in n or "протяж" in n or "к груди стоя" in n:
            primary = ["side_delt", "traps"]
            secondary = ["front_delt:0.5"]
            pattern = "upright_row"
            role = "compound"
            sfr = "low"
            joints = ["shoulder"]
        else:
            primary = ["side_delt", "front_delt"]
            secondary = ["triceps:0.5"]
            pattern = "vertical_press"
            role = "compound"
            sfr = "mid" if "штан" in n or "стоя" in n else "high"
            joints = ["shoulder"]

    elif sk == "biceps":
        primary = ["biceps"]
        secondary = []
        pattern = "curl"
        joints = ["elbow"]
        role = "isolation"
        sfr = "high"
        if "кист" in n:
            primary = ["forearms"]
            pattern = "wrist_curl"
            joints = ["wrist"]
        if "молот" in n or "обратн" in n:
            secondary = ["forearms:0.5"]

    elif sk == "triceps":
        primary = ["triceps"]
        secondary = []
        pattern = "extension"
        joints = ["elbow"]
        role = "isolation"
        sfr = "high"
        if "жим" in n and "узк" in n:
            secondary = ["chest:0.5", "front_delt:0.5"]
            pattern = "close_grip_press"
            role = "compound"
            joints = ["elbow", "shoulder"]
            sfr = "mid"
        if "брусь" in n or "отжиман" in n:
            secondary = ["chest:0.5", "front_delt:0.5"]
            pattern = "dip"
            role = "compound"
            joints = ["elbow", "shoulder"]
            sfr = "mid"
        if "из за голов" in n or "из-за голов" in n or "француз" in n:
            pattern = "overhead_extension"
            joints = ["elbow", "shoulder"]
            sfr = "high"

    elif sk == "core_func":
        if (
            "пресс" in n
            or "скручив" in n
            or "планка" in n
            or ("колен" in n and "брусь" in n)
            or "ласты" in n
        ):
            primary = ["abs"]
            secondary = []
            pattern = "core"
            joints = ["lumbar"]
            role = "core"
            sfr = "high"
        elif "отжиман" in n or "жим гантелей лежа" in n:
            primary = ["chest"]
            secondary = ["triceps:0.5", "front_delt:0.5"]
            pattern = "pushup"
            joints = ["shoulder", "wrist"]
            role = "compound"
            sfr = "high"
        elif "присед" in n or "выпад" in n:
            primary = ["quads", "glutes"]
            secondary = ["hamstrings:0.5"]
            pattern = "squat" if "присед" in n else "lunge_split"
            joints = ["knee", "hip"]
            role = "compound"
            sfr = "mid"
        elif (
            "берпи" in n
            or "джампинг" in n
            or "прыж" in n
            or "конькобеж" in n
            or "бег" in n
        ):
            primary = ["full_body"]
            secondary = []
            pattern = "conditioning"
            joints = ["knee", "ankle"]
            role = "cardio"
            sfr = "low"
        elif "махи гир" in n:
            primary = ["hamstrings", "glutes"]
            secondary = ["front_delt:0.5", "erectors:0.5"]
            pattern = "swing"
            joints = ["hip", "lumbar"]
            role = "compound"
            sfr = "mid"
        elif "сгибание ног" in n:
            primary = ["hamstrings"]
            pattern = "leg_curl"
            joints = ["knee"]
            role = "isolation"
            sfr = "high"
        elif "ягодичн" in n:
            primary = ["glutes"]
            pattern = "hip_thrust"
            joints = ["hip"]
            role = "isolation"
            sfr = "high"
        elif "разведен" in n:
            primary = ["rear_delt"]
            pattern = "rear_delt"
            joints = ["shoulder"]
            role = "isolation"
            sfr = "high"
        elif "пуловер" in n:
            primary = ["lats", "chest"]
            pattern = "pullover"
            joints = ["shoulder"]
            role = "isolation"
            sfr = "high"
        elif "трицепс" in n or "разгибание руки" in n or "француз" in n:
            primary = ["triceps"]
            pattern = "extension"
            joints = ["elbow"]
            role = "isolation"
            sfr = "high"
        else:
            primary = ["full_body"]
            pattern = "conditioning"
            joints = []
            role = "compound"
            sfr = "mid"

    elif sk == "cardio":
        primary = ["cardio"]
        secondary = []
        pattern = "cardio"
        joints = []
        role = "cardio"
        sfr = "n/a"
        if "hiit" in n or "интервал" in n:
            joints = ["knee", "ankle"]

    else:
        primary = ["unknown"]
        pattern = "other"
        joints = []
        role = "compound"
        sfr = "mid"

    return {
        "primary": ",".join(primary),
        "secondary": ",".join(secondary) if secondary else "—",
        "pattern": pattern,
        "joints": ",".join(joints) if joints else "—",
        "sfr": sfr,
        "role": role,
        "equip": equip(name, section),
    }


def main():
    text = LIBRARY.read_text(encoding="utf-8")
    exercises = parse_exercises(text)
    rows = []
    for section, name in exercises:
        t = pattern_and_muscles(name, section)
        rows.append((section, name, t))

    lines = [
        "---",
        "Тема: Метаданные и теги упражнений для автоподбора",
        "Раздел: exercises",
        "Связи: [[exercise-library]] [[../methodology/exercise-selection]] [[../volume-landmarks/fractional-sets]] [[../contraindications/index]] [[home-equipment]]",
        "---",
        "",
        "# Теги упражнений (метаданные)",
        "",
        "> [[index]] | [[exercise-library]] | [[../index]]",
        "",
        "Спутник [[exercise-library]]. Имена здесь совпадают с библиотекой посимвольно. При подборе замен, расчёте дробного объёма и фильтрации по суставам читай теги здесь, а видео и канон имени бери из library.",
        "",
        "## Схема тегов",
        "",
        "| Поле | Значения | Назначение |",
        "|------|----------|------------|",
        "| primary | chest, lats, mid_back, quads, hamstrings, glutes, adductors, calves, side_delt, front_delt, rear_delt, biceps, triceps, forearms, abs, erectors, traps, full_body, cardio | Прямая нагрузка (1.0 к дробному объёму) |",
        "| secondary | muscle:0.5 | Косвенный вклад синергиста |",
        "| pattern | squat, hinge, lunge_split, horizontal_press, incline_press, vertical_press, vertical_pull, horizontal_pull, fly, curl, extension, ... | Паттерн движения |",
        "| joints | shoulder, elbow, wrist, lumbar, hip, knee, ankle | Зоны риска для фильтров |",
        "| sfr | high / mid / low / n/a | Stimulus-to-fatigue |",
        "| role | compound / isolation / core / cardio | Роль в сессии |",
        "| equip | barbell, dumbbell, cable, machine, smith, bodyweight, band, kettlebell, trx, bench, cardio_machine | Оборудование |",
        "",
        "## Правила использования при сборке week-N",
        "",
        "1. Имя упражнения только из [[exercise-library]].",
        "2. При боли в суставе исключи упражнения с этим joint в теге, подбери другой pattern с тем же primary.",
        "3. При дефиците восстановления предпочитай `sfr: high` и `role: isolation` / machine.",
        "4. Дробный объём: primary = 1.0, secondary = 0.5 на подход, см. [[../volume-landmarks/fractional-sets]].",
        "5. При добавлении нового упражнения в library добавь строку и сюда (или перезапусти `scripts/generate_exercise_tags.py` и поправь вручную).",
        "",
        "## Формат строки в library (опционально)",
        "",
        "Можно дублировать компактную строку под видео:",
        "",
        "```",
        "Tags: primary=chest | secondary=triceps:0.5,front_delt:0.5 | pattern=horizontal_press | joints=shoulder | sfr=high | role=compound | equip=dumbbell,bench",
        "```",
        "",
        "Полная таблица ниже остаётся источником правды по тегам.",
        "",
    ]

    current = None
    for section, name, t in rows:
        if section != current:
            current = section
            lines.append(f"## {section}")
            lines.append("")
            lines.append(
                "| Упражнение | primary | secondary | pattern | joints | sfr | role | equip |"
            )
            lines.append(
                "|------------|---------|-----------|---------|--------|-----|------|-------|"
            )
        lines.append(
            f"| {name} | {t['primary']} | {t['secondary']} | {t['pattern']} | {t['joints']} | {t['sfr']} | {t['role']} | {t['equip']} |"
        )

    lines.extend(
        [
            "",
            f"*Всего упражнений с тегами: {len(rows)}*",
            "",
            "## Связи",
            "",
            "- [[exercise-library]] — канонические имена и видео",
            "- [[../methodology/exercise-selection]] — алгоритм SFR",
            "- [[../methodology/mobility-screen-intake]] — фильтр по joints после скрининга",
            "- [[../contraindications/index]] — протоколы суставов",
            "",
        ]
    )

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} rows={len(rows)}")


if __name__ == "__main__":
    main()
