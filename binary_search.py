#algoritmo de busqueda binaria: nos permite conseguir un elemento especifico en una secuencia ordenada

#antes vamos a implementar una busqueda ingenua (naive search: busqueda elemento por elemento) luego una busqueda binaria

import random
import time

#por cada indice el el rango de la longitud de la lista, si el elemento con tal indice en la lista es igual al objetivo de la busqueda, retorna el indice del elemento; sino retorna - 1 porque es un numero que no puede ser un indice
def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1 

#ahora implementando la busqueda binaria trabaja imaginando esta lista y sus indices
#mi_lista = [1, 3, 5, 10, 12]
# indices =  0  1  2  3   4

#print(busqueda_ingenua(mi_lista, 15))

#con la busqueda binaria (mucho mas eficiente cuando las listas son largas) vamos a eliminar la mitad de las opciones que nos quedan en cada una de las rondas, una condicion basica para hacerlo es que la lista sea ordenada de forma ascendente
def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None): #cuando damos un valor a los parametros en la definicion de una funcion significa que se los estamos dando por defecto
    if limite_inferior is None: #si el limite inferior no se especifico (entonces es el por defecto)
        limite_inferior = 0 #zero es el indice de inicio de la lista
    if limite_superior is None:#si el limite superior no se especifico (entonces es el por defecto)
        limite_superior = len(lista)-1 #la longitud de la lista - 1 es el ultimo elemento de la lista

    #si el intervalo entre lim sup y lim inf no es valido, retorna -1 (inidce inexistente)
    if limite_superior < limite_inferior:
        return -1

   
    #queremos obtener el indice intermedio en la mitad de la lista
    punto_medio = (limite_inferior + limite_superior) // 2

    #evaluamos el punto medio!
    #si el elemento con el indice del punto medio corresponde al objetivo de la busqueda, entonces retorna el indice del elemento; sino vamos a descartar la mitad de los elementos de la lista evaluando si el objetivo de la busqueda es menor o mayor del elemento correspondente al indice del punto medio y en estos casos volvemos a ejecutar la funcion misma en la que estamos (RECURSION) per con parametros diferentes, achicados con respeto a antes
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1) #aqui acichamos el limite superior al indice del punto medio menos uno porque la busqueda ahora puede iniciar de 0 hasta el punto medio (excluido) porque la condicion nos dice que el objetivo de la busqueda es menor del elemento con indice punto medio en la lista 
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)#aqui acichamos el limite inferior al indice del punto medio mas uno porque la busqueda ahora puede iniciar del punto medio (excluido) hasta limite superior porque la condicion nos dice que el objetivo de la busqueda es mayor del elemento con indice punto medio en la lista


if __name__ == '__main__': #esta es una forma precaucional: de esta forma el codigo no se ejecuta si lo estamos importando

    #creamos una lista ordenada de manera ascendente de 10000 numeros aleatorios
    tamano = 10000
    conjunto_inicial = set() #conjunto vacio

    #mientras la longitud del conjunto_inicial sea menor del tamano anade al conjunto_inicial un numero intero aleatorio en el rango especificado entre parentesis. cuando de alcance el tamano deseado, modifica el conjunto_inicial en una lista (metodo list) y con el metodo sorted ordenala de forma ascendente
    while len(conjunto_inicial) < tamano:
        conjunto_inicial.add(random.randint(-3*tamano, 3*tamano))

    lista_ordenada = sorted(list(conjunto_inicial))

    #medir el tiempo de busqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada: 
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos")


    #medir el tiempo de busqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada: 
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos")


