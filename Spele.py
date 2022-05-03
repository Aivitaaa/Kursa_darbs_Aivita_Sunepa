import math
from array import *
import random
import MD1_modulis as nm
import MD1_ievades_modulis as inp


points = 0


def saskatisana():
    global points
    print()
    print("Saskaitīšana ar cipariem no 1 līdz 100, ievadiet pareizo atbildi: ")
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1, " + ", num2, "=... ?")
    input_sum = input()

    try:
        input_sum = int(input_sum)
    except:
        print("Ievadi veselu skaitli!!!")
        return

    real_sum = num1 + num2
    if real_sum == input_sum:
        points = points + 3
        print("Pareiza atbilde! :) ")
    else:
        points = points - 3
        print("Jāpamācas ! :(")
        print("Pareiza atbilde : ", real_sum)


def atnemsana():
    global points
    print()
    print("Atņemšana ar cipariem no 1 līdz 100, ievadiet pareizo atbildi (var būt negatīva atbilde): ")
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1, " - ", num2, "=... ?")
    input_starp = input()

    try:
        input_starp = int(input_starp)
    except:
        print("Ievadi veselu skaitli!!!")
        return

    real_starp = num1 - num2
    if real_starp == input_starp:
        points = points + 3
        print("Pareiza atbilde! :) ")
    else:
        points = points - 3
        print("Jāpamācas ! :(")
        print("Pareiza atbilde : ", real_starp)


def dalisana():
    global points
    print()
    print("Dalīšana ar skaitļiem no 1 līdz 100, ja rezultāts ir reāls skaitlis, tad ierakstīt pirmos divus ciparus aiz komata noapaļojot, atdalīt ar punktu!")
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1, " / ", num2, "=... ?")
    input_dal = input()

    try:
        input_dal = float(input_dal)
    except:
        print("Ievadi reālu skaitli!!!")
        return

    real_dal = round(num1/num2, 2)
    if real_dal == input_dal:
        points = points + 5
        print("Pareiza atbilde! :) ")
    else:
        points = points - 5
        print("Jāpamācas ! :(")
        print("Pareiza atbilde : ", real_dal)


def trigonometrija():
    global points
    print()
    print("Tiek dota sin/cos vērtība un nepieciešams ierakstīt atbilstošo vērtību")
    vert = {
        "oπ": 0,
        "π/2": 90,
        "π": 180,
        "2π/3": 270,
        "2π": 360}
    funk = ["sin", "cos"]
    rand_value = random.randint(0, 4)
    rand_funkc = random.randint(0, 1)
    keys_list = list(vert)
    key = keys_list[rand_value]

    print(funk[rand_funkc], " pie ", key, " = ... ?")
    input_val = input()

    try:
        input_val = int(input_val)
    except:
        print("Ievadi veselu skaitli!!!")
        return

    if rand_funkc == 0:
        real_val = round(math.sin(math.radians(vert[key])))
    else:
        real_val = round(math.cos(math.radians(vert[key])))

    if real_val == input_val:
        points = points + 8
        print("Pareiza atbilde! :) ")
    else:
        points = points - 8
        print("Jāpamācas ! :(")
        print("Pareiza atbilde : ", real_val)


def mini():
    print("Jums ir jāizvēlas tā jautājuma zīme, kura ir laimīgā => tā dubultos Jūsu punktu skaitu vai arī to pazaudēsiet")
    rows, cols = (2, 2)
    global points
    arr = [["?"]*cols]*rows
    for r in arr:
        for c in r:
            print(c, end=" ")
        print()
    row = input("Izvēlieties rindu: ")
    col = input("Izvēlieties kolonnu: ")
    try:
        row = int(row)
        col = int(col)
    except:
        print("Ievadi veselu skaitli!!!")
        return

    num1 = random.randint(1, 2)
    num2 = random.randint(1, 2)
    if row == num1 and col == num2:
        points = points * 2
        print("Pareiza atbilde, tu esi veiksmīgs! :) ")
    else:
        points = 0
        print("Paveiksies nākošreiz ! :(")


faila_vards = "rezultati.txt"
data = inp.pievienot_lietotaju()


while True:

    print()
    print("Šajā programmā var izvēlēties 4 matemātiskās spēles un vienu minēšanas spēli , kurās Jūs varat iegūt attiecīgo punktu skaitu vai to zaudēsiet")
    print("Saskaitīšana (3p) => 1")
    print("Atņemšana (3p) => 2 ")
    print("Dalīšana (5p) => 3")
    print("Trigonometriskās funkcijas (8p) => 4")
    print("Uzmini (2x punktu skaits) => 5")
    print("Beigt Darbu un Apskatīt Visus Rezultātus => 6")
    choise = input("Ievadiet Spēli: ")

    if choise == "1":
        saskatisana()

    elif choise == "2":
        atnemsana()

    elif choise == "3":
        dalisana()

    elif choise == "4":
        trigonometrija()

    elif choise == "5":
        mini()

    elif choise == "6":
        data = data + " " + str(points)
        nm.write_fail(faila_vards, data)
        nm.print_fail(faila_vards)
        break
    else:
        print("Ievadiet derīgu komandu! (skat. augstāk)")
       
