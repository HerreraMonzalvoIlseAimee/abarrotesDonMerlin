#Tienda#
from customtkinter import *
from PIL import Image, ImageTk
import openpyxl
from pythonds3 import *

#------

def mostrarVentana(ventanaPadre):
    def rotarColaIzq(colaRotar):
        elemento = colaRotar.remove_front()
        colaRotar.add_rear(elemento)
        return colaRotar, elemento

    def rotarColaDer(colaRotar):
        elemento = colaRotar.remove_rear()
        colaRotar.add_front(elemento)
        return colaRotar,elemento
    
    def imprimirCola(miCola,instruccion):
        
        eliminarEtiquetas(frameCola)
        if instruccion=='d':
                _,valor=rotarColaDer(miCola)
        elif instruccion=='i':
                _,valor=rotarColaIzq(miCola)
        valorCola = CTkLabel(master=frameCola,
                             text=valor,
                             font=("Matura MT Script Capitals",25),text_color="#ee76ab")
        valorCola.grid(row=0, column=0,pady=8,sticky="ew")
        return miCola
        
    def crearColaInventario(auxInventario):
        colaComprar=Deque()
        #auxInventario=[]
        #auxInventario=mostrarInventario()
        for i in auxInventario:
            colaComprar.add_rear(i)
        return colaComprar

    def quicksortPrecios(inventario):  
        quicksortAux(inventario, 0, len(inventario)-1)
        return inventario

    def quicksortAux(lista, inicio, fin):
        if inicio < fin:
            pivote = particion(lista, inicio, fin)
            quicksortAux(lista, inicio, pivote-1)
            quicksortAux(lista, pivote+1, fin)

    def particion(lista, inicio, fin):
        pivote = lista[inicio]
        izquierda = inicio + 1
        derecha = fin

        bandera = False
        while not bandera:
            while izquierda <= derecha and lista[izquierda][1] <= pivote[1]:
                izquierda = izquierda + 1
            while derecha >= izquierda and lista[derecha][1] >= pivote[1]:
                derecha = derecha - 1
            if derecha < izquierda:
                bandera = True
            else:
                lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

        lista[inicio], lista[derecha] = lista[derecha], lista[inicio]
        return derecha

    def imprimirInventario(inventario,menu):
        fila=0
        for data in inventario:
            etiqueta = CTkLabel(master=menu, text=data[0],font=("Matura MT Script Capitals",25),text_color="#ee76ab" )
            etiqueta2 = CTkLabel(master=menu, text=data[1],font=("Matura MT Script Capitals",25),text_color="#ee76ab")
            etiqueta.grid(row=fila, column=0,padx=50)
            etiqueta2.grid(row=fila, column=1)
            fila+=1
    def eliminarEtiquetas(menu):
        for widget in menu.winfo_children():
            if isinstance(widget,CTkLabel):
                widget.destroy()
            
    def mostrarInventario():
        mostrarInventario=[]
        
        archivo=openpyxl.load_workbook("recetario.xlsx")
        
        ingredientes = archivo["Ingredientes"]
        
        fila=0
        for i in range(2, ingredientes.max_row):
            
            celda="A"+str(i)
            celda2="B"+str(i)
            
            valor=ingredientes[celda].value
            valor2=ingredientes[celda2].value
     
            mostrarInventario.append([valor,valor2])
        return mostrarInventario

    
    ventanaTienda = CTk()
    ventanaTienda.geometry("1300x720") ##tamaño
    ventanaTienda.title("**COMPRAR:") ##Titulo
    ventanaTienda.resizable(True,True) ##redimensionar
    ventanaTienda.configure(fg_color= "#d62957")

    ventanaTienda.grid_columnconfigure((1,2),weight=1)
    ventanaTienda.grid_rowconfigure((0),weight=1)

    ventanaTienda.iconbitmap("moneda.ico") ##icono

    #pantallaIngredientes = CTkFrame(master=ventanaTienda, fg_color="black")
    #pantallaIngredientes.pack(fill="both", expand=True) #Empacar todo todo lo de la pantalla de logeo

    
    tiendita = CTkLabel(ventanaTienda, text= "TIENDITA MAGIKA",
             text_color="#ffbfdb",
             bg_color="transparent",
             font=("Old English Text MT",50))
    tiendita.grid(row=0,column=1,padx=20,pady=5)
    
    ##Frame menu de ingredientes---------------------------------
    menu = CTkFrame(master = ventanaTienda,
                    width=550,
                    fg_color="#572e4f")
    menu.grid(row=0,column=1, padx=10,pady= 150,sticky="nsew")
    
    menu.grid_columnconfigure((1,2),weight=1)
    menu.grid_rowconfigure((1),weight=1)

    #Frame menu2---------------------------------
    menu2 = CTkFrame(master = ventanaTienda,
                    width=600,
                    fg_color="#8e7e9a")
    menu2.grid(row=0,column=2, padx=10, pady=30, sticky="nsew")

    menu.grid_columnconfigure((0),weight=1)
    menu2.grid_rowconfigure((1,2,3,4),weight=1)
    
    #Frame cola---------------------------------------------
    frameCola = CTkFrame(master=menu2,
                    height=25,
                    fg_color="#572e4f")
    frameCola.grid(column=0,row=1,padx=10,sticky="nsew")
  
    #Frame botones----------------------------------
    frameColaBut = CTkFrame(master=menu2,
                    height=30,
                    fg_color="#572e4f")
    frameColaBut.grid(column=0,row=2,pady=20,sticky="nsew")

    frameColaBut.grid_rowconfigure((0),weight=0)
    frameColaBut.grid_columnconfigure((1,2,3,4),weight=1)
    #--------------
    
    #mostrar el menu
    inventario = []
    inventario = mostrarInventario()
    imprimirInventario(inventario,menu)
    
    print(inventario)
    inventarioOrdenado=[]
    inventarioOrdenado=quicksortPrecios(inventario)
    colaInventario = crearColaInventario(inventarioOrdenado)
    #Botones ------------------------------------------
    
    ingredientesMenu=CTkButton(frameColaBut, text="Ordenar/$",
                            font=("Old English Text MT",30),
                            fg_color="#c66509",
                            height=25,
                            command= lambda: [quicksortPrecios(inventario),eliminarEtiquetas(menu), imprimirInventario(inventario,menu),ingredientesMenu.destroy()])
    ingredientesMenu.grid(row=0,column=2, padx=1,sticky="ew")
    
    
    rotarAbajo=CTkButton(frameColaBut, text="▽",
                            font=("Old English Text MT",30),
                            fg_color="#c66509",
                            height=25,
                            command = lambda: [imprimirCola(colaInventario,"i")])
    rotarAbajo.grid(row=0,column=1,padx=1,sticky="ew")
    
    rotarArriba=CTkButton(frameColaBut, text="△",
                            font=("Old English Text MT",30),
                            fg_color="#c66509",
                            height=25,
                            command = lambda: [imprimirCola(colaInventario,"d")])
    rotarArriba.grid(row=0,column=4,padx=1,sticky="ew")
    
    selecProducto=CTkButton(frameColaBut, text="Select",
                            font=("Old English Text MT",25),
                            fg_color="#c66509",
                            height=25)
    selecProducto.grid(row=0,column=3, padx=1,sticky="ew")
 
    #Comportamiento al cerrar:
    ventanaTienda.protocol("WM_DELETE_WINDOW", lambda: [ventanaTienda.destroy(),ventanaPadre.deiconify()])
    ventanaTienda.mainloop()
    return ventanaTienda


