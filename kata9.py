#En esta ocavión nos han pedido crear una función para promediar el contenido de combustible de un cohete en 3 tanques
##Comenzamos realizando la funcion que contenga como argumentos el porcentaje de cada uno de los tanques de combustible
from math import degrees


totalowo= 1


def tcombustible(t1, t2, t3):
    tcomb = t1 + t2 + t3
    promedio = tcomb * 100 / 3
    print(f"""El promedio de lo lleno que están los tanques es {promedio}""")   
tcombustible(.10, .50, .60)

#Ahora para el ejercicio 2 nos piden crear un informe que cntenga varios argumentos específicos  
# Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno
##Comenzamos creando una funcion para asignar dinámicamente los tanques y el combustible requerido
def ttanques(**tanques):
    totalt = 0 
    for i in tanques.values():
        totalt= totalt + i;
    return(totalt)

##Ahora almacenamos el valor resultante en una variable global para usarla más tarde

totalcombustible= (ttanques(tanque1=10, tanque2=20, tanque3=30))

##Volveremos a crear otra variable para los valores dinámicos del tiempo de salida

def hora(*minutos):
    totalm = 0
    for i in minutos:
        totalm= totalm + i;
        return(totalm)

##Nuevamente vamos a almacenar el resultado en una variable para usarla en la funcion final

totalh= (hora(30, 20))
##Finalmente integramos el valor en la función siguiente, la que terminará siendo la estructura final

def informe(destino, tiempoD,):
    print(f"""
    La misión a {destino} empezará en {totalh} minutos.
    Durarando {tiempoD} horas.
    El combustible requerido es {totalcombustible} litros.
   """),
informe('Marte', 30)
