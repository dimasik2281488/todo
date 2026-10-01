"""Пользовательское меню и цикл приложения."""

from typing import Callable, Optional

from todo_app.storage import TaskStore


MENU_TEXT = """
=== Менеджер задач ===
1. Показать задачи
2. Добавить задачу
3. Редактировать задачу
4. Удалить задачу
0. Выйти
""".strip()


def parse_task_number(raw: str) -> Optional[int]:
    try:
        return int(raw.strip())
    except ValueError:
        return None


class TaskApp:
    def __init__(
        self,
        store: Optional[TaskStore] = None,
        reader: Callable[[str], str] = input,
        writer: Callable[[str], None] = print,
    ) -> None:
        self.store = store or TaskStore()
        self._read = reader
        self._write = writer
        self.running = True

    def show_menu(self) -> None:
        self._write("")
        self._write(MENU_TEXT)

    def show_tasks(self) -> None:
        self._write("")
        self._write("=== Список задач ===")
        tasks = self.store.list_tasks()
        if not tasks:
            self._write("Список задач пуст.")
            return
        for index, title in enumerate(tasks, start=1):
            self._write(f"{index}. {title}")

    def add_task(self) -> None:
        self._write("")
        self._write("=== Добавление задачи ===")
        title = self._read("Введите название задачи: ")
        try:
            self.store.add(title)
        except ValueError as error:
            self._write(str(error))
            return
        self._write("Задача добавлена.")

    def edit_task(self) -> None:
        self._write("")
        self._write("=== Редактирование задачи ===")
        if len(self.store) == 0:
            self._write("Список задач пуст.")
            return
        self.show_tasks()
        number = parse_task_number(self._read("Введите номер задачи: "))
        if number is None:
            self._write("Необходимо ввести число.")
            return
        new_title = self._read("Введите новое название: ")
        try:
            self.store.edit(number, new_title)
        except IndexError as error:
            self._write(str(error))
            return
        except ValueError as error:
            self._write(str(error))
            return
        self._write("Задача изменена.")

    def delete_task(self) -> None:
        self._write("")
        self._write("=== Удаление задачи ===")
        if len(self.store) == 0:
            self._write("Список задач пуст.")
            return
        self.show_tasks()
        number = parse_task_number(self._read("Введите номер задачи: "))
        if number is None:
            self._write("Необходимо ввести число.")
            return
        try:
            deleted = self.store.delete(number)
        except IndexError as error:
            self._write(str(error))
            return
        self._write(f"Задача «{deleted}» удалена.")

    def handle_choice(self, choice: str) -> None:
        mapping = {
            "1": self.show_tasks,
            "2": self.add_task,
            "3": self.edit_task,
            "4": self.delete_task,
            "0": self.exit_app,
        }
        action = mapping.get(choice.strip())
        if action is None:
            self._write("Неизвестная команда. Попробуйте снова.")
            return
        action()

    def exit_app(self) -> None:
        self.running = False
        self._write("Приложение завершено.")

    def run(self) -> None:
        self._write("Добро пожаловать в менеджер задач!")
        while self.running:
            self.show_menu()
            choice = self._read("Выберите действие: ")
            self.handle_choice(choice)


def main() -> None:
    TaskApp().run()
