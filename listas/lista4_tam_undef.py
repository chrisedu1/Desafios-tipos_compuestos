#Realizar la carga de valores enteros por teclado,
#almacenarlos en una lista.
lista = []
valor = int(input("ingrese valor(0 para finalizar): "))
while valor!=0:
 #Finalizar la carga de enteros al ingresar el cero.
    lista.append(valor)
    valor = int(input("ingresar valor (0 para finalizar): "))
##mostrar el tamaño de la lista al final.
print("tamaño de la lista")
print(len(lista))