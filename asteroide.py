print("Así que un asteroide está cerca del planeta, ¿eh? \n¿A cuántos km/h va el asteroide?")
velocidad= input()

if int(velocidad) < 25:
    print("Bien, ahora dime, ¿Sus dimenciones son mayores a 25 metros?")
    print("Si                 No")
    dimenciones = input()
    if dimenciones == "No":
        print("No te preocupes, no es una amenza. Puede que veas un rayo de luz desde la tierra, ve a afuera, con suerte lo veas.")
    else:
        print("Estamos en problemas")
        print("¿El tamaño es mayor a 1000 metros?")
        print("Si                No")
        diosNosAbandona = input()
        if diosNosAbandona == "Si":
            print("Saludame a DiCaprio")
        else:
            print("Es mejor que evacuén a todos los de la zona de impacto")
else: 
    print("¡Uy!, sin importar el tamaño, esta velocidad merece una alerta.")

