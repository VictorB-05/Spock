import random

import Interfaz


def juego(opcion):
    numero_aleatorio = random.randint(1, 5)
    rel = opcion.comparar(numero_aleatorio)
    if  rel == 1:
        Interfaz.resultado.set("Has ganado")
    elif rel == -1:
        Interfaz.resultado.set("Has perdido")
    else:
        Interfaz.resultado.set("Empate")


