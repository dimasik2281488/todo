import tkinter as tk


class AppListbox(tk.Listbox):
    """Собственный список для отображения задач."""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            bg="#2a2a3d",
            fg="#ffffff",
            selectbackground="#4a6cf7",
            font=("Arial", 12),
            activestyle="none",
            borderwidth=0,
            highlightthickness=0,
            **kwargs,
        )

    def show_tasks(self, tasks):
        """Отображает задачи; выполненные помечаются галочкой."""
        self.delete(0, tk.END)
        for task in tasks:
            mark = "[x]" if task["done"] else "[ ]"
            self.insert(tk.END, f"{mark} {task['title']}")

    def get_selected_index(self):
        """Возвращает индекс выбранной задачи или None."""
        selection = self.curselection()
        return selection[0] if selection else None
