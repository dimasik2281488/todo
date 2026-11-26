import json
import os


class Storage:
    """Слой хранения данных: сохранение и загрузка задач в JSON."""

    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load(self):
        """Возвращает список задач. Если файла нет или он повреждён - пустой список."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def save(self, tasks):
        """Сохраняет список задач в JSON-файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
