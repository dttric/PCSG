from tkinter import *
from tkinter import messagebox
from time import sleep
from tkinter.ttk import Combobox  
import sys

# items
wood = 0
planks = 0
home = 0
w_pickaxe = 0
rock = 0
r_pickaxe = 0

def exit():
	sys.exit()

def error_win():
	messagebox.showinfo('Произошла ошибка!', 'Чет не работает \nЖди обнову на гитхаб') 

def craft():
	def craft_process():
		print("начат процесс...")

	def error_win():
		messagebox.showinfo('Произошла ошибка!', 'Система создания недоделаная! \nЖди обнову на гитхаб')
		
	craft = Tk()
	craft.geometry('330x70')
	craft.resizable(width=0, height=0)
	craft.title("ПКСГ (Крафт)")
	lablc = Label(craft, text="Выбирайте:")
	wtc = Combobox(craft, state="readonly")
	craft_now = Button(craft, text="Создать!", command=error_win)
	wtc['values'] = ('Доски','Д.Кирка','Дом','Кирка')
	lablc.pack(side="left")
	wtc.pack(side="left")
	wtc.get()
	craft_now.pack(side="bottom")
	craft.mainloop()
		
def help():
	help = Tk()
	help.title("ПКСГ (Помощь)")
	help.geometry('360x160')
	help.resizable(width=0, height=0)
	label = Label(text="Отправляйте баги на гитхаб")
	ghlink = Label(text="https://github.com/dttric/PCSG")
	label.pack()
	ghlink.pack()
	help.mainloop()

root = Tk()
root.title("ПКСГ")
root.geometry('330x160')
root.resizable(width=0, height=0)
welcome = Label(text="Добро Пожаловать в ПКСГ 1.5")
wtuwd = Label(text="Что вы хотите делать?")
craft = Button(root, text="крафт", command=craft)
mine = Button(root, text="шахта", command=error_win)
wood = Button(root, text="лес", command=error_win)
check = Button(root, text="проверка ресов", command=error_win)
help = Button(root, text="помощь", command=help)
exit = Button(root, text="выход (без сохранения)", command=exit)
welcome.pack()
wtuwd.pack()
help.pack(side="top")
exit.pack(side="top")
craft.pack(side="left")
mine.pack(side="left")
wood.pack(side="left")
check.pack(side="right")
root.mainloop()