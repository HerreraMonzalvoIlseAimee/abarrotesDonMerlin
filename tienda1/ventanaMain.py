import openpyxl
import os
from customtkinter import *
from openpyxl import Workbook, load_workbook
from ventanaUsuario import ventanaRegistrar
from ventanaDUsr import menuUsuario
from listaUsuarios import diccioUsuarios
from listaUsuarios import verificarExcel
from PIL import Image

verificarExcel() #Verificar que exista el Excel con los usuarios

def ocultarContra(): # Muestra la contraseña en el menú/ Admin
    if entryPass1U.cget("show") == "":
        entryPass1U.configure(show="*")
        ocultarA.configure(text="👁‍")
    else:
        entryPass1U.configure(show="")
        ocultarA.configure(text="🔒")

def ocultarContraU(): # Muestra la contraseña en el menú/ Usuario
    if entryPassU.cget("show") == "":
        entryPassU.configure(show="*")
        ocultarU.configure(text="👁‍")
    else:
        entryPassU.configure(show="")
        ocultarU.configure(text="🔒")
      
def mostrarPantalla(pantalla): #Ver que pantalla mostrar
    labelFondo.pack_forget() #El .pack oculta las demás pantallas de la vista
    pantallaAdmin.pack_forget()
    pantallaUsuario.pack_forget()
    pantalla.pack(fill="both", expand=True) #Muetra el nuevo frame

def mensajeTemporal(texto, tiempo, a , b):
    mensaje = CTkLabel(raiz, text=texto, text_color="white", font=("Arial", 13))
    mensaje.place(relx=a,rely=b)

    #Se elimina el mensaje
    mensaje.after(tiempo, mensaje.destroy)
    

def loginAdmin():
    datosAdmin= []
    datosAdmin.append('Admin_790')
    datosAdmin.append('1450Contra')
    usuAdmin= entryAdmin.get() #Guarda lo que ingresas en el campo
    #print("Usuario:", usuAdmin)
    Contra = entryPass1U.get()
    #print("Contraseña:", Contra)
    if datosAdmin[0] == usuAdmin and datosAdmin[1] == Contra:
        mostrarPantalla(pantallaAdmin) #Mostrar ahora la pantalla admin
    else:
        print("Usuario o contraseña incorrecto")

import ventanaUsuario #Regresa los datos de registro

def loginUsuario():
    datosActualizados = diccioUsuarios()
    Usuario =entryUsrU.get()
    ContraU =entryPassU.get()

    if Usuario in datosActualizados:
        infoUsuario= datosActualizados[Usuario]
        if ContraU == infoUsuario["contraseña"]:
            print("Ingreso sesion exitosamente.")
            menuUsuario(raiz)
            raiz.withdraw()
        else:
            print("Contraseña incorrecta.")
            mensajeTemporal("Contraseña incorrecta.", 2000, 0.215, 0.66)
    else:
        mensajeTemporal("Contraseña incorrecta.", 2000, 0.215, 0.66)
 
    
#----Pantalla Principal----
raiz=CTk()
raiz.geometry("1280x720+300+150")  ##tamaño
raiz.title("**ABARROTES DON MERLIN**") ##Titulo
raiz.resizable(False,False) ##Que no cambie el tamaño
raiz.iconbitmap("frog.ico") ##icono

imagenFondo = Image.open("Fondo.jpg")
fondo = CTkImage(light_image=imagenFondo, size=(1280, 720))
labelFondo = CTkLabel(master=raiz, image=fondo, text="") # Sin texto
labelFondo.place(x=0, y=0, relwidth=1, relheight=1)

labelFondo.pack(fill="both", expand=True) #Empacar todo todo lo de la pantalla de logeo #Snap ITC

CTkLabel(raiz, text= "ABARROTES DON\nMERLIN", text_color="orange", bg_color="#0a4748",font=("Snap ITC", 60)).place(x=20,y=120)
CTkLabel(raiz, text= "BIENVENIDO  :)", text_color="white", bg_color="black",font=("Comic Sans MS",34)).place(x=120,y=10)
CTkLabel(raiz, text= "© 2025 Abarrotes Don Merlín. Todos los derechos reservados.", text_color="#818181", bg_color="black",font=("Helvetica",17)).place(x=430,y=692)
CTkLabel(raiz, text= "v.1.21.5", text_color="#818181", bg_color="black",font=("Helvetica",17)).place(x=13,y=565)



#--------------------Frame Usuarios--------------------

frameUser = CTkFrame(master=labelFondo, width=450, height=200, fg_color="#bcbcbc")
frameUser.place(x=120, y=300) #Ajusta la posicion en pantalla
frameUser.configure(border_width=7)

imagenUsuario = Image.open("Usuario.jpg")
fondoUsuario = CTkImage(light_image=imagenUsuario, size=(241, 88))
labelimagenUsuario = CTkLabel(master=labelFondo, image=fondoUsuario, text="")
labelimagenUsuario.place(relx=0.18, rely=0.35)

entryUsrU = CTkEntry(frameUser, placeholder_text="Nombre de Usuario")
entryUsrU.place(relx=0.34,rely=0.33)

entryPassU = CTkEntry(frameUser, placeholder_text="Contraseña", show="*")
entryPassU.place(relx=0.34,rely=0.53)

entryPassU.bind("<Return>", lambda event: loginUsuario()) # Con enter igual funcioné
botonIngU = CTkButton(frameUser,text="Ingresar",fg_color="#3159B6", command=lambda:loginUsuario())
botonIngU.place(relx=0.7,rely=0.8,anchor= "center")

#Para el boton de 👁
ocultarU = CTkButton(frameUser, text="👁‍",fg_color="#305CA8",font=("Bahnschrift",15), command=ocultarContraU, width=30)
ocultarU.place(relx=0.66,rely=0.53)

#Ventana para registrarse
botonRegistU = CTkButton(frameUser, text="Registrarse",fg_color="#3159B6", command=lambda:ventanaRegistrar(raiz))#lambda para que no se ejecute al empezar
botonRegistU.place(relx=0.3,rely=0.8,anchor= "center")

#--------------------Admin--------------------
entryAdmin = CTkEntry(raiz, placeholder_text="Administrador")
entryAdmin.place(relx=0.767,rely=0.164)

botonIngU = CTkButton(raiz,text="Ingresar",fg_color="#4a8788", command=loginAdmin, width=90)
botonIngU.place(relx=0.888,rely=0.215)

entryPass1U = CTkEntry(raiz, placeholder_text="Contraseña", show="*") #Que se vea solo ****
entryPass1U.place(relx=0.885,rely=0.164)

entryPass1U.bind("<Return>", lambda event: loginAdmin()) # Con enter igual funcioné

#Para el boton de 👁
ocultarA = CTkButton(raiz, text="👁‍",fg_color="#4a8788",font=("Bahnschrift",15), command=ocultarContra, width=30)
ocultarA.place(relx=0.967,rely=0.215)


#-------------------- Pantalla admin --------------------
pantallaAdmin = CTkFrame(master=raiz, fg_color="black")


#-------------------- Pantalla usuario --------------------
pantallaUsuario = CTkFrame(master=raiz, fg_color="black")
CTkLabel(pantallaUsuario, text= "HOLA", text_color="green", bg_color="red",font=("Arial",45)).place(x=145,y=15)


raiz.mainloop()
