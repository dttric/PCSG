import time as t
import sys
import os
from termcolor import colored
wood = 0
planks = 0
home = 0
w_pickaxe = 0
rock = 0
r_pickaxe = 0

print(colored("Привет, " + os.getlogin(),'green'))
print(colored("help - команды",'green'))
print(colored("выходить только через exit",'green'))
print(colored("если нечего не происходит то нет такой команды",'green'))
while True:
    try:
        command = str(input(">>> "))
        if command == "menu":
            command = str(input(">>> "))

        if command == "wood":
            try:
                print("плюс 0.1 дерева в секунду =)")
                print("выход в меню с помощью ^C")
                print("добыча дерева идет")
                while True:
                    wood += 0.1
                    print(wood)
                    t.sleep(1)
            except KeyboardInterrupt:
                print("\nвозвращение в меню...")
        if command == "mine":
            if w_pickaxe or r_pickaxe >= 1:
                rock += 1
                w_pickaxe -= 1
                t.sleep(1)
                if w_pickaxe == 0:
                    command = "menu"
                if r_pickaxe == 0:
                    command = "menu"
            else:
                print("у тебя кирок нет ботинок (крафт через craft)")
                command = "menu"
        if command == "exit":
            exit()
        if command == "check":
            print("дерево:", wood)
            print("доски:", planks)
            print("дом:", home)
            print("д. кирка:", w_pickaxe)
            print("камни:", rock)
            print("кирка:", r_pickaxe)
        if command == "help":
            print(colored("список команд:",'green'))
            print(colored("craft для крафта",'green'))
            print(colored("mine для шахты",'green'))
            print(colored("wood для похода в лес по дерево",'green'))
            print(colored("menu для возвращения",'green'))
            print(colored("check для проверки материалов",'green'))
        if command == "craft":
            print("wpix для крафта д.кирки")
            print("pix для крафта кирки")
            print("home для дома")
            print("planks для досок")
            wtc = input("что крафтить?:")
            if wtc == "pix":
                if rock >= 10:
                    craft = input("Ты можешь скрафтить Кирку у нее 50 использываний (Y/N):")
                    if craft == "Y" or "y":
                        craft = True
                    if craft == True:
                        rock -= 10
                        r_pickaxe += 100
                        print("+100 прочности к.кирки =)")
                        print("-10 камня")
                else:
                    print("у тебя нет дерева на кирку (")
                wtc == False

            if wtc == "wpix":
                if wood >= 9:
                    craft = input("Ты можешь скрафтить Деревяную Кирку у нее 50 использываний (Y/N):")
                    if craft == "Y" or "y":
                        craft = True
                    if craft == True:
                        wood -= 9
                        w_pickaxe += 50
                        print("+50 прочности кирки =)")
                        print("-9 досок")
                else:
                    print("у тебя нет дерева на кирку (")
                wtc == False

            if wtc == "planks":
                if wood >= 5:
                    craft = input("доски из них крафтится все деревянное стоймость 5 дерева (Y/N):")
                    if craft == "Y" or "y":
                        craft = True
                        wood -= 5
                        planks += 50
                else:
                    print("нет дерева на доски (")
                wtc == False

            if wtc == "home":
                if planks >= 1000:
                    craft = input("Дом он даст нечего (пока) стоймость 100 досок (Y/N):")
                    if craft == "Y" or "y":
                        wood -= 100
                        home += 1
                    if home >= 1:
                        print("я заметил у тебя уже есть дом зачем тебе еще?")
                        print("нажми н не трать в пустую доски")
                else:
                    print("нет досок для постройки дома (")
                wtc == False
    except KeyboardInterrupt:
            print(colored("\nвыход только через exit",'green'))
