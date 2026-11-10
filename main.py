"""Лабораторная №5, вариант 2: GUI Tkinter (задания 2, 4, 7, 2*, 6*)."""
import tkinter as tk
from tkinter import messagebox, ttk


class LabApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ЛР №5 | Шкловский Г. В. | Вариант 2")
        self.geometry("750x560")
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label="Выход", command=self.destroy)
        menu.add_cascade(label="Файл", menu=file_menu)
        self.config(menu=menu)

        tabs = ttk.Notebook(self)
        tabs.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        text_frame = ttk.Frame(tabs, padding=16)
        list_frame = ttk.Frame(tabs, padding=16)
        draw_frame = ttk.Frame(tabs, padding=16)
        currency_frame = ttk.Frame(tabs, padding=16)
        for label, frame in [("Текст", text_frame), ("Список", list_frame),
                             ("Рисование", draw_frame), ("Конвертер", currency_frame)]:
            tabs.add(frame, text=label)

        ttk.Label(text_frame, text="Задание 2: введи текст").pack()
        self.text_input = ttk.Entry(text_frame, width=44)
        self.text_input.pack(pady=8)
        ttk.Button(text_frame, text="Показать",
                   command=lambda: messagebox.showinfo("Текст", self.text_input.get())).pack()

        ttk.Label(list_frame, text="Задание 4: выбери элемент").pack()
        self.items = tk.Listbox(list_frame, height=7)
        self.items.pack(fill=tk.X, pady=8)
        for item in ("Python", "Tkinter", "Git", "SQLite", "FastAPI"):
            self.items.insert(tk.END, item)
        ttk.Button(list_frame, text="Выбрать", command=self.choose_item).pack()

        ttk.Label(draw_frame, text="Повышенное 2: рисование мышью (левая кнопка)").pack()
        self.canvas = tk.Canvas(draw_frame, bg="white", height=300)
        self.canvas.pack(fill=tk.X, pady=8)
        self.last_point = None
        self.canvas.bind("<Button-1>", self.begin_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", lambda e: setattr(self, "last_point", None))
        ttk.Button(draw_frame, text="Очистить",
                   command=lambda: self.canvas.delete("all")).pack()

        ttk.Label(currency_frame, text="Повышенное 6: конвертер RUB → USD").pack()
        self.rubles = ttk.Entry(currency_frame)
        self.rubles.pack(pady=8)
        ttk.Label(currency_frame, text="Учебный фиксированный курс: 90 RUB за 1 USD").pack()
        ttk.Button(currency_frame, text="Перевести", command=self.convert).pack(pady=8)
        self.result = ttk.Label(currency_frame, text="")
        self.result.pack()

    def choose_item(self):
        selection = self.items.curselection()
        if not selection:
            messagebox.showwarning("Выбор", "Сначала выбери элемент")
            return
        messagebox.showinfo("Выбрано", self.items.get(selection[0]))

    def begin_draw(self, event):
        self.last_point = (event.x, event.y)

    def draw(self, event):
        if self.last_point:
            x, y = self.last_point
            self.canvas.create_line(x, y, event.x, event.y, width=3,
                                    fill="navy", capstyle=tk.ROUND, smooth=True)
        self.last_point = (event.x, event.y)

    def convert(self):
        try:
            amount = float(self.rubles.get().replace(",", "."))
            if amount < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Введите положительную сумму в рублях")
            return
        self.result.config(text=f"{amount / 90:.2f} USD")


if __name__ == "__main__":
    LabApp().mainloop()
