#modos para concatenar cadenas de caracteres
#supongamos que queremos crear una cadena que diga:
#aprender a programar con _____

# organizacion = "freeCodeCamp"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f'Aprende a programar con {organizacion}')

# Mad Libs

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

madlib = f"Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)