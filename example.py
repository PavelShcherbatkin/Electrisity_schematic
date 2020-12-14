from time import gmtime, strftime
import tkinter as tk
import os
import sqlite3


def run():
    global options_1
    global options_2
    global options_3
    global options_4
    os.system('add.py')
    data = my_reload()
    print(data)
    options_1, options_2, options_3, options_4 = data
    om_1 = tk.OptionMenu(frm_con, variable_1, *options_1)
    om_1.grid(row=2, column=0, padx=5, pady=5, sticky='n')
    om_2 = tk.OptionMenu(frm_con, variable_2, *options_2)
    om_2.grid(row=3, column=0, padx=5, pady=5, sticky='n')
    om_3 = tk.OptionMenu(frm_con, variable_3, *options_3)
    om_3.grid(row=4, column=0, padx=5, pady=5, sticky='n')
    om_4 = tk.OptionMenu(frm_con, variable_4, *options_4)
    om_4.grid(row=5, column=0, padx=5, pady=5, sticky='n')

window = tk.Tk()
window.title("Определение оптимального срока службы элементов системы")

frm_1 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
frm_1.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

window.rowconfigure([0, 1, 2], weight=1, minsize=50)
window.columnconfigure([0, 1, 2], weight=1, minsize=50)

frm_1.rowconfigure([0, 1, 2], weight=0, minsize=20)
frm_1.columnconfigure([0, 1, 2], weight=1, minsize=50)



# Фрейм для конструктора
frm_con = tk.Frame(master=frm_1, relief=tk.SUNKEN, borderwidth=3)
frm_con.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

frm_con.rowconfigure([0, 1, 2, 3, 4], weight=0, minsize=10)
frm_con.columnconfigure([0, 1], weight=1, minsize=25)


# Данные
shema_data = {}

# Данные для конструктора [id, link, name, наработка на отказ, номинальная интенсивность отказа]
# данные по первой конфигурации элекментов

def get_data():
    sql = f'SELECT * FROM elements'
    conn = sqlite3.connect('database.db')
    data = conn.execute(sql).fetchall()
    conn.close()
    return data


# данные по первой конфигурации элекментов
options_1 = []

# данные по второй конфигурации элекментов
options_2 = []

# данные по третей конфигурации элекментов
options_3 = []

# данные по четвертой конфигурации элекментов
options_4 = []

def add():
    data = get_data()
    for element in data:
        el = str(element[1]) + ' ' + element[2] + ' ' + str(element[3]) + ' ' + str(element[4])
        if element[1] == 1:
            options_1.append(el)
        elif element[1] == 2:
            options_2.append(el)
        elif element[1] == 3:
            options_3.append(el)
        elif element[1] == 4:
            options_4.append(el)


def my_reload():
    data = get_data()
    options_1 = []
    options_2 = []
    options_3 = []
    options_4 = []
    for element in data:
        el = str(element[1]) + ' ' + element[2] + ' ' + str(element[3]) + ' ' + str(element[4])
        if element[1] == 1:
            options_1.append(el)
        elif element[1] == 2:
            options_2.append(el)
        elif element[1] == 3:
            options_3.append(el)
        elif element[1] == 4:
            options_4.append(el)
    return (options_1, options_2, options_3, options_4)


add()

def ok():
    print('Установка нового времени')

def information(link):
    entry_1['text'] = shema_data[link][0]
    entry_2['text'] = shema_data[link][1]
    entry_3['text'] = shema_data[link][2]
    entry_4['text'] = shema_data[link][3]


def ok_1():
    t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    n = number_of_link.get()
    for label in frm_com.grid_slaves():
        if int(label.grid_info()["row"]) == int(n):
            label.destroy()
    for entry in frm_date.grid_slaves():
        if int(entry.grid_info()["row"]) == int(n):
            entry.destroy()
    lbl = tk.Label(frm_date, text = 'Звено номер: ' + n)
    lbl.grid(row=n, column=0)
    entry = tk.Entry(master=frm_date, width=50, relief=tk.SUNKEN, borderwidth=3)
    entry.insert(0, t)
    entry.grid(row=n, column=1)
    btn = tk.Button(master=frm_date, text='Применить', command=ok)
    btn.grid(row=n, column=2)
    name = variable_1.get()
    lbl_1 = tk.Label(frm_com, text = 'Звено номер: ' + n)
    lbl_2 = tk.Label(frm_com, text = 'Тип элемента: 1')
    lbl_3 = tk.Label(frm_com, text = 'Элемент: ' + name)
    btn_4 = tk.Button(master=frm_com, text='Посмотреть информацию', command=(lambda: information(int(n))))
    lbl_1.grid(row=n, column=0)
    lbl_2.grid(row=n, column=1)
    lbl_3.grid(row=n, column=2)
    btn_4.grid(row=n, column=3)
    new_name = name.split(" ")
    shema_data[int(n)] = [new_name[0], new_name[1], new_name[2], new_name[3]]


