#Ventanas multiples

import tkinter as tk
from tkinter import Toplevel

Ventana1 = tk.Tk ()
Ventana1.title ('Nombre')
Ventana1.geometry ('300x300')

def abrir_ventana_hija():
    Ventana2 = tk.Tk ()
    Ventana2.title ('Programando en python')
    Ventana2.geometry ('300x300')

    ProgPython = tk.Label (Ventana2 , text = 'Programando en python' , font = ('Arial' , 12))
    ProgPython.pack ()  

Nombre = tk.Label (Ventana1 , text = 'Ricardo Barreras León', font = ('Arial' , 12))
Nombre.pack (pady = 20)

boton_abrir = tk.Button(Ventana1, text='Siguiente pagina', command=abrir_ventana_hija)
boton_abrir.pack(pady=20)

Ventana1.mainloop ()