from customtkinter import *
import os

window = CTk()
window.title("To-Do")
window.geometry("400x600")
set_appearance_mode("dark")

# Список для зберігання об'єктів чекбоксів
all_tasks = []

# Функція запису всіх справ у текстовий файл
def save_to_file():
    # Відкриваємо файл на запис (старий вміст видаляється)
    with open("tasks.txt", "w", encoding="utf8") as f:
        # Проходимо по кожному чекбоксу в списку
        for task in all_tasks:
            # Отримуємо текст і стан (1 - виконано, 0 - ні)
            f.write(f"{task.cget("text")}|{task.get() == 1}\n")         


def add_task_ui(text, is_checked=False):
    task = CTkCheckBox(scrool_frame,
                       text=text,
                       command=save_to_file,
                       corner_radius=20
                       )

    # Якщо задача завантажена як "виконана", ставимо галочку
    if is_checked:
        task.select()
    
    task.pack(anchor="w", pady=5, padx=10)
    all_tasks.append(task)

    save_to_file()

# Функція обробки натискання кнопки "Додати"
def on_add_click():
    # Отримуємо текст із поля введення
    t = entry.get()

    # Якщо поле не порожнє, створюємо задачу і очищуємо поле
    if t:
        add_task_ui(t)
        entry.delete(0, "end")



# Функція очищення списку від завершених справ
def delete_done_tasks():
    global all_tasks

    new_list = []
    for task in all_tasks:
        if task.get() == 1:
            task.destroy()
        else:
            new_list.append(task)
    all_tasks = new_list

    save_to_file()


# Заголовок
CTkLabel(window,
         text="not",
         font=("Arial", 24, "bold")
        ).pack(pady=20)
       

# Поле введення
entry = CTkEntry(window,
                 placeholder_text="що плануєте?",
                 height=45,
                 corner_radius=15
                 )
entry.pack(fill="x", padx=25, pady=5)
# Контейнер для кнопок, щоб вони були в один ряд
btn_frame = CTkFrame(window,
                     fg_color="transparent"
                     )
btn_frame.pack(pady=15)

# Кнопка "+ Додати"
CTkButton(btn_frame,
          text="+ Додати",
          width=120,
          corner_radius=10,
          command=on_add_click,
          ).pack(side="left", padx=5)

# Кнопка видалення "🗑 Очистити" (червона: #E74C3C)
CTkButton(btn_frame,
          text="🗑 Очистити",
          width=120,
          corner_radius=10,
          command=delete_done_tasks,
          fg_color="red",
          ).pack(side="left", padx=5)

# Прокручувана область для задач
scrool_frame = CTkScrollableFrame(window, width=340, height=320)
scrool_frame.pack(pady=10, padx=10, fill="both", expand=True)


# Перевірка наявності файлу при старті
if os.path.exists("tasks.txt"):
    # Читаємо файл і відновлюємо задачі
    with open("tasks.txt", "r", encoding="utf8") as f:
        # Для кожного рядка розділяємо текст і статус
        for line in f:
            # Створюємо задачу на екрані
            parts = line.strip().split("|")
            if len(parts) == 2:
                add_task_ui(parts[0], parts[1] == "True")



# Запуск
window.mainloop()