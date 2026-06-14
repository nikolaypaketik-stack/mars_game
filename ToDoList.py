from pathlib import Path

import customtkinter as ctk


TASKS_FILE = Path(__file__).with_name("tasks.txt")


class TodoApp:
    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.title("To-Do")
        self.window.geometry("400x600")
        ctk.set_appearance_mode("dark")

        self.tasks: list[ctk.CTkCheckBox] = []

        ctk.CTkLabel(
            self.window,
            text="not",
            font=("Arial", 24, "bold"),
        ).pack(pady=20)

        self.entry = ctk.CTkEntry(
            self.window,
            placeholder_text="що плануєте?",
            height=45,
            corner_radius=15,
        )
        self.entry.pack(fill="x", padx=25, pady=5)

        button_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        button_frame.pack(pady=15)

        ctk.CTkButton(
            button_frame,
            text="+ Додати",
            width=120,
            corner_radius=10,
            command=self.on_add_click,
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="Очистити",
            width=120,
            corner_radius=10,
            command=self.delete_done_tasks,
            fg_color="red",
        ).pack(side="left", padx=5)

        self.scroll_frame = ctk.CTkScrollableFrame(self.window, width=340, height=320)
        self.scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.load_tasks()

    def run(self) -> None:
        self.window.mainloop()

    def save_to_file(self) -> None:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(f"{task.cget('text')}|{task.get() == 1}\n")

    def load_tasks(self) -> None:
        if not TASKS_FILE.exists():
            return

        with TASKS_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|", maxsplit=1)
                if len(parts) == 2:
                    self.add_task_ui(parts[0], parts[1] == "True", save=False)

    def add_task_ui(self, text: str, is_checked: bool = False, *, save: bool = True) -> None:
        task = ctk.CTkCheckBox(
            self.scroll_frame,
            text=text,
            command=self.save_to_file,
            corner_radius=20,
        )

        if is_checked:
            task.select()

        task.pack(anchor="w", pady=5, padx=10)
        self.tasks.append(task)

        if save:
            self.save_to_file()

    def on_add_click(self) -> None:
        text = self.entry.get().strip()
        if not text:
            return

        self.add_task_ui(text)
        self.entry.delete(0, "end")

    def delete_done_tasks(self) -> None:
        remaining_tasks = []

        for task in self.tasks:
            if task.get() == 1:
                task.destroy()
            else:
                remaining_tasks.append(task)

        self.tasks = remaining_tasks
        self.save_to_file()


def main() -> None:
    TodoApp().run()


if __name__ == "__main__":
    main()
