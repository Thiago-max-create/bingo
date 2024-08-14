

import tkinter as tk
import random
import time

numeroSorteado = []


root = tk.Tk()


label_var = tk.StringVar()
root.title("BINGO")
root.iconbitmap('./assents/BINGO.ico')

tk.Label(root, text="resultado: ").grid(row=3, column=0)
tk.Label(root, textvariable=label_var).grid(row=0, column=0)



button_style = {
    'font': ('Arial', 11),
    'bg': '#FF0000',
    'fg': '#ffffff',
    'relief': 'raised',
    'bd': 3,
    'width': 10,
    'height': 10
}


def sortear():
        if len(numeroSorteado) < 75:
            numero = random.randint(1, 75)
            while numero in numeroSorteado:
                numero = random.randint(1, 75)
            numeroSorteado.append(numero)
            label_var.set(numeroSorteado)
        else:
            label_var.set(text='Fim do jogo')




tk.Button(root, text="SORTEAR",  command=sortear, **button_style).grid(row=1, column=1)

root.mainloop()



