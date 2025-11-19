#Actividad 15

import tkinter as tk

Ventana1 = tk.Tk ()
Ventana1.title ("Nombre de usuario.")
Ventana1.geometry ('500x300')


LabelNombre = tk.Label (Ventana1, text = 'Nombre')
LabelNombre.pack ( pady = 10)
EntryNombre = tk.Entry (Ventana1)
EntryNombre.pack ()

LabelApellido = tk.Label (Ventana1, text = 'Apellido')
LabelApellido.pack ( pady = 10)

EntryApellido = tk.Entry (Ventana1)
EntryApellido.pack ()



def mostrar_texto():
    
    Nombre = EntryNombre.get ()
    Apellido = EntryApellido.get()
    NomApe = Nombre + ' ' + Apellido
    etiqueta_resultado.config(text=f"Nombre Completo: {NomApe}")

etiqueta_resultado = tk.Button(Ventana1, text="Nombre", command=mostrar_texto)
etiqueta_resultado.pack(pady=10)

etiqueta_resultado = tk.Label(Ventana1, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)


Ventana1.mainloop ()


