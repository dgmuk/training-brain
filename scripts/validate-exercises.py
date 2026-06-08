#!/usr/bin/env python3
"""
Валидатор упражнений для training-brain

Проверяет все week-N.md файлы на соответствие библиотеке упражнений.
Находит упражнения с названиями, которые не совпадают с exercise-library.md

Использование:
    python scripts/validate-exercises.py
    python scripts/validate-exercises.py --fix  # автоматическое исправление (будет в будущем)
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass


@dataclass
class Exercise:
    """Упражнение из библиотеки"""
    name: str
    video_url: str
    section: str  # Группа мышц


@dataclass
class Issue:
    """Проблема найденная в файле"""
    file: Path
    line_number: int
    exercise_found: str
    suggestion: str
    issue_type: str  # 'name_mismatch', 'not_in_library', 'video_mismatch'


class ExerciseValidator:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.library_path = root_dir / "knowledge-base" / "exercises" / "exercise-library.md"
        self.exercises: Dict[str, Exercise] = {}
        self.exercise_names: Set[str] = set()
        self.issues: List[Issue] = []
        
    def load_library(self) -> bool:
        """Загружает библиотеку упражнений"""
        if not self.library_path.exists():
            print(f"❌ Библиотека не найдена: {self.library_path}")
            return False
            
        content = self.library_path.read_text(encoding='utf-8')
        current_section = ""
        current_exercise = None
        current_video = ""
        
        for line in content.split('\n'):
            # Определяем секцию (группу мышц)
            if line.startswith('## '):
                current_section = line.replace('##', '').strip()
                continue
                
            # Название упражнения (заголовок 3-го уровня)
            if line.startswith('### '):
                # Сохраняем предыдущее упражнение если было
                if current_exercise:
                    self.exercises[current_exercise.lower()] = Exercise(
                        name=current_exercise,
                        video_url=current_video,
                        section=current_section
                    )
                    self.exercise_names.add(current_exercise)
                
                current_exercise = line.replace('###', '').strip()
                current_video = ""
                continue
            
            # Ссылка на видео
            video_match = re.match(r'\[Видео\]\((.*?)\)', line)
            if video_match and current_exercise:
                current_video = video_match.group(1)
        
        # Последнее упражнение
        if current_exercise:
            self.exercises[current_exercise.lower()] = Exercise(
                name=current_exercise,
                video_url=current_video,
                section=current_section
            )
            self.exercise_names.add(current_exercise)
        
        print(f"✅ Загружено упражнений: {len(self.exercises)}")
        return True
    
    def find_similar(self, name: str, threshold: int = 3) -> List[str]:
        """Находит похожие названия упражнений (простое сравнение)"""
        name_lower = name.lower()
        similar = []
        
        for ex_name in self.exercise_names:
            ex_lower = ex_name.lower()
            # Простая эвристика: если одно содержится в другом
            if name_lower in ex_lower or ex_lower in name_lower:
                similar.append(ex_name)
        
        return similar[:5]  # Максимум 5 предложений
    
    def validate_file(self, file_path: Path):
        """Проверяет один файл week-N.md"""
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        in_exercise_block = False
        current_exercise = None
        exercise_line_number = 0
        
        for i, line in enumerate(lines, 1):
            # Находим упражнение (заголовок 3-го уровня)
            if line.startswith('### '):
                exercise_name = line.replace('###', '').strip()
                
                # Убираем ссылку на видео если она в заголовке (старый формат)
                exercise_name = re.sub(r'\[Видео\].*', '', exercise_name).strip()
                
                # Пропускаем служебные заголовки
                if exercise_name.startswith('📊') or 'Статистика' in exercise_name:
                    in_exercise_block = False
                    continue
                
                in_exercise_block = True
                current_exercise = exercise_name
                exercise_line_number = i
                
                # Проверяем есть ли в библиотеке
                if current_exercise.lower() not in self.exercises:
                    similar = self.find_similar(current_exercise)
                    suggestion = similar[0] if similar else "Упражнение не найдено в библиотеке"
                    
                    self.issues.append(Issue(
                        file=file_path,
                        line_number=exercise_line_number,
                        exercise_found=current_exercise,
                        suggestion=suggestion,
                        issue_type='not_in_library' if not similar else 'name_mismatch'
                    ))
    
    def validate_all_weeks(self):
        """Проверяет все файлы week-N.md в проекте"""
        clients_dir = self.root_dir / "clients"
        
        if not clients_dir.exists():
            print(f"❌ Папка clients не найдена: {clients_dir}")
            return
        
        week_files = list(clients_dir.rglob("week-*.md"))
        print(f"🔍 Найдено файлов для проверки: {len(week_files)}")
        
        for week_file in week_files:
            self.validate_file(week_file)
    
    def print_report(self):
        """Выводит отчет о найденных проблемах"""
        if not self.issues:
            print("\n✅ Все упражнения соответствуют библиотеке!")
            return
        
        print(f"\n⚠️  Найдено проблем: {len(self.issues)}\n")
        
        # Группируем по файлам
        issues_by_file: Dict[Path, List[Issue]] = {}
        for issue in self.issues:
            if issue.file not in issues_by_file:
                issues_by_file[issue.file] = []
            issues_by_file[issue.file].append(issue)
        
        for file, file_issues in issues_by_file.items():
            relative_path = file.relative_to(self.root_dir)
            print(f"📄 {relative_path}")
            
            for issue in file_issues:
                icon = "🔴" if issue.issue_type == 'not_in_library' else "⚠️ "
                print(f"  {icon} Строка {issue.line_number}: '{issue.exercise_found}'")
                if issue.suggestion != "Упражнение не найдено в библиотеке":
                    print(f"     💡 Возможно имелось в виду: '{issue.suggestion}'")
                else:
                    print(f"     ❌ {issue.suggestion}")
            print()
        
        # Статистика по типам проблем
        mismatch_count = sum(1 for i in self.issues if i.issue_type == 'name_mismatch')
        not_found_count = sum(1 for i in self.issues if i.issue_type == 'not_in_library')
        
        print("📊 Статистика:")
        print(f"   - Неточное название (есть похожее): {mismatch_count}")
        print(f"   - Не найдено в библиотеке: {not_found_count}")


def main():
    root_dir = Path(__file__).parent.parent
    validator = ExerciseValidator(root_dir)
    
    print("🏋️  Валидатор упражнений training-brain\n")
    
    if not validator.load_library():
        sys.exit(1)
    
    validator.validate_all_weeks()
    validator.print_report()
    
    # Возвращаем код ошибки если есть проблемы
    sys.exit(1 if validator.issues else 0)


if __name__ == '__main__':
    main()
