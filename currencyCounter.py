
from cProfile import label
from multiprocessing.sharedctypes import Value
from optparse import Option
from currency_converter import CurrencyConverter
from datetime import date
import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date

import os

c = CurrencyConverter()

root = tk.Tk()

root.title("Currency converter by: Eetu Snellman")
root.geometry("500x1000")

canvas = tk.Canvas(root, height=1600, width=700, bg="#0127C1")
canvas.pack()

frame = tk.Frame(root, bg="#687FDB")
frame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.2)

frame = tk.Frame(root, bg="#687FDB")
frame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.5)


otsikko = Label(text="Currency converter application",
                fg="white", bg="#687FDB", font=("Courier", 15))

otsikko.place(relheight=0.05, relwidth=0.8, relx=0.5,
              rely=0.05, anchor=CENTER)

clicked = StringVar()
clicked.set("EUR")

drop = OptionMenu(root, clicked, *c.currencies)
drop.place(relx=0.3, rely=0.3, anchor=CENTER)

clicked1 = StringVar()
clicked1.set("EUR")


drop1 = OptionMenu(root, clicked1, *c.currencies)
drop1.place(relx=0.3, rely=0.6, anchor=CENTER)

syote_temp = DoubleVar()
syote2 = tk.Entry(root, textvariable=syote_temp)
syote2.place(relx=0.5, rely=0.3)
syote = syote2.get()


def convertCurrency():

    global tulos
    tulos = c.convert(syote, clicked.get(), clicked1.get(),
                      date=date(2022, 6, 6))

    amount = Label(root, text="%.2f" % tulos)
    amount.place(relx=0.6, rely=0.6, anchor=CENTER)

    print("%.2f" % tulos)


convertButton = Button(root, text="Convert", command=convertCurrency)
convertButton.place(relx=0.4, rely=0.3, anchor=CENTER)


root.mainloop()


käytetytValuutat = []

print("Lista valuutoista")

print(" ")

print(c.currencies)


def kysymys():
    global rahanMäärä
    rahanMäärä = input("Valitse rahan määrä. ")

    if rahanMäärä.isalpha() == True:
        print("Käytä rahamäärän ilmoittamiseen numeroita! ")
        kysymys()


def kysymys2():
    global muutetaan
    muutetaan = input(
        "Ilmoita alkuperäinen valuutta. Valitse vaihtoehto yllä olevasta listasta. ")
    muutetaan = muutetaan.upper()

    if muutetaan.isalpha() == False:
        print("Käytä valuutan ilmoittamiseen kirjaimia! ")
        kysymys2()

    elif muutetaan not in c.currencies:
        print("Valuutta epäsopiva! Ilmoita uusi valuutta. ")
        kysymys2()

    else:
        käytetytValuutat.append(muutetaan)


def kysymys3():
    global halutaan
    halutaan = input("Ilmoita mihin valuuttaan haluat muuttaa " +
                     rahanMäärä + " valuutasta " + muutetaan + " ")
    halutaan = halutaan.upper()

    if halutaan.isalpha() == False:
        print("Käytä valuutan ilmoittamiseen kirjaimia! ")
        kysymys3()

    elif halutaan in käytetytValuutat:
        print("Et voi ilmoittaa samaa valuuttaa kahdesti! Valitse toinen valuutta.")
        kysymys3()

    elif halutaan not in c.currencies:
        print("Valuutta epäsopiva! Ilmoita uusi valuutta. ")
        kysymys3()

    else:
        tulos = c.convert(rahanMäärä, muutetaan, halutaan)

        print("Raha " + rahanMäärä + " muutettuna " +
              muutetaan + " ----> " + halutaan)

        print("%.2f" % tulos)


# kysymys()
# kysymys2()
# kysymys3()
