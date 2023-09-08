#Funcion que solicita la carga del dia, mes, año
#se almacena en una tupla que retorna los datos ingresados.
def cargar_fecha():
    dd=int(input("Ingrese número de día: "))
    mm=int(input("Ingrese número de mes: "))
    aa=int(input("Ingrese número de año: "))
    return (dd, mm, aa)
#Recibe la tupla con la fecha y la muestra en pantalla.
def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")
#Bloque principal
fecha=cargar_fecha()
imprimir_fecha(fecha)
    