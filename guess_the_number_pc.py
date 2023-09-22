#el ordenador adivina el numero que nosotros seleccionemos

import random


def adivina_el_numero_ordenador(x):  #x es el limite superior

    print("============================")
    print("   Bienvenido(a) al juego!  ")
    print("============================")
    print(f"Piensa en un numero entre 1 y {x} para que el ordenador intente adivinarlo!")
    
    limite_inferior = 1
    limite_superior = x

    respuesta = ""

    while respuesta != "c": #"c" quiere decir correcta
        #generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #tmb podria ser el limite_superior   
        
        #obtener respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa A. Si es muy baja, ingresa B. Si es correcta, ingresa C: ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1 #cambia el limite superior del intervalo bajandola de 1 porque el usuario dijo que la respuesta era demasiaso alta
        elif respuesta == "b":
            limite_inferior = prediccion + 1 #cambia el limite inferior del intervalo incrementandolo de 1 porque el usuario dijo que la respuesta era demasiado baja

    #print esta fuera del ciclo porque el ciclo dura hasta cuando respuesta != "c"
    print(f"Siii! El ordenadora adivino tu numero correctamente: {prediccion}")


adivina_el_numero_ordenador(10)



