#calculator_number3

import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = calc.get()
    if value == '0' and len(value) == 1:
        value = ''
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if not value:
        return
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def calculate():
    value = calc.get()
    if not value:
        return
    if value[-1] in '-+/*':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        eval_value = value.replace('×', '*').replace('÷', '/')#умножение можн убрать
        calc.insert(0, eval(eval_value))
    #обработка_ошибок
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Нужно вводить только цифры!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!')
        calc.insert(0, 0)

def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

win = tk.Tk()
win.geometry("540x600")
win.resizable(False, False)   # <-- ЗАПРЕТ ИЗМЕНЕНИЯ РАЗМЕРА
win['bg'] = '#2B2B2B'
win.title('Workmate WM-888X')

#самая верхняя панелька с экраном(первый прямоугольник)
bg_frame = tk.Frame(win, bg="#B2B2B2", bd=1, relief="flat")
bg_frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=(15, 4))
bg_frame.grid_columnconfigure(0, weight=1)

title_label = tk.Label(bg_frame, text="W WORKMATE", font=("Arial", 11, "bold"), fg="#1A1A1A", bg="#B2B2B2")
title_label.grid(row=0, column=0, pady=(6, 2))

#поле ввода побольше (шрифт и внутренний отступ)
calc = tk.Entry(bg_frame, justify=tk.RIGHT, font=("Consolas", 36, "bold"), bg="#BAC4B9", fg="#111111", bd=5, relief="sunken")
calc.insert(0, '0')
calc.grid(row=1, column=0, sticky='we', padx=20, pady=(0, 15), ipady=10)

#средняя панелька с белым фоном(прямоугольник2?)
bg_frame2 = tk.Frame(win, bg="#B2B2B2", bd=1, relief="flat")
bg_frame2.grid(row=1, column=0, sticky="nsew", padx=15, pady=4)
for i in range(6):
    bg_frame2.grid_columnconfigure(i, weight=1)
#прочие по мелочам(текст и мелкие детали)
text1 = tk.Label(bg_frame2, text="WM-888X", font=("Arial", 14, "bold"), fg="black", bg="#B2B2B2")
text1.grid(row=0, column=0, columnspan=2, sticky='w', padx=18, pady=(4, 0))

text2 = tk.Label(bg_frame2, text="12-DIGIT CALCULATOR\n[ 2 POWER ]", font=("Arial", 10, "bold"), fg="black", bg="#B2B2B2", justify="left")
text2.grid(row=1, column=0, columnspan=2, sticky='w', padx=18, pady=(0, 6))

solar_panel = tk.Frame(bg_frame2, bg="#555511", width=200, height=40, relief="sunken", bd=2)
solar_panel.grid(row=0, column=3, columnspan=2, rowspan=2, padx=5, pady=5)

digit_text1 = tk.Label(bg_frame2, text="12", font=("Arial", 14, "bold"), fg="black", bg="#B2B2B2")
digit_text1.grid(row=0, column=5, sticky='s', padx=18)
digit_text2 = tk.Label(bg_frame2, text="digits", font=("Arial", 9), fg="black", bg="#B2B2B2")
digit_text2.grid(row=1, column=5, padx=18)

#поле ввода с кнопками
bg_frame3 = tk.Frame(win, bg="#3b3b3b", bd=1, relief="flat")
bg_frame3.grid(row=2, column=0, sticky="nsew", padx=15, pady=(4, 15))

for i in range(8):
    bg_frame3.grid_columnconfigure(i, weight=1)

#основной фрейм(на нем кнопки)
main_frame = tk.Frame(bg_frame3, bg="#3b3b3b", relief="sunken", bd=3)
main_frame.grid(row=1, column=0, rowspan=5, columnspan=8, sticky="ew")

for i in range(8):
    main_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    main_frame.grid_rowconfigure(i, weight=1, minsize=52)

btn_digit = {"bd": 3, "relief": "raised", "font": ('Arial', 14, 'bold'), "bg": "#D6D6D6", "fg": "#111111"}
btn_dark = {"bd": 3, "relief": "raised", "font": ('Arial', 12, 'bold'), "bg": "#4A4A4A", "fg": "#FFFFFF"}
btn_blue = {"bd": 3, "relief": "raised", "font": ('Arial', 11, 'bold'), "bg": "#366CA8", "fg": "#FFFFFF"}