def ok_2():
    t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    n = number_of_link.get()
    for label in frm_com.grid_slaves():
        if int(label.grid_info()["row"]) == int(n):
            label.destroy()
    for entry in frm_date.grid_slaves():
        if int(entry.grid_info()["row"]) == int(n):
            entry.destroy()
    lbl = tk.Label(frm_date, text = 'Звено номер: ' + n)
    lbl.grid(row=n, column=0)
    entry = tk.Entry(master=frm_date, width=50, relief=tk.SUNKEN, borderwidth=3)
    entry.insert(0, t)
    entry.grid(row=n, column=1)
    btn = tk.Button(master=frm_date, text='Применить', command=ok)
    btn.grid(row=n, column=2)
    name = variable_2.get()
    lbl_1 = tk.Label(frm_com, text = 'Звено номер: ' + n)
    lbl_2 = tk.Label(frm_com, text = 'Тип элемента: 2')
    lbl_3 = tk.Label(frm_com, text = 'Элемент: ' + name)
    btn_4 = tk.Button(master=frm_com, text='Посмотреть информацию', command=(lambda: information(int(n))))
    lbl_1.grid(row=n, column=0)
    lbl_2.grid(row=n, column=1)
    lbl_3.grid(row=n, column=2)
    btn_4.grid(row=n, column=3)
    new_name = name.split(" ")
    shema_data[int(n)] = [new_name[0], new_name[1], new_name[2], new_name[3]]

def ok_3():
    t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    n = number_of_link.get()
    for label in frm_com.grid_slaves():
        if int(label.grid_info()["row"]) == int(n):
            label.destroy()
    for entry in frm_date.grid_slaves():
        if int(entry.grid_info()["row"]) == int(n):
            entry.destroy()
    lbl = tk.Label(frm_date, text = 'Звено номер: ' + n)
    lbl.grid(row=n, column=0)
    entry = tk.Entry(master=frm_date, width=50, relief=tk.SUNKEN, borderwidth=3)
    entry.insert(0, t)
    entry.grid(row=n, column=1)
    btn = tk.Button(master=frm_date, text='Применить', command=ok)
    btn.grid(row=n, column=2)
    name = variable_3.get()
    lbl_1 = tk.Label(frm_com, text = 'Звено номер: ' + n)
    lbl_2 = tk.Label(frm_com, text = 'Тип элемента: 3')
    lbl_3 = tk.Label(frm_com, text = 'Элемент: ' + name)
    btn_4 = tk.Button(master=frm_com, text='Посмотреть информацию', command=(lambda: information(int(n))))
    lbl_1.grid(row=n, column=0)
    lbl_2.grid(row=n, column=1)
    lbl_3.grid(row=n, column=2)
    btn_4.grid(row=n, column=3)
    new_name = name.split(" ")
    shema_data[int(n)] = [new_name[0], new_name[1], new_name[2], new_name[3]]

def ok_4():
    t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    n = number_of_link.get()
    for label in frm_com.grid_slaves():
        if int(label.grid_info()["row"]) == int(n):
            label.destroy()
    for entry in frm_date.grid_slaves():
        if int(entry.grid_info()["row"]) == int(n):
            entry.destroy()
    lbl = tk.Label(frm_date, text = 'Звено номер: ' + n)
    lbl.grid(row=n, column=0)
    entry = tk.Entry(master=frm_date, width=50, relief=tk.SUNKEN, borderwidth=3)
    entry.insert(0, t)
    entry.grid(row=n, column=1)
    btn = tk.Button(master=frm_date, text='Применить', command=ok)
    btn.grid(row=n, column=2)
    name = variable_4.get()
    lbl_1 = tk.Label(frm_com, text = 'Звено номер: ' + n)
    lbl_2 = tk.Label(frm_com, text = 'Тип элемента: 4')
    lbl_3 = tk.Label(frm_com, text = 'Элемент: ' + name)
    btn_4 = tk.Button(master=frm_com, text='Посмотреть информацию', command=(lambda: information(int(n))))
    lbl_1.grid(row=n, column=0)
    lbl_2.grid(row=n, column=1)
    lbl_3.grid(row=n, column=2)
    btn_4.grid(row=n, column=3)
    new_name = name.split(" ")
    shema_data[int(n)] = [new_name[0], new_name[1], new_name[2], new_name[3]]

variable_1 = tk.StringVar(window)
variable_1.set('1')

variable_2 = tk.StringVar(window)
variable_2.set('2')

variable_3 = tk.StringVar(window)
variable_3.set('3')

variable_4 = tk.StringVar(window)
variable_4.set('4')


#Виджеты Конструктор
constructer = tk.Label(master=frm_con, text='Конструктор')
constructer.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

number_of_link = tk.Entry(master=frm_con)
number_of_link.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="n")

