#Agenda la clave sera la fecha,
#permitir almacenar varias actividades para la misma fecha(hora y actividad)
#func1 cargar datos en la agenda
def cargar():
    agenda={}
    continua1="s"
    while continua1 == "s":
        fecha=input("Ingrese la fecha con formato dd/mm/aa: ")
        continua2="s"
        lista=[]
        while continua2=="s":
            hora=input("Ingrese la hora de la actividad con formato hh:mm: ")
            actividad=input("Ingrese la descripcion de la actividad: ")
            lista.append((hora,actividad))
            continua2=input("Ingresa otra actividad para la misma fecha[s/n]: ")
        agenda[fecha]=lista
        continua1=input("Ingresa otra fecha [s/n]: ")
    return agenda
#func 2Listado completo de la agenda
def imprimir(agenda):
    print("Listado completo de la agenda")
    for fecha in agenda:
        print("Para la fecha: ", fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
#func3 consulta de una fecha
def consulta_fecha(agenda):
    fecha=input("Ingrese la fecha que desea consultar: ")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No hay actividades agendadas para dicha fecha")
        
agenda=cargar()
imprimir(agenda)
consulta_fecha(agenda)