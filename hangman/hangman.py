import random
import string 

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(listaDePalabras):
    #seleccionar una palabra al azar de la lista de palabras validas
    palabra = random.choice(listaDePalabras) #la funcion choice nos permite coger una opcion al azar de una lista

    #la palabra no debe contener ningun caracter que no queramos obtener en nuestro juego(por ejemplio guion o espacio)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(listaDePalabras)

    return palabra.upper()
    
     
def ahorcado():

    print("============================")
    print("   Bienvenido(a) al juego!  ")
    print("============================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra) #set convierte la palabra a un conjunto (estructura de dato en Python, una colección no ordenada de objetos únicos). Ej: si la palabra por adivinar es python se tranformara en 'Python' = {'P', 'y', 't', 'h', 'o', 'n'} y si se escribiera por error Pythooon solo se almacenaria una o porque un conjunto no prevee repeticiones
    letras_adivinadas = set() #conjunto nuevo
    
    abecedario = set(string.ascii_uppercase) #esa funcion del modulo string nos va a retornar una lista con todas las letras del abecedario en mayuscula (no contiene enye)

    vidas = 7

    #mientras queden letras por adivinar y el contador de vidas sea mayor que zero...
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}") #el metodo join une todos los elementos de un conjunto o de una secuencia, transformandola en una string, con el caracter que especifiquemos antes entre los elementos. en este caso de un conjunto se convierte en string: ' '.join({'a', 'b', 'c'})  --> 'a b c'

        #creamos una variable para el estado actual de la palabra: 
        #para cada lera en la palabra , incluye esa letra si la letra ha sido adivinada, si no esta en el conjunto letras_adivinada pero si esta en la palabra significa que todavia no de ha adivinado en este caso agregamos un guion. EJ: H - L A
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra] #list comprehension(forma de escribir las lista en una sola linea especificando lo que queremos incluir en esta lista dando alguna condicion)

        #monstramos el estado de la ahorca
        print(vidas_diccionario_visual[vidas]) #el numero de la variable vida le indica al diccionario vidas_diccionario_visual cual clave coger y entonces cual valor (que es un dibujo) monstrar

        #monstramos el estado actual de la palabra
        print(f"Palabra: {' '.join(palabra_lista)}") #usamos el metodo join en la variable creada para el estaod actual de la palabra

        #como se va a escoger esta letra nueva

        letra_usuario = input("Escoge una letra: ").upper()

        #si la letra escogida por el usuario esta en abecedario pero no esta en el conjunto de letras adivinadas, se anade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #si la letra escogida por el usuario esta en las letras por adivinar de la palabra, elimina esta letra del conjunto de letras por adivinar y anade una nueva linea; si no, quita una vida de la variable vidas y monstra el mensaje "tu letra no esta en la palabra"
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra")
        
        #si la letra escogida por el usuario ya fue ingresada, monstra este mensaje
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. por favor escoge una letra nueva")
        
        #si ninguna de estas opciones es verdadera, significa que el caracter ingresado era falso
        else: 
            print("\nEsta letra no es valida!")

    #se llega a esta linea cuando se adivinan todas las letras de la palabra o cuando se agotan las vidas del jugador

    #si se agotan las vidas monstra la ahorca y el mensaje
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado! Perdiste! Lo lamento mucho! La palabra era: {palabra}")
    #si no, quieres decir que, segun la otra condicion del ciclo while,las letras por adivinar son menores de zero, entonces adivinaste la palabra, entonces monstra el mensaje
    else:
        print(f"Excelente! Adivinaste la palabra {palabra}!")


ahorcado()








