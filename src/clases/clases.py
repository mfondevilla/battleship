import numpy as np
from ..variables.variables import (
    VALID_LETTERS, VALID_NUMBERS, BOARD_SIZE,
    SHIP, WATER, HIT, MISS, ERROR, REPEAT, SHIPS
)

class SalirJuego(Exception):
    """Se lanza cuando el usuario decide abandonar la partida."""
    pass


class Tablero:
    """
    Representa el tablero de un jugador en el juego Hundir la Flota

    Atributos:
    - player_id: identificador del jugador (máquina o jugador)
    - BOARD_SIZE: tamaño del tablero
    - tablero_barcos: matriz (array de numpy) donde se almacenan los barcos
    - tablero_disparos: matriz (array de numpy) donde se registran los disparos realizados
    """

    def __init__(self, player_id):
        self.player_id = player_id
        self.BOARD_SIZE = BOARD_SIZE
        self.tablero_barcos   = np.full((self.BOARD_SIZE, self.BOARD_SIZE), WATER)
        self.tablero_disparos = np.full((self.BOARD_SIZE, self.BOARD_SIZE), WATER)

    def place_ships(self):
        """
        Coloca los barcos aleatoriamente en el tablero.
        """
        direcciones = {
            "N": (-1,  0),
            "S": ( 1,  0),
            "E": ( 0,  1),
            "O": ( 0, -1)
        }

        for tamaño, cantidad in SHIPS.items():
            for _ in range(cantidad):
                colocado = False

                while not colocado:
                    fila      = np.random.randint(0, self.BOARD_SIZE)
                    columna   = np.random.randint(0, self.BOARD_SIZE)
                    direccion = np.random.choice(list(direcciones.keys()))
                    df, dc    = direcciones[direccion]
                    posiciones = []

                    for i in range(tamaño):
                        f = fila    + df * i
                        c = columna + dc * i
                        if not (0 <= f < self.BOARD_SIZE and 0 <= c < self.BOARD_SIZE):
                            break
                        posiciones.append((f, c))

                    if len(posiciones) == tamaño:
                        libre = True
                        for f, c in posiciones:
                            if self.tablero_barcos[f][c] != WATER:
                                libre = False
                                break
                        if libre:
                            for f, c in posiciones:
                                self.tablero_barcos[f][c] = SHIP
                            colocado = True

    def receive_shot(self, shot):
        """
        Procesa un disparo en una coordenada del tablero.

        Args:
            shot (tuple): Coordenada del disparo en formato (fila, columna).

        Returns:
            tuple: (resultado, mensaje)
        """
        fila, columna = shot

        if not (0 <= fila < self.BOARD_SIZE and 0 <= columna < self.BOARD_SIZE):
            return ERROR, "Disparo fuera de rango"

        if self.tablero_barcos[fila][columna] in (HIT, MISS):
            return REPEAT, "Ya disparado"

        if self.tablero_barcos[fila][columna] == WATER:
            self.tablero_barcos[fila][columna]   = MISS
            self.tablero_disparos[fila][columna] = MISS  # ← corregido
            return MISS, "Agua"

        if self.tablero_barcos[fila][columna] == SHIP:
            self.tablero_barcos[fila][columna]   = HIT
            self.tablero_disparos[fila][columna] = HIT   # ← corregido
            return HIT, "Tocado"

        return ERROR, "Valor desconocido"

    def display(self, tablero):
        """
        Muestra por pantalla el tablero proporcionado con formato.
        """
        print("  " + " ".join(VALID_LETTERS[:self.BOARD_SIZE]))
        for i in range(self.BOARD_SIZE):
            numero_fila = str(i + 1).rjust(2)
            fila        = " ".join(map(str, tablero[i]))
            print(f"{numero_fila} {fila}")

    def display_barcos(self):
        """Muestra el tablero con la posición de los barcos."""
        self.display(self.tablero_barcos)

    def display_disparos(self):
        """Muestra el tablero de disparos realizados."""
        self.display(self.tablero_disparos)