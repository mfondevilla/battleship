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

board_player = create_board (BOARD_SIZE, WATER)     ### crear tablero para jugador 
board_pc = create_board (BOARD_SIZE, WATER)         ### crear tablero para la máquina



### función de colocar barcos

### PARA EL .PY from variables.variables import SHIPS

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

board_player   = place_ships(board_player,   SHIPS, SHIP, WATER, seed=42)
board_pc = place_ships(board_pc, SHIPS, SHIP, WATER, seed=99)

print(f"Este es tu tablero, jugador:\n\n{board_player}")

###### print(f"Este es el tablero del pc:\n\n{board_pc}") Sólo para testear, no hay que printear