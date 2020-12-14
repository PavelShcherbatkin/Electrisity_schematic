from tkinter import *


def greeting():
    print('Hello stdout world!...')

root = Tk()
root.title("Определение оптимального срока службы элементов системы")
root.geometry("700x400")

win = Frame(root)
win.pack(side=LEFT)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)
win.mainloop()

win_2 = Frame(win)
win_2.pack(side=Right)
Button(win_2, text='Hello', command=greeting).pack(side=LEFT)

root.mainloop()