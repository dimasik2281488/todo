import tkinter as tk


class AppButton(tk.Button):
    """Собственная кнопка приложения с единым стилем."""

    def __init__(self, master, text, command=None, color="#4a6cf7", **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            bg=color,
            fg="#ffffff",
            activebackground="#3b55c4",
            activeforeground="#ffffff",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=12,
            pady=4,
            cursor="hand2",
            **kwargs,
        )
