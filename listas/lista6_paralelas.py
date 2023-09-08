#programa que permite cargar el nombre de 5 personas y sus edades.
nombres = [] 
edades = []
for x in range (5):
    #se raliza la carga de los nombres y edades mediante los input.
    nom = input("ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed=int(input("Ingrese la edad dedicha persona: "))
    edades.append(ed)
#se imprimen los datos cargados en el orden solicitado.  
print("nombre de las personas mayores de edad: ")
for x in range (5):
    if edades[x]>=18:
        print(nombres[x])