import tkinter as tk
from tkinter import ttk



def MostrarColor (event):
    Selecion = ElegirCombobox.get ()

    if Selecion == 'ROJO':
        Colores.config ( background= 'red')
        Color = 'red'
    elif Selecion == 'AZUL':
        Colores.config ( background= 'blue')
        Color = 'blue'
    elif Selecion == 'AMARILLO':
        Colores.config ( background= 'yellow')
        Color = 'yellow'
    elif Selecion == 'VERDE':
        Colores.config ( background= 'green')
        Color = 'green'
    else:
        Colores.config ( background= 'purple')
        Color = 'purple'

    Resultado.config (text= f'Has seleccionado el color: {Selecion}', fg = Color, background='black')

Ventana = tk.Tk ()
Ventana.title ('Seleccion de color')
Ventana.geometry ('300x100')

Elegir = tk.Label (Ventana, text = 'SELECCIONA UN COLOR.')
Elegir.pack (pady = 2)

Opciones = ['ROJO', 'AZUL', 'AMARILLO', 'VERDE', 'MORADO']

ElegirCombobox = ttk.Combobox ( Ventana, values= Opciones, state = 'readonly')
ElegirCombobox.pack (pady = 2)

ElegirCombobox.bind ('<<ComboboxSelected>>', MostrarColor)

Resultado = tk.Label ( Ventana, text = 'Selecciona un color para mostrar.')
Resultado.pack ()

Colores = tk.Label (text='             ')
Colores.pack (pady= 2)


Ventana.mainloop ()