#нерабочие балванки!!!!!
tk.Button(bg_frame3, text='↑5/4↓', **btn_dark).grid(row=0, column=0, sticky='wens', padx=3, pady=6)
tk.Button(bg_frame3, text='MⅠⅡ', **btn_dark).grid(row=0, column=2, sticky='wens', padx=3, pady=6)
tk.Button(bg_frame3, text='MⅠ-', **btn_dark).grid(row=0, column=3, sticky='wens', padx=3, pady=6)
tk.Button(bg_frame3, text='MⅠ+', **btn_dark).grid(row=0, column=4, sticky='wens', padx=3, pady=6)
tk.Button(bg_frame3, text='A0234F', **btn_dark).grid(row=0, column=6, columnspan=2, sticky='wens', padx=3, pady=6)

#адекватные кнопки значений
#строка 0
tk.Button(main_frame, text='MC', **btn_dark).grid(row=0, column=0, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='MR', **btn_dark).grid(row=0, column=2, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='M-', **btn_dark).grid(row=0, column=3, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='M+', **btn_dark).grid(row=0, column=4, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='√', **btn_dark).grid(row=0, column=6, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='MU', **btn_dark).grid(row=0, column=7, sticky='wens', padx=3, pady=3)

#строка 1
tk.Button(main_frame, text='00→0', **btn_dark).grid(row=1, column=0, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='7', **btn_digit, command=lambda: add_digit('7')).grid(row=1, column=2, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='8', **btn_digit, command=lambda: add_digit('8')).grid(row=1, column=3, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='9', **btn_digit, command=lambda: add_digit('9')).grid(row=1, column=4, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='÷', **btn_dark, command=lambda: add_operation('/')).grid(row=1, column=6, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='%', **btn_dark).grid(row=1, column=7, sticky='wens', padx=3, pady=3)

#строка2
tk.Button(main_frame, text='+/-', **btn_dark).grid(row=2, column=0, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='4', **btn_digit, command=lambda: add_digit('4')).grid(row=2, column=2, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='5', **btn_digit, command=lambda: add_digit('5')).grid(row=2, column=3, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='6', **btn_digit, command=lambda: add_digit('6')).grid(row=2, column=4, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='*', **btn_dark, command=lambda: add_operation('*'   )).grid(row=2, column=6, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='—', **btn_dark, command=lambda: add_operation('-')).grid(row=2, column=7, sticky='wens', padx=3, pady=3)

#строка 3
tk.Button(main_frame, text='ON\nAC', **btn_blue, command=clear).grid(row=3, column=0, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='1', **btn_digit, command=lambda: add_digit('1')).grid(row=3, column=2, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='2', **btn_digit, command=lambda: add_digit('2')).grid(row=3, column=3, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='3', **btn_digit, command=lambda: add_digit('3')).grid(row=3, column=4, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='+', **btn_dark, command=lambda: add_operation('+')).grid(row=3, column=6, rowspan=2, sticky='wens', padx=3, pady=3)
tk.Button(main_frame, text='=', **btn_dark, command=calculate).grid(row=3, column=7, rowspan=2, sticky='wens', padx=3, pady=3)

# СТРОКА 4
tk.Button(main_frame, text='CE/C', **btn_blue, command=clear).grid(row=4, column=0, sticky='wens', padx=(3,2), pady=3)
tk.Button(main_frame, text='0', **btn_digit, command=lambda: add_digit('0')).grid(row=4, column=1, columnspan=2, sticky='wnse', padx=(10,2), pady=3)
tk.Button(main_frame, text='00', **btn_digit, command=lambda: add_digit('00')).grid(row=4, column=3, sticky='wens', padx=2, pady=3)
tk.Button(main_frame, text='.', **btn_digit, command=lambda: add_digit('.')).grid(row=4, column=4, sticky='wens', padx=2, pady=3)

win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=0)
win.grid_rowconfigure(2, weight=5)
win.grid_columnconfigure(0, weight=1)

win.mainloop()