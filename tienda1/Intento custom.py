from customtkinter import *
from ventanaUsuario import ventanaRegistrar
from ventanaDUsr import menuUsuario
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
    pantallaLogin.pack_forget() #El .pack oculta las demás pantallas de la vista
    pantallaAdmin.pack_forget()
    pantallaUsuario.pack_forget()
    pantalla.pack(fill="both", expand=True) #Muetra el nuevo frame
    

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
datos = ventanaUsuario.cuentas1
print(datos)

def loginUsuario(datos):
    Usuario =entryUsrU.get()
    ContraU =entryPassU.get()
    print(Usuario)
    print(datos)
    if Usuario in datos:
        print("d")
        infoUsuario= datos[Usuario]
        if ContraU == infoUsuario["contraseña"]:
            print("Igreso sesion exitosamente.")
            print("{Usuario}, dinero: {infoUsuario['dinero']}")
            
            menuUsuario(raiz)
            raiz.withdraw()
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no registrado.")
 
    
#----Pantalla Principal----
raiz=CTk()
raiz.geometry("1280x720") ##tamaño
raiz.title("**ABARROTES DON MERLIN**") ##Titulo
raiz.resizable(False,False) ##Que no cambie el tamaño
raiz.configure(bg= "black") # Color

raiz.iconbitmap("frog.ico") ##icono

pantallaLogin = CTkFrame(master=raiz, fg_color="black")
pantallaLogin.pack(fill="both", expand=True) #Empacar todo todo lo de la pantalla de logeo

CTkLabel(raiz, text= "ABARROTES\nDON\nMERLIN", text_color="orange", bg_color="black",font=("Old English Text MT", 90)).place(x=610,y=40)
CTkLabel(raiz, text= "BIENVENIDO  :)", text_color="white", bg_color="black",font=("Papyrus",34)).place(x=120,y=10)


#--------------------Frame Usuarios--------------------
frameUser = CTkFrame(master=pantallaLogin, width=450, height=240, fg_color="grey")
frameUser.place(x=120, y=80) #Ajusta la posicion en pantalla
frameUser.configure(border_width=10)

CTkLabel(frameUser, text= "CLIENTE", text_color="purple", bg_color="grey",font=("Bahnschrift",45)).place(x=135,y=15)

CTkLabel(frameUser, text= "Usuario:", text_color="white", bg_color="grey",font=("Bahnschrift",25)).place(relx=0.15,rely=0.334)
entryUsrU = CTkEntry(frameUser, placeholder_text="Nombre de Usuario")
entryUsrU.place(relx=0.54,rely=0.35)
CTkLabel(frameUser, text= "Contraseña:", text_color="white", bg_color="grey",font=("Bahnschrift",25)).place(relx=0.15,rely=0.53)
entryPassU = CTkEntry(frameUser, placeholder_text="Contraseña", show="*")
entryPassU.place(relx=0.54,rely=0.55)

botonIngU = CTkButton(frameUser,text="Ingresar",fg_color="#3159B6", command=lambda:loginUsuario(datos))
botonIngU.place(relx=0.7,rely=0.8,anchor= "center")

#Para el boton de 👁
ocultarU = CTkButton(frameUser, text="👁‍",fg_color="#305CA8",font=("Bahnschrift",15), command=ocultarContraU, width=30)
ocultarU.place(relx=0.86,rely=0.55)

#Ventana para registrarse
botonRegistU = CTkButton(frameUser, text="Registrarse",fg_color="#3159B6", command=lambda:ventanaRegistrar(raiz))#lambda para que no se ejecute al empezar
botonRegistU.place(relx=0.3,rely=0.8,anchor= "center")

#--------------------Frame Admin--------------------
frameAdmin = CTkFrame(master=pantallaLogin , width=450, height=240, fg_color="grey")
frameAdmin.place(x=120, y=370) #Ajusta la posicion en pantalla
frameAdmin.configure(border_width=10)
CTkLabel(frameAdmin, text= "ADMIN", text_color="orange", bg_color="grey",font=("Bahnschrift",45)).place(x=145,y=15)

CTkLabel(frameAdmin, text= "Usuario:", text_color="white", bg_color="grey",font=("Bahnschrift",25)).place(relx=0.15,rely=0.334)
entryAdmin = CTkEntry(frameAdmin, placeholder_text="Nombre de usuario")
entryAdmin.place(relx=0.54,rely=0.35)
CTkLabel(frameAdmin, text= "Contraseña:", text_color="white", bg_color="grey",font=("Bahnschrift",25)).place(relx=0.15,rely=0.53)

botonIngU = CTkButton(frameAdmin,text="Ingresar",fg_color="#3159B6", command=loginAdmin)
botonIngU.place(relx=0.7,rely=0.8,anchor= "center")

entryPass1U = CTkEntry(frameAdmin, placeholder_text="Contraseña", show="*") #Que se vea solo ****
entryPass1U.place(relx=0.54,rely=0.55)

#Para el boton de 👁
ocultarA = CTkButton(frameAdmin, text="👁‍",fg_color="#305CA8",font=("Bahnschrift",15), command=ocultarContra, width=30)
ocultarA.place(relx=0.86,rely=0.55)



#-------------------- Pantalla admin --------------------
pantallaAdmin = CTkFrame(master=raiz, fg_color="black")

'''
#-------------------- Pantalla usuario --------------------
pantallaUsuario = CTkFrame(master=raiz, fg_color="black")
CTkLabel(pantallaUsuario, text= "HOLA",
         text_color="green",
         bg_color="red",font=("Arial",45)).place(x=145,y=15)
'''

raiz.mainloop()
