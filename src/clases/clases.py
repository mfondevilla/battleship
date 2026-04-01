import numpy as np

seed_partida = 1
np.random.seed(seed_partida)

BOARD_SIZE = 10
WATER = "-"
SHIP = "O"
HIT = "X"
MISS = "*"
#validators
VALID_LETTERS = "ABCDEFGHIJ"
VALID_NUMBERS = list(range(1, BOARD_SIZE + 1))
SHIPS = {
    1 : 4,
    2 : 3,
    3 : 2,
    4 : 1
}

class Tablero:
    def __init__(self, player_id):
        self.player_id = player_id
        self.BOARD_SIZE = BOARD_SIZE
        self.tablero_barcos = np.full((self.BOARD_SIZE, self.BOARD_SIZE), WATER)
        self.tablero_disparos = np.full((self.BOARD_SIZE, self.BOARD_SIZE), WATER)
        
    def place_ships(self):
        direcciones = {
            "N" : (-1, 0),
            "S" : (1, 0),
            "E" : (0, 1),
            "O" : (0, -1)
        }
        for cantidad, tamaño in SHIPS.items():
            for _ in range(cantidad):

                colocado = False

                while not colocado:
                    fila = np.random.randint(0, self.BOARD_SIZE)
                    columna = np.random.randint(0, self.BOARD_SIZE)
                    
                    direccion = np.random.choice(list(direcciones.keys()))
                    df, dc = direcciones[direccion]
                    
                    posiciones = []

                    # generar todas las posiciones del barco
                    for i in range(tamaño):
                        f = fila + df * i
                        c = columna + dc * i

                        # comprobar que está dentro del tablero
                        if not (0 <= f < self.BOARD_SIZE and 0 <= c < self.BOARD_SIZE):
                            break

                        posiciones.append((f, c))

                    # comprobar que tiene el tamaño correcto (no se salió)
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

        return self.tablero_barcos
    
    def receive_shot(self, shot):
        fila, columna = shot
        
        if not (0 <= fila < self.BOARD_SIZE and 0 <= columna < self.BOARD_SIZE):
            return None, "Disparo fuera de rango"
        
        elif self.tablero_barcos[fila][columna] in (HIT, MISS):
            return None, "Ya disparado"
        
        elif self.tablero_barcos[fila][columna] == WATER:
            self.tablero_barcos[fila][columna] = MISS
            self.tablero_disparos[fila][columna] = MISS
            resultado = MISS, "Agua"
            
        elif self.tablero_barcos[fila][columna] == SHIP:
            self.tablero_barcos[fila][columna] = HIT
            self.tablero_disparos[fila][columna] = HIT
            resultado = HIT, "Tocado"
            
        
            
        return resultado
    
    def display(self, tablero):
        # cabecera con letras
        print("  " + " ".join(VALID_LETTERS[:self.BOARD_SIZE]))

        # filas con números
        for i in range(self.BOARD_SIZE):
            numero_fila = str(i + 1).rjust(2)
            fila = " ".join(tablero[i])
            print(f"{numero_fila} {fila}")


    def display_barcos(self):
        self.display(self.tablero_barcos)


    def display_disparos(self):
        self.display(self.tablero_disparos)
        


    