from tkinter import *
from time import sleep

def exit():
	val.configure(text="Вывод: кнопка будет работать когда я добавлю сейвы")

def help():
	val.configure(text="Вывод: название кнопок читай!")

root = Tk()
root.title("ПКСГ")
root.geometry('330x160')
root.resizable(width=0, height=0)
welcome = Label(text="Добро Пожаловать в ПКСГ 1.5")
wtuwd = Label(text="Что вы хотите делать?")
val = Label(text="Вывод: ", font=("Monospace",8), bg="black", fg="white")
craft = Button(root, text="крафт")
mine = Button(root, text="шахта")
wood = Button(root, text="лес")
check = Button(root, text="проверка ресов")
help = Button(root, text="помощь", command=help)
exit = Button(root, text="выход (без сохранения)", command=exit)
welcome.pack()
wtuwd.pack()
val.pack()
help.pack(side="top")
exit.pack(side="top")
craft.pack(side="left")
mine.pack(side="left")
wood.pack(side="left")
check.pack(side="right")
root.mainloop()
