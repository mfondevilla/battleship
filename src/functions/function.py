# importar clases y variables

import numpy as np
from clases.clases import Tablero
from variables.variables import (
    VALID_LETTERS, VALID_NUMBERS, BOARD_SIZE,
    SHIP, WATER, HIT, MISS, ERROR, REPEAT
)


#### validar cordenada según VALID_LETTERS Y VALID_NUMBERS

def coordenada_valida(letra, numero):
    return letra.upper() in VALID_LETTERS and numero in VALID_NUMBERS




### conversión a matriz de la coordenada recibida

def parsear_coordenada(letra, numero):
    fila = numero - 1
    columna = VALID_LETTERS.index(letra.upper())
    return fila, columna




### solicitamos la coordenada para disparar en el tablero del oponente

def pedir_disparo():
    while True:
        try:
            letra  = input("Introduce letra (A-J): ").strip().upper()
            numero = int(input("Introduce número (1-10): ").strip())

            if coordenada_valida(letra, numero):
                return parsear_coordenada(letra, numero)
            else:
                print("Coordenada fuera de rango. Inténtalo de nuevo.")

        except ValueError:
            print("Entrada no válida. Introduce una letra y un número.")


### generamos una coordenada aleatoria válida para simular un disparo de la CPU

def disparo_cpu(tablero_obj):
    while True:
        fila    = np.random.randint(0, BOARD_SIZE)
        columna = np.random.randint(0, BOARD_SIZE)

        # solo dispara donde no haya disparado antes
        if tablero_obj.tablero_barcos[fila][columna] not in (HIT, MISS):
            return fila, columna


### comprobar si hay ganador o si seguimos jugando

def check_winner(tablero_obj):
    return not np.any(tablero_obj.tablero_barcos == SHIP)



### Gestiona el turno del jugador, solicita el disparo y llama al receive_shot del tablero de la CPU. Además,
#   Si ya ha disparado ahí, le pide que elija otra coordenada.
 
def turno_jugador(tablero_cpu):
    while True:
        shot = pedir_disparo()
        resultado, mensaje = tablero_cpu.receive_shot(shot)

        if resultado == REPEAT:
            print("Ya habías disparado ahí. Elige otra coordenada.")
        elif resultado == ERROR:
            print(f"Error inesperado: {mensaje}")
        else:
            print(mensaje)  # "Tocado" o "Agua"
            break


### Gestiona el turno de la CPU, y llama al receive_shot del tablero del jugador.

def turno_cpu(tablero_jugador):
    shot = disparo_cpu(tablero_jugador)
    resultado, mensaje = tablero_jugador.receive_shot(shot)
    fila, columna = shot

    # convertir índices de vuelta a formato legible
    letra  = VALID_LETTERS[columna]
    numero = fila + 1
    print(f"La CPU ha disparado en {letra}{numero}: {mensaje}")


### instrucciones del juego desde el menú
def mostrar_instrucciones():

    print("""
─────────────────────────────────────────
      INSTRUCCIONES - HUNDIR LA FLOTA
─────────────────────────────────────────
 Objetivo:
   Hundir todos los barcos de la CPU antes
   de que ella hunda los tuyos.

 Cómo jugar:
   - Introduce una letra (A-J) y un número
     (1-10) para indicar dónde disparas.
   - En cualquier momento puedes escribir
     'salir' cuando se pida la letra para
     abandonar la partida sin quedarte
     atrapada en la consola.

 Símbolos del tablero:
   O  = Barco (solo visible en tu tablero)
   X  = Tocado
   *  = Agua
   -  = Casilla sin disparar

 Barcos en partida:
   - 4 barcos de tamaño 1
   - 3 barcos de tamaño 2
   - 2 barcos de tamaño 3
   - 1 barco  de tamaño 4

 ¡Buena suerte!
─────────────────────────────────────────
    """)


### para el menú inicial y devolver la opción elegida

def mostrar_menu():
    while True:
        print("""
─────────────────────────────────────────
            HUNDIR LA FLOTA
─────────────────────────────────────────
  1. Nueva partida
  2. Instrucciones
  3. Salir

─────────────────────────────────────────
        """)

        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            return opcion
        elif opcion == "2":
            mostrar_instrucciones()
        elif opcion == "3":
            return opcion
        else:
            print("Opción no válida. Elige 1, 2 o 3.")


#### Para limpiar la pantalla cada vez que termine una ronda. Hay que llamarla en el .main 

import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")