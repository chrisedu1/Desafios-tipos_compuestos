#diccionario que permite almacenar 5 articulos
# Utilizar como clave el nombre de los productos y como valor el precio
def cargar():
    productos={}
    for x in range(5):
        nombre=input("Ingrese el nombre del producto: ")
        precio=int(input("Ingrese el precio: "))
        productos[nombre]=precio
    return productos
#imprime todo el diccionario
def imprimir(productos):
    print("Listado de todos los articulos")
    for nombre in productos:
        print(nombre, productos[nombre])
 
#Imprime los articulos con precio superio a 100       
def imprimir_mayor100(productos):
    print("Listado de articulos con precios mayores a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)
#bloque principal     
productos=cargar()
imprimir(productos)
imprimir_mayor100(productos)