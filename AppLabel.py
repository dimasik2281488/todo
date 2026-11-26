import tkinter as tk


class AppLabel(tk.Label):
    """Собственная надпись приложения с единым стилем."""

    def __init__(self, master, text="", size=11, bold=False, **kwargs):
        super().__init__(
            master,
            text=text,
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Arial", size, "bold" if bold else "normal"),
            **kwargs,
        )

    def show_tasks(self, tasks):
        """Показывает статистику задач: всего и выполнено."""
        done = sum(1 for task in tasks if task["done"])
        self.config(text=f"Всего задач: {len(tasks)} | Выполнено: {done}")
