import pandas as pd
#rutas
path_productos = '../data/productos.csv'
path_ventas = '../data/ventas.csv'
#Cargar datos
productos = pd.read_csv(path_productos)
ventas = pd.read_csv(path_ventas)

#
print(ventas)