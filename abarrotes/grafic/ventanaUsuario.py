from tkinter import *
def crearSecundaria(ventanaPadre):
    # Crea la ventana secundaria
    ventanaUsuario = Toplevel()
    ventanaUsuario.geometry("1100x700")
    ventanaUsuario.config(bg= "black")
    ventanaUsuario.title("ABARROTES DON MERLíN")

    
    #Comportamiento al cerrar:
    ventanaUsuario.protocol("WM_DELETE_WINDOW", lambda: [ventanaUsuario.destroy(),ventanaPadre.deiconify()])
    return ventanaUsuario
