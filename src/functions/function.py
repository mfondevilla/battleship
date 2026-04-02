### importar variables desde "variables"

import sys
sys.path.append("..")  # sube una carpeta

from variables import variables


### importar 'numpy' y 'random'

import numpy as np
import random


### función de crear tablero

from variables.variables import BOARD_SIZE, WATER

def create_board (BOARD_SIZE, WATER):
    board = np.full((BOARD_SIZE, BOARD_SIZE), WATER)
    return board

#### board_player = create_board (BOARD_SIZE, WATER)     ### crear tablero para jugador 
#### board_pc = create_board (BOARD_SIZE, WATER)         ### crear tablero para la máquina



### función de colocar barcos

from variables.variables import SHIPS

def place_ships(board, SHIPS, SHIP, WATER, seed=None):
    np.random.seed(seed)
    size = board.shape[0]

    for ship_length, quantity in SHIPS.items():
        for _ in range(quantity):
            placed = False

            while not placed:
                # orientación: 0 = horizontal, 1 = vertical
                orientation = np.random.randint(0, 2)

                if orientation == 0:  # horizontal
                    row = np.random.randint(0, size)
                    col = np.random.randint(0, size - ship_length + 1)

                    # comprobar si cabe
                    if np.all(board[row, col:col + ship_length] == WATER):
                        board[row, col:col + ship_length] = SHIP
                        placed = True

                else:  # vertical
                    row = np.random.randint(0, size - ship_length + 1)
                    col = np.random.randint(0, size)

                    if np.all(board[row:row + ship_length, col] == WATER):
                        board[row:row + ship_length, col] = SHIP
                        placed = True

    return board

#### board_player   = place_ships(board_player,   SHIPS, SHIP, WATER, seed=42)
#### board_pc = place_ships(board_pc, SHIPS, SHIP, WATER, seed=99)

#### print(f"Este es tu tablero, jugador:\n\n{board_player}")

###### print(f"Este es el tablero del pc:\n\n{board_pc}") Sólo para testear, no hay que printear


### función de disparo

### PARA EL .PY from variables.variables import HIT, MISS, WATER, SHIP

def shot(tablero_barcos, tablero_disparos, SHIP, WATER, HIT, MISS):
    
    # pedimos coordenadas para hacerlo interactivo
    row = int(input("Elige fila (0-9): "))
    col = int(input("Elige columna (0-9): "))

    # comprobar si ya se ha disparado ahí
    if tablero_disparos[row, col] in [HIT, MISS]:
        print("Ya has disparado aquí, elige otra casilla.")
        return shot(tablero_barcos, tablero_disparos, SHIP, WATER, HIT, MISS)

    # comprobar si es tocado o agua
    if tablero_barcos[row, col] == SHIP:
        tablero_disparos[row, col] = HIT
        print("¡Tocado!")
    else:
        tablero_disparos[row, col] = MISS
        print("¡Agua!")

    return tablero_disparos


### función de disparo aleatorio del pc

### PARA EL .PY from variables.variables import HIT, MISS, WATER, SHIP

def random_shot(tablero_barcos, tablero_disparos, SHIP, WATER, HIT, MISS):
    
    while True:
        # elegir coordenadas aleatorias
        row = np.random.randint(0, tablero_barcos.shape[0])
        col = np.random.randint(0, tablero_barcos.shape[1])

        # comprobar si ya se ha disparado ahí
        if tablero_disparos[row, col] not in [HIT, MISS]:
            break

    # comprobar si es tocado o agua
    if tablero_barcos[row, col] == SHIP:
        tablero_disparos[row, col] = HIT
        print(f"¡El pc ha disparado en ({row}, {col}) y ha tocado!")
    else:
        tablero_disparos[row, col] = MISS
        print(f"¡El pc ha disparado en ({row}, {col}) y ha fallado!")

    return tablero_disparos

#### random_shot(board_player, tablero_disparos_pc, SHIP, WATER, HIT, MISS)
