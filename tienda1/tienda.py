import openpyxl
from pythonds3 import Queue,Deque
#Tienda#
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
        contador=1
    for j in mostrarInventario:
        print(contador,".",j)
        contador+=1
    return mostrarInventario

def interfazInventario(lista):
    for data in lista:
        

def rotarColaIzq(colaRotar):
    elemento = colaRotar.remove_front()
    colaRotar.add_rear(elemento)
    return colaRotar    

def rotarColaDer(colaRotar):
    elemento = colaRotar.remove_rear()
    colaRotar = add_front(elemento)
    return colaRotar
    
def crearColaInventario():
    colaComprar=Deque()
    auxInventario=[]
    auxInventario=mostrarInventario()
    for i in auxInventario:
        colaComprar.add_rear(i)
    return colaComprar

def comprar():
    inventario = mostrarInventario()
    eleccion = int(input("Articulo elegido\n"))
    if 1 <= eleccion <= len(inventario):  
        precio = inventario[eleccion-1][1]
        print(f"Precio: {precio}")
        return precio

    ##Pruebas
#inventario=mostrarInventario()
comprar()
