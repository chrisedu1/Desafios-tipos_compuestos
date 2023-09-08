# programa que permite cargar un codigo de producto como clave
#Guardar para la clave el nombre del producto, su precio y cantidad en stock.
#Carga de datos en el diccionario
def cargar():
    productos={}
    continua="s"
    while continua == "s":
        codigo=int(input("Ingresa el codigo del producto: "))
        descripcion=input("Ingrese la descripcion: ")
        precio=float(input("Ingrese el precio: "))
        stock=int(input("Ingrese el stock actual: "))
        productos[codigo]=(descripcion, precio, stock)
        continua=input("Desea cargar otro producto [s/n]?")
    return productos
#Listado completo de productos
def imprimir(productos):
    print("Listado completo de productos:")
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])
#consulta de un producto por clave; mostrar el nombre, precio y stock.  
def consulta(productos):
    codigo=int(input("Ingrese el codigo del articulo a consultar: "))
    if codigo in productos:
        print(productos[codigo][0],productos[codigo][1],productos[codigo][2])
#Mostrar listado de productos con stock en cero.   
def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero: ")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])
#Boque principal
productos=cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)