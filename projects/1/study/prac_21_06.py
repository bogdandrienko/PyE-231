import threading
import time
import tkinter as tk


# Практика: реализовать приложение с интерфейсом (таймер)
# pip install auto-py-to-exe
# auto-py-to-exe

def start():
    thread = threading.Thread(target=timer, args=(), kwargs={})
    thread.start()


def timer():
    global seconds
    global minutes
    global hours
    global is_play
    is_play = True

    while is_play:
        seconds += 1
        if seconds > 59:
            minutes += 1
            seconds = 0
        if minutes > 59:
            hours += 1
            minutes = 0
            seconds = 0

        time.sleep(0.1)
        label_result.config(text=str(f"{hours:02d}:{minutes:02d}:{seconds:02d}"))  # print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")


def pause():
    global is_play
    is_play = False


def stop():
    global seconds
    global minutes
    global hours
    seconds = 0
    minutes = 0
    hours = 0
    pause()
    label_result.config(text=str(f"{hours:02d}:{minutes:02d}:{seconds:02d}"))


if __name__ == "__main__":
    seconds = 0
    minutes = 0
    hours = 0
    is_play = True

    window = tk.Tk()  # создаётся главный экземпляр объекта

    # настройки окна
    window.title("Таймер")
    window.geometry('640x480')

    # наполнение дизайна
    label_result_title = tk.Label(window, text="Результат:", font=("Arial Bold", 25))
    label_result_title.grid(column=0, row=0)

    label_result = tk.Label(window, text="-", font=("Arial Bold", 25))
    label_result.grid(column=0, row=1)

    button_start = tk.Button(window, text="старт", command=start, font=("Arial Bold", 25))
    button_start.grid(column=0, row=2)

    button_pause = tk.Button(window, text="пауза", command=pause, font=("Arial Bold", 25))
    button_pause.grid(column=1, row=2)

    button_stop = tk.Button(window, text="стоп", command=stop, font=("Arial Bold", 25))
    button_stop.grid(column=2, row=2)

    # цикл событий - отрисовка окна
    window.mainloop()
