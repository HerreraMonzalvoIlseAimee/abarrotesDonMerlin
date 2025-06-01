#Tienda#
from customtkinter import *
from PIL import Image, ImageTk
from ventanaTienda import *
import openpyxl
def menuUsuario(ventanaPadre):
    ventanaUsr = CTkToplevel(ventanaPadre)
    ventanaUsr.geometry("1280x720") ##tamaño
    ventanaUsr.title("**COMPRAR: ABARROTES DON MERLIN**") ##Titulo
    ventanaUsr.resizable(True,True) ##redimensionar
    ventanaUsr.configure(fg_color= "#900C3F")

    ventanaUsr.grid_columnconfigure(0,weight=3)
    ventanaUsr.grid_rowconfigure(0,weight=3)

    ventanaUsr.iconbitmap("moneda.ico") ##icono

    #pantallaIngredientes = CTkFrame(master=ventanaTienda, fg_color="black")
    #pantallaIngredientes.pack(fill="both", expand=True) #Empacar todo todo lo de la pantalla de logeo


    CTkLabel(ventanaUsr, text= "ABARROTES DON MERLIN",
             text_color="#FFC300",
             bg_color="transparent",
             font=("Old English Text MT",60)).place(relx=0.035,rely=0.03)
    CTkLabel(ventanaUsr, text= "Polvos, aguas, esencias y más :)",
             text_color="white",
             bg_color="transparent",
             font=("Papyrus",28)).place(relx=0.6,rely=0.88)

    ##Menu de ingredientes

    menu = CTkFrame(master = ventanaUsr,
                    width=1500,
                    height=1000,
                    fg_color="#6e2145")
    menu.grid(row=0,column=0,sticky="ew")
    menu.grid_columnconfigure((1,2,3,4,5),weight=1)
    menu.grid_rowconfigure((1,2,3,4,5),weight=1)

    ingredientesMenu=CTkButton(menu, text="ver usuario",
                            font=("Old English Text MT",30),
                            fg_color="#c66509",
                            width=100,
                            height=50)
    ingredientesMenu.grid(row=2,column=1, padx=100, pady=40,sticky="ew")
    crearPocionesMenu=CTkButton(menu, text="crear pociones",
                            font=("Old English Text MT",30),
                            fg_color="#c66509",
                            width=100,
                            height=50)
    crearPocionesMenu.grid(row=3, column=1, padx=100,pady=40,sticky="ew")
    comprarMenu=CTkButton(menu, text="comprar ingredientes",
                            font=("Old English Text MT",30),
                            fg_color="#c66509",
                            width=100,
                            height=50,
                            command=lambda: [mostrarVentana(ventanaUsr),ventanaUsr.withdraw()])
    comprarMenu.grid(row=4, column=1, padx=100,pady=40,sticky="ew")
    sugerenciasMenu=CTkButton(menu, text="mandar sugerencias",
                            font=("Old English Text MT",30),
                            fg_color="#c66509",
                            width=100,
                            height=50)
    sugerenciasMenu.grid(row=5, column=1, padx=100,pady=40,sticky="ew")
    imagen_pil = Image.open("pez1.png")
    imagen_ctk = CTkImage(light_image=imagen_pil, size=(450, 400)) #Tamaño
    label_imagen = CTkLabel(master=ventanaUsr,bg_color="transparent", image=imagen_ctk, text="") #Texto vacío para que solo se vea la imagen
    label_imagen.grid(row=0, column=0,sticky="e")
    #Comportamiento al cerrar:
    ventanaUsr.protocol("WM_DELETE_WINDOW", lambda: [ventanaUsr.destroy(),ventanaPadre.deiconify()])

   # ventanaUsr.mainloop()
    return ventanaUsr
