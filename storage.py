"""Хранилище задач в памяти."""

from typing import List, Optional


class TaskStore:
    def __init__(self) -> None:
        self._tasks: List[str] = []

    def list_tasks(self) -> List[str]:
        return list(self._tasks)

    def add(self, title: str) -> str:
        cleaned = title.strip()
        if not cleaned:
            raise ValueError("Название задачи не может быть пустым.")
        self._tasks.append(cleaned)
        return cleaned

    def get(self, number: int) -> Optional[str]:
        index = number - 1
        if index < 0 or index >= len(self._tasks):
            return None
        return self._tasks[index]

    def edit(self, number: int, new_title: str) -> str:
        if self.get(number) is None:
            raise IndexError("Задачи с таким номером нет.")
        cleaned = new_title.strip()
        if not cleaned:
            raise ValueError("Название задачи не может быть пустым.")
        self._tasks[number - 1] = cleaned
        return cleaned

    def delete(self, number: int) -> str:
        if self.get(number) is None:
            raise IndexError("Задачи с таким номером нет.")
        return self._tasks.pop(number - 1)

    def __len__(self) -> int:
        return len(self._tasks)
