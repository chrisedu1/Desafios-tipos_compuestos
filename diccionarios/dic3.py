#App que permite crear un diccionario ingles/castellano
#la clave es la palabra en ingles y el valor es la apalbra en castellano
#func1 cargar el diccionario
def cargar():
    diccionario={}
    continua="s"
    while continua == "s":
        caste=input("Ingrese palabra en castellano: ")
        ing=input("Ingrese palabra en ingles: ")
        diccionario[ing]=caste
        continua=input("Quiere cargar otra palabra:[s/n]")
    return diccionario
#func2 Listado completo de los diccionario
def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])
#func3 ingresar por teclado una palabra en ingles y si existe en el diccionario
#devolver esa palabra en castellano
def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en ingles a consultar: ")
    if pal in diccionario:
        print("en castellano significa:", diccionario[pal])
#bloque principal    
diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)