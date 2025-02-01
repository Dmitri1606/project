import tkinter as tk

def get_values():
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter=value2*value1
    result_label = tk.Label(window, text=ter)
    result_label.grid(column=1, row=4)
def divide():
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    print( value1/value2)

# Создаем главное окно
window = tk.Tk()

# Создаем два поля ввода
entry1 = tk.Entry(window, width=10)
entry1.grid(column=1, row=0)

entry2 = tk.Entry(window, width=10)
entry2.grid(column=1, row=1)

# Создаем кнопку для получения значений
btn = tk.Button(window, text="умножить", command=get_values)
btn.grid(column=1, row=2)
btn2 = tk.Button(window, text="поделить", command=divide)
btn2.grid(column=1, row=3)
# Запускаем главный цикл приложения

window.mainloop()
