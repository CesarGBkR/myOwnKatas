#En este módulo nos solicitan crear una lista almacenada en una variable donde se alojen los 8 planetas.
##Crearemos la variable con los carácteres especificados

from tkinter import PROJECTING


planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupieter", "Saturno", "Urano", "Neptuno"]

##Mostramos la lista creada

print(planetas)

##Ahora nos piden agregar a Pluton a la lista, para esto usaremos .APPEND

planetas.append("Pluton")

##Mostramos la lista actualizada

print(planetas)

#Para el segundo ejercicio, nos piden crear una solicitud donde el usuario agregue el nombre de un planeta
##Usaremos input() para esto

pname=input("""
Hola, dime el nombre de un planeta, no olvides poner la prier letra en mayúscula
""")

#También nos solicita que busquemos el nombre en la lista
##Para esto usaremos INDEX() y un ciclo FOR para mostrar un mensaje en caso de que no se encuentre

for i in planetas:
    if i != pname:
        print(f"veo que no es {i}")
    elif i == pname:
        indexp = planetas.index(i) + 1
        print(f"Entonces es {i} y está en el index: {indexp}")
        print(f"""Además, los planetas que se encuentran más lejos del sol que el son {planetas[indexp: ]} """) ##Indicamos que planetas están más alejados del sol que el ingresado, usando slices de la variavle planetas con index asignado por la variable I del ciclo FOR, que es igual al valor ingresado
        break

