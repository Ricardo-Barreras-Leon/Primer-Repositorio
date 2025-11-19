#Operaciones Basicas
import tkinter as tk

Ventana1 = tk.Tk ()
Ventana1.title ('Operaciones')
Ventana1.geometry ('400x400')


Num1Label = tk.Label (Ventana1 , text = 'Introduce el primer numero.')
Num1Label.pack (pady = 10)
Num1Entry = tk.Entry (Ventana1)
Num1Entry.pack (pady = 10)


Num2Label = tk.Label (text = 'Introduce el segundo numero.')
Num2Label.pack (pady = 10)
Num2Entry = tk.Entry (Ventana1)
Num2Entry.pack (pady = 10)

BotonSumar = tk.Button ( Ventana1 , text = 'SUMAR', )
BotonSumar.pack ()


Ventana1.mainloop()