om_1 = tk.OptionMenu(frm_con, variable_1, *options_1)
om_1.grid(row=2, column=0, padx=5, pady=5, sticky='n')
btn_1 = tk.Button(master=frm_con, text='1_Ok', width=10, command=ok_1)
btn_1.grid(row=2, column=1, padx=5, pady=5, sticky='n')

om_2 = tk.OptionMenu(frm_con, variable_2, *options_2)
om_2.grid(row=3, column=0, padx=5, pady=5, sticky='n')
btn_2 = tk.Button(master=frm_con, text='2_Ok', width=10, command=ok_2)
btn_2.grid(row=3, column=1, padx=5, pady=5, sticky='n')

om_3 = tk.OptionMenu(frm_con, variable_3, *options_3)
om_3.grid(row=4, column=0, padx=5, pady=5, sticky='n')
btn_3 = tk.Button(master=frm_con, text='3_Ok', width=10, command=ok_3)
btn_3.grid(row=4, column=1, padx=5, pady=5, sticky='n')

om_4 = tk.OptionMenu(frm_con, variable_4, *options_4)
om_4.grid(row=5, column=0, padx=5, pady=5, sticky='n')
btn_4 = tk.Button(master=frm_con, text='4_Ok', width=10, command=ok_4)
btn_4.grid(row=5, column=1, padx=5, pady=5, sticky='n')



# Фрейм для компонент
frm_com = tk.Frame(master=frm_1, relief=tk.SUNKEN, borderwidth=3)
frm_com.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

frm_com.rowconfigure(0, weight=0, minsize=10)
frm_com.columnconfigure([0, 1, 2, 3], weight=1, minsize=25)

# Виджеты для компонент
components = tk.Label(master=frm_com, text='Компоненты')
components.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="n")



# Фрейм для дата установки
frm_date = tk.Frame(master=frm_1, relief=tk.SUNKEN, borderwidth=3)
frm_date.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')

frm_date.rowconfigure(0, weight=0, minsize=10)
frm_date.columnconfigure([0, 2], weight=1, minsize=25)
frm_date.columnconfigure(1, weight=0, minsize=25)

date = tk.Label(master=frm_date, text='Дата установки')
date.grid(row=0, column=0, padx=5, pady=5, sticky="n")




# требуемый уровень надежности
reliability = tk.Label(master=frm_1, text='Требуемый уровень надежности:')
reliability.grid(row=1, column=0)

ent_reliability = tk.Entry(master=frm_1, width=50, relief=tk.SUNKEN, borderwidth=3)
ent_reliability.grid(row=1, column=1)


def calculate():
    print('Будет расчет замены элементов')
    print(shema_data)


btn_reliability = tk.Button(master=frm_1, text="Вывод плана замены оборудования", command=calculate)
btn_reliability.grid(row=1, column=2)



# Схема
frm_2 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
frm_2.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
frm_2.rowconfigure([0, 1, 2], weight=0, minsize=20)
frm_2.columnconfigure([0, 1, 2], weight=1, minsize=50)

shema = tk.Label(master=frm_2, text='Схема')
shema.grid(row=0, column=0, padx=5, pady=5, sticky="n")


# Информация о выбранном компоненте
frm_3 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
frm_3.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
inf = tk.Label(master=frm_3, text='Информация о выбранном компоненте:')
inf.grid(row=0, column=0, padx=5, pady=5, sticky="n")

# Тип элемента
label_1 = tk.Label(master=frm_3, text="Тип элемента:")
entry_1 = tk.Label(master=frm_3, width=50, relief=tk.SUNKEN, borderwidth=3)
label_1.grid(row=1, column=0, sticky="e")
entry_1.grid(row=1, column=1)


# Наименование
label_2 = tk.Label(master=frm_3, text="Наименование:")
entry_2 = tk.Label(master=frm_3, width=50, relief=tk.SUNKEN, borderwidth=3)
label_2.grid(row=2, column=0, sticky="e")
entry_2.grid(row=2, column=1)

# Наработка на отказ
label_3 = tk.Label(master=frm_3, text="Наработка на отказ:")
entry_3 = tk.Label(master=frm_3, width=50, relief=tk.SUNKEN, borderwidth=3)
label_3.grid(row=3, column=0, sticky="e")
entry_3.grid(row=3, column=1)

#Номинальная интенсивность отказов
label_4 = tk.Label(master=frm_3, text="Номинальная интенсивность отказов:")
entry_4 = tk.Label(master=frm_3, width=50, relief=tk.SUNKEN, borderwidth=3)
label_4.grid(row=4, column=0, sticky="e")
entry_4.grid(row=4, column=1)

# Кнопка добавить
label_5 = tk.Button(master=frm_3, text="Добавить компонент", command=run)
label_5.grid(row=5, column=1, sticky="e")


window.mainloop()
