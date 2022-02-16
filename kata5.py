#En la Kata 5, en el primer ejercicio, requiere que realicemos un programa en el que nos calcule la distancia entre dos planetas
#Yo crearé un código interactivo para que sea dinámico en datos, haciendo que permitas medir la distancia entre los planetas que requieras
from math import floor

##Inciaremos con un saludo y una recolección de datos para las variables del primer y segundo planeta
print("""
Hola, bienvenido.
Aquí podrás calcular la distancia entre tus planetas favoritos.
""")
planeta1 = input("""
Ingresa la distancia en Km y sin puntos del primer planeta.
""")
planeta2 = input("""
Ahora ingresa la distancia del segundo planeta en el mismo formato.
""")

##Ahora haremos las debidas operaciones para sacar la distancia en km de los planetas, usaremos ABS para que no importe el orden en el que se ingresen los datos

distancia = abs(int(planeta1) - int(planeta2))

###Nuestro extra será calcular la distancia entre planetas entregada en kilometros, tambien en millas, para eso
###tomaremos los valores entregados en la operación a kilometros,  los multiplicaremos por 0.621

distanciam = distancia * 0.621

##Por último entregamos a la pantalla todos los valores
print(f"""La distancia en kilometros es: {distancia}""")
print(f"""La distancia en millas es: {floor(distanciam)}""")


#Esta solución la apliqué para el primer ejercicio y parece que aplica para el segundo