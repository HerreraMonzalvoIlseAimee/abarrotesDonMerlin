def quicksortPrecios(inventario):
    quicksortAux(inventario, 0, len(lista)-1)
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
