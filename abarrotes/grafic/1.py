from tkinter import *
from PIL import Image, ImageTk
raiz=Tk()
raiz.title("**ABARROTES DON MERLIN**") ##Titulo
raiz.resizable(True,True) ##redimensionar

raiz.iconbitmap("frog.ico") ##icono

raiz.geometry("800x400") ##tamaño
raiz.config(bg= "black")
Label(raiz, text= "ABARROTES\nDON\nMERLIN", fg="orange", bg="black",font=("Old English Text MT","34")).place(x=10,y=5)
Label(raiz, text= "BIENVENIDO\n:)", fg="white", bg="black",font=("Papyrus","34")).place(x=415,y=235)


            #Frame Usuarios
frameUser = Frame() 
frameUser.pack(side="right", anchor="n") # FUll: El frame se ajusta a la redimesion
##                  x/y     /omitirse
frameUser.config(bg ="grey")

frameUser.config(bd=10)

frameUser.config(relief="groove")

frameUser.config(width= "400",height = "200") ##tamaño frame

Label(frameUser, text= "CLIENTE", fg="purple", bg="grey",font=("Bahnschrift","25")).place(x=10,y=5)

botonIngU = Button(frameUser,text="Ingresar")
botonIngU.place(relx=0.5,rely=0.95,anchor= "center")

Label(frameUser, text= "Usuario:", fg="white", bg="grey",font=("Bahnschrift","15")).place(relx=0.1,rely=0.3)
entryUsrU = Entry(frameUser).place(relx=0.5,rely=0.35)


            #Frame Admin
frameAdmin = Frame() 
frameAdmin.pack(side="left", anchor="s") # FUll: El frame se ajusta a la redimesion
##                  x/y     /omitirse
frameAdmin.config(bg ="grey")

frameAdmin.config(bd=10)

frameAdmin.config(relief="groove")

frameAdmin.config(width= "400",height = "200") ##tamaño frame

Label(frameAdmin, text= "ADMIN", fg="orange", bg="grey",font=("Bahnschrift","25")).place(x=10,y=5)

botonIngU = Button(frameAdmin,text="Ingresar")
botonIngU.place(relx=0.5,rely=0.95,anchor= "center")

raiz.mainloop()
