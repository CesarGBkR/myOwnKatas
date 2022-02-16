#En esta kata, nos piden que creemos un diccionario con algunas de las propiedades del planeta Marte
##Creamos el diccionario con los elemntos proporcionados

from cmath import polar
from unicodedata import name


planet = {
    'name': 'Mars',
    'moons': 2
}

##Ahora llamaremos a los valores asignados al diccionario

print(f"""El nombre del planeta es: {planet.get('name')}
Y tiene {planet['moons']} luna(s)""")

#Lo siguiente que nos piden es agregar un nuevo objeto al diccionario que sea igual a un subdiccionario con unos valores específicos
##Esta vez usamos [] para agregar el nuevo elemento, pero también podemos usar UPDATE

planet['circunferencia (km)']={
    'polar': 6752,
    'equatorial': 6792
}

##Ahora imprimimos el nombre junto a uno de los objetos del sudirectorio agregado

print(f"""El planeta {planet['name']} tiene una circunferencia polar de: {planet['circunferencia (km)']['polar']}
""")

#A partir de aquí comenzamos con la resolución del ejercicio 2
#Nos piden calcular el número total de lunas del sistema solar y el número promedio de lunas que tiene un planeta
##Empezamos estableciendo los datos apoyandonos de lo que nos entregan en el ejercicio

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

##Para el primer requisito del ejercicio, usaremos un ciclo FOR para asignar la suma de todas las lunas en una variable llamada TMOONS
##Para el segundo, volveremos a usar e ciclo FOR, pero esta vez haciendo que por cada KEY en el diccionario, nos agregue a un numero en el contador
##dicho número será almacenado en la variable PLANETS para despues usarlo para promediarlo junto al total de lunas
###Declaramos las variables

planets = 0
moons = 0

###Creamos el ciclo FOR

for i in planet_moons.values():
    moons= moons + i
    planets = planets  + 1

##Por último creamos una variable que almacene la operación para el promedio, usando las variables anteriores ya con los valores correspondientes
promedio = moons / planets

print(f"""El total de planetas en el sistema solar es: {planets} 
El de lunas es: {moons}
El promedio de lunas por planeta es: {promedio}""")