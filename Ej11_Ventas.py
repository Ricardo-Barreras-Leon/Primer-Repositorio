import tkinter as tk
from tkinter import messagebox

def SubTotal ():
    CantiArticulos = float (CantidadArticulosEntry.get ())
    PrecioArticulos = float (PrecioArticulosEntry.get ())
    TotalSubTotal = CantiArticulos * PrecioArticulos

    Resultado.config ( text= f'El SUB TOTAL es de: {TotalSubTotal}')

def IVA ():
    CantiArticulos = float (CantidadArticulosEntry.get ())
    PrecioArticulos = float (PrecioArticulosEntry.get ())
    TotalIVA = (CantiArticulos * PrecioArticulos) * 0.16

    Resultado.config ( text= f'El IVA es de: {TotalIVA}')

def TOTAL ():
    CantiArticulos = float (CantidadArticulosEntry.get ())
    PrecioArticulos = float (PrecioArticulosEntry.get ())
    TotalIVA = (CantiArticulos * PrecioArticulos) * 0.16
    Total = TotalIVA + (CantiArticulos * PrecioArticulos)

    Resultado.config ( text= f'El precio TOTAL es de: {Total}')


Ventana = tk.Tk ()
Ventana.geometry ('400x400')
Ventana.title ('CALCULO DE VENTAS')

CantidadArticulos= tk.Label ( text = 'CANTIDAD DE ARTICULOS')
CantidadArticulos.pack ( pady = 10 )

CantidadArticulosEntry = tk.Entry ()
CantidadArticulosEntry.pack ( pady = 5 )

PrecioArticulo = tk.Label ( text = 'PRECIO POR ARTICULO')
PrecioArticulo.pack ( pady = 5 )

PrecioArticulosEntry = tk.Entry ()
PrecioArticulosEntry.pack ( pady = 5 )

BotonSubTotal = tk.Button ( text = 'SUB TOTAL' , command = SubTotal)
BotonSubTotal.pack ( pady = 5 )

BotonIVA = tk.Button ( text = 'IVA' , command= IVA)
BotonIVA.pack ( pady = 5 )

BotonTotalCompra = tk.Button ( text = 'TOTAL DE LA COMPRA' , command = TOTAL)
BotonTotalCompra.pack ( pady = 5 )

Resultado = tk.Label ( text = '')
Resultado.pack ( pady = 10 )

Ventana.mainloop ()