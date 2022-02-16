##Velocidad de la nave
#Muestra los segundos necesarios para pasar de 0 a 11200 metros por segundo, dada la aceleración de la nave en metros por segundo.

#Definimos variables de Velocidad inicial, Velocidad final y Aceleración
endVelocity = 11200
startVelocity = 0
acceleration = 9.8

#Usamos una variable llamada Time donde le daremos un valor igual a la formula t = Vf - Vi : a Remplazando los valores de la formula por las variables ya establecidas.
time = (endVelocity - startVelocity) / acceleration

#Usamos Print para mostrar el resultado de la operación
print("Tiempo para alcanzar la velocidad deseada = ", time)
