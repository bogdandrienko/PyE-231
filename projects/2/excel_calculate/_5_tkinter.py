# tkinter - самая примитивная, уже есть в питоне
# pyqt5 - самая продвинутая, очень тяжёлая, истоки - QT - C++
# pyside6 - ответвление pyqt5
import time
import tkinter as tk
import tkinter.ttk as ttk
import openpyxl
# pip install pyinstaller
# pyinstaller --onefile --windowed _5_tkinter.py
# pip install auto-py-to-exe
# auto-py-to-exe


def clicked():
    # lbl.configure(text="Я же просил...")
    print("Привет Евгений")

    # открыть файл
    workbook = openpyxl.load_workbook(str(entry_filename.get()))
    worksheet = workbook.active

    sum1 = 0
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        val = float(row[1])

        time.sleep(0.1)

        sum1 += val
    print(sum1)

    label_result.config(text=str(sum1))

def timer():
    seconds = 0
    minutes = 0
    hours = 0
    speed = 1.0

    while seconds < 10:
        seconds += 1
        if seconds > 59:
            minutes += 1
            seconds = 0
        if minutes > 59:
            hours += 1
            minutes = 0
            seconds = 0

        time.sleep(speed)  # 1.0 = 0.5 + 0.5 | 2x  # 1.0 = 0.1 + 0.1 ... | 10x  # 1.0 = 5.0 + 0.1 ... | 5x

        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        label_result.config(text=str(f"{hours:02d}:{minutes:02d}:{seconds:02d}"))


if __name__ == "__main__":
    window = tk.Tk()  # создаётся главный экземпляр объекта

    # настройки окна
    window.title("Заголовок окна")
    window.geometry('1280x720')

    # наполнение дизайна
    label_filename = tk.Label(window, text="Введите имя файла:", font=("Arial Bold", 25))
    label_filename.grid(column=0, row=0)

    entry_filename = tk.Entry(window, width=30, font=("Arial Bold", 25))
    entry_filename.insert(0, "temp/data.xlsx")
    entry_filename.grid(column=0, row=1)

    label_result_title = tk.Label(window, text="Результат:", font=("Arial Bold", 25))
    label_result_title.grid(column=1, row=0)

    label_result = tk.Label(window, text="-", font=("Arial Bold", 25))
    label_result.grid(column=1, row=1)

    button_start = tk.Button(window, text="Не нажимать!", command=clicked, font=("Arial Bold", 25))
    button_start.grid(column=2, row=2)

    # цикл событий - отрисовка окна
    window.mainloop()
