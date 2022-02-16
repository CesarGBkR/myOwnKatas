## En este ejercicio usaremos los métodos aprendidos para resolver los problemas planteados

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C""" 

#El primer ejercicio nos pide que separemos el string dentro de la variable Text por oraciones para trabajer con su contenido, usarémos el metordo .split() sin argumentos para resolverlo

oraciones = text.split()

print(oraciones)

#El siguiente ejercicio nos pide que la salida de nuestro código nos diga si la oración contiene un hecho
##Definimos los parametros que seleccionaremos como hecho = temperature
###Ahora harémos un ciclo For para revisar todos los elementos de la lista en la variable Oraciones, donde si el elemento está dentro de los hechos, nos lo imprima.

for i in oraciones: 
    if i == "4cm": 
        print(i)
    elif i == "127":
        print(i)
    elif i == "year.":
        print(i)
    elif i == "C":
        i = "Celcius"
        print(i)

#Ahora vamos a practicar como darle formato a nuestras cadenas
#Los datos que menajaremos serán

nombre = "Ganímides"
gravedad = 0.00143 # in kms
planeta = "Marte"
gravedadm = gravedad * 1000 

#
title = f"Gravedad el planeta {nombre}"

# Creamos la plantilla
hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""

# Unión de ambas cadenas
template = f"""{title.title()} 
{hechos} 
""" 
print(hechos)

# Nuevos datos muestra
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

# Comprobamos la plantilla
print(hechos)

new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))