import random


def jugar():
    usuario = input("Elige una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijeras: \n").lower()
    ordenador = random.choice(['pi', 'pa', 'ti']) #funcion choice del modulo random que elige de forma casual un elemento en una lista

    if usuario == ordenador:
        return f'Empate! El ordenador escogio {ordenador}'
    
    if gano_el_jugador(usuario, ordenador): #si la funcion gano_el_jugador retorna true
        return f'Ganaste! El ordenador escogio {ordenador}'
    
    return f'Perdiste! El ordenador escogio {ordenador}'


def gano_el_jugador(jugador, oponente):
    # digamos que esta funcion tiene que retornar True si gana el jugador
    # el jugador gana en estos casos:
    # si escoge piedra: piedra gana a tijera (pi > ti)
    # si escoge tijera: tijera gana a papel (ti > pa)
    # si escoge papel: papel gana a piedra (pa > pi)

    if ((jugador == 'pi' and oponente == 'ti')
        or(jugador == 'ti' and oponente == 'pa')
        or(jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    

print(jugar())