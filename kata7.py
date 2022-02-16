#Nos piden crear un programa donde solicitemos una lista de planetas usando el ciclo WHILE para posteriormente imprimir la lista
##Primero creamos las variables que nos servirán para almacenar datos durante nuestro ciclo WHILE

newPlanet = ""
planetas = []

##Ahor harémos un ciclo que agregue los valores que ingrese el usuario, el ciclo se cerrará hasta que escriba la palabra "done"

while newPlanet.lower() != "done":
    if newPlanet:
        planetas.append(newPlanet)
    newPlanet = input("""Agrega un planeta más a tu lista, si ya no tienes más por agregar, escribe 'done'
    """)

##Por último imprimiremos los cada uno de los valores de la  lista creada usando un ciclo FOR

for i in planetas:
    print(i)