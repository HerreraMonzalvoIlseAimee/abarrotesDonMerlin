from customtkinter import *
from listaUsuarios import agregarUsuarios

def ventanaRegistrar(ventanaPadre):
    # Crea la ventana secundaria
    ventanaReg = CTkToplevel(ventanaPadre) #Crea ventana nueva
    ventanaReg.focus_force() # Se posiciona adelante de la otra ventana
    #ventanaReg.lift() # La eleva por encima de otras ventanas
    ventanaReg.grab_set() # Bloquea la ventana principal hasta que cierres esta
    ventanaReg.title("Registro de Usuario")
    ventanaReg.resizable(False,False) ##Que no cambie el tamaño
    ventanaReg.geometry("400x400+750+300")  
    ventanaReg.configure(fg_color ="black")
    
    def ocultarContraR():
        if entryContra.cget("show") == "": # Muestra la contraseña en el menú/ Registrar
            entryContra.configure(show="*")
            ocultarR.configure(text="👁‍")
        else:
            entryContra.configure(show="")
            ocultarR.configure(text="🔒")

    CTkLabel(ventanaReg, text="Registro de Usuario", font=("Arial", 20)).pack(pady=20)
    entryUsuario = CTkEntry(ventanaReg, placeholder_text= "Nombre de Usuario")
    entryUsuario.pack(pady=4)
    entryContra = CTkEntry(ventanaReg, placeholder_text= "Contraseña", show="*")
    entryContra.pack(pady=10)

    #Para el boton de 👁
    ocultarR = CTkButton(ventanaReg, text="👁‍",fg_color="#305CA8",font=("Bahnschrift",15), command=ocultarContraR, width=30)
    ocultarR.place(relx=0.70,rely=0.45)

    Regist = CTkButton(ventanaReg, text="Registrarse", command=lambda: registrarUsuario(entryUsuario, entryContra, ventanaReg))
    Regist.place(x=130, y=180)

    def registrarUsuario(entryUsuario, entryContra, ventanaReg):
        usuario = entryUsuario.get()
        contra = entryContra.get()
        agregarUsuarios(usuario, contra, ventanaReg)
