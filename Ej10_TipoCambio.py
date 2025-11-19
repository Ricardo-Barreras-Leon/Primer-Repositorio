#Da sierta cantidad de dinero dependiendo en cuanto este el peso equivalente.

import tkinter as tk
from tkinter import messagebox

def TotalDolares ():
    Dolar = 18.46
    PesoMex = float (CantidadEntry.get ())
    CantiDolares = PesoMex / Dolar

    RespuestaBoton.config ( text = f'Cantidad en Dolares: {CantiDolares:.2f}')

def TotalEuros ():
    Euros = 21.45
    PesoMex = float (CantidadEntry.get ())
    CantiEuros = PesoMex / Euros

    RespuestaBoton.config ( text = f'Cantidad en Euros: {CantiEuros:.2f}')

def TotalLibras ():
    Libre = 24.66
    PesoMex = float (CantidadEntry.get ())
    CantiLibra = PesoMex / Libre

    RespuestaBoton.config ( text = f'Cantidad en Libras: {CantiLibra:.2f}')

def TotalYenes ():
    Yenes = 8.20
    PesoMex = float (CantidadEntry.get ())
    CantiYenes = PesoMex * Yenes

    RespuestaBoton.config ( text = f'Cantidad en Yenes: {CantiYenes:.2f}')

Ventana = tk.Tk ()
Ventana.geometry ('400x400')
Ventana.title ('DIVISAS')

Cantidad = tk.Label ( text = 'CANTIDAD')
Cantidad.pack ( pady = 10 )

CantidadEntry = tk.Entry ()
CantidadEntry.pack ( pady = 5 )

DolaresBoton = tk.Button ( text = 'Dólares', command = TotalDolares)
DolaresBoton.pack (pady = 5 )

EurosBoton = tk.Button ( text = 'Euros' , command = TotalEuros)
EurosBoton.pack (pady = 5 )

LibrasBoton = tk.Button ( text = 'Libras' , command = TotalLibras)
LibrasBoton.pack ( pady = 5 )

YenesBoton = tk.Button ( text = 'Yenes' , command = TotalYenes)
YenesBoton.pack ( pady = 5 )

RespuestaBoton = tk.Label ( text = '.' )
RespuestaBoton.pack ( pady = 10 )

Ventana.mainloop ()