#el usuario va a adivnar un numero elegido por la computadora
#el juego le va a decir si es mayor, menor o igual al que elegio el ordenador

import random 


def adivina_el_numero(x): #x representa el numero maximo

    print("============================")
    print("   Bienvenido(a) al juego!  ")
    print("============================")
    print("Tu meta es adivinar el numero generado por el ordenador.")

    numero_aleatorio = random.randint(1, x) #funcion del modulo random que genera un numero intero aleatorio (1 es el limite inferior inclusive y x es el limite superior inclusive)

    prediccion = 0 #zero porque debe ser en cualquier caso diferente del numero_aleatorio (de 1 a x)

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeno")
        if prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeno")

    #print esta fuera del ciclo porque el ciclo dura hasta cuando prediccion != numero_aleatorio  
    print(f"Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente!")


adivina_el_numero(10)