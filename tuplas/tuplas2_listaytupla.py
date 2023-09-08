#Se define la tupla con 3 valores enteros
#Convertir la tupla a lista y viceversa, modificando sus valores.
fechatupla=(25, 12, 2016)
print("imprimimos primer tupla")
print(fechatupla)
#Se copia la tupla en una lista
fechalista=list(fechatupla)
print("imprimimos la lista que se le copio a la tupla anterior")
print(fechalista)
#Se modifica la lista
fechalista[0]=31
print("imprimimos las lista ya modificada")
print(fechalista)
#Se copia la lista modificada a una tupla.
fechatupla2=tuple(fechalista)
print("imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)