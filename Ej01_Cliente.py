import tkinter as tk

#EJEMPLO 1


Ventana1 = tk.Tk ()

Ventana1.title ("Nombre de usuario.")
Ventana1.geometry ('300x300')

LabelNombre = tk.Label (Ventana1, text = 'Nombre')
LabelNombre.pack ( pady = 10)

EntryNombre = tk.Entry (Ventana1)
EntryNombre.pack ()

LabelApellido = tk.Label (Ventana1, text = 'Apellido')
LabelApellido.pack ( pady = 10)

EntryApellido = tk.Entry (Ventana1)
EntryApellido.pack ()

Boton = tk.Button (Ventana1 , text = 'Saludar' )
Boton.pack ( pady = 10 )


def mostrar_texto():
    texto = EntryNombre.get() , '' , EntryApellido.get() 
    etiqueta_resultado.config(text=f"Escribiste: {texto}")



etiqueta_resultado = tk.Label(Ventana1, text= '', font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)



Ventana1.mainloop ()






