# JUEGO DE AHORCADO

import random

# Lista de palabras para el juego
palabras = ["python", "sistema", "juego", "algoritmo", "programa", "computadora", "teclado", "raton", "pantalla"]

# Función para seleccionar palabra secreta
def seleccionar_palabra():
    """Selecciona una palabra al azar de la lista de palabras usando random.choice()"""
    return random.choice(palabras)

# Función para dibujar el ahorcado
def dibujar_ahorcado(intentos_fallidos):
    """Dibuja el estado del ahorcado según el número de intentos fallidos"""
    if intentos_fallidos >= 1:
        print("  O  ")
    if intentos_fallidos >= 2:
        print("  |  ", end="")
    if intentos_fallidos >= 3:
        print(" /", end="")
    if intentos_fallidos >= 4:
        print(" \\")
    else:
        print()

    if intentos_fallidos >= 5:
        print(" /", end="")
    if intentos_fallidos >= 6:
        print(" \\")
    print()

# Función para indicar el estado del juego
def mostrar_estado(palabra_oculta, intentos_fallidos, letras_adivinadas):
    """Muestra el estado del juego, incluyendo la palabra oculta, los intentos fallidos y las letras adivinadas"""
    print("\nPalabra:", " ".join(palabra_oculta))
    print("Intentos fallidos:", intentos_fallidos)
    print("Letras adivinadas:", ", ".join(letras_adivinadas))
    dibujar_ahorcado(intentos_fallidos)

# Función principal para jugar al ahorcado
def jugar_ahorcado():
    """Función principal que controla el juego de ahorcado"""
    palabra_secreta = seleccionar_palabra()
    palabra_oculta = ["_"] * len(palabra_secreta)
    intentos_fallidos = 0
    letras_usadas = []

