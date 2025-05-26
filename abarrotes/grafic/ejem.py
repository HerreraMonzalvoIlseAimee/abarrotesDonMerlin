import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Crear un frame
marco = tk.Frame(ventana, bg="white", bd=2, relief="sunken")
marco.pack(pady=10)  # Usar pack para posicionar el frame en la ventana

# Agregar botones al marco
boton1 = tk.Button(marco, text="Botón 1")
boton1.pack(side="left", padx=10)
boton2 = tk.Button(marco, text="Botón 2")
boton2.pack(side="left", padx=10)

# Mostrar la ventana
ventana.mainloop()
