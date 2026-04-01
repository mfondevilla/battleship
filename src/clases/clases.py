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

ERROR = "Error"
REPEAT = "Repeat"

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
        self.tablero_barcos = np.full((self.BOARD_SIZE, self.BOARD_SIZE), WATER)
        self.tablero_disparos = np.full((self.BOARD_SIZE, self.BOARD_SIZE), WATER)
        
    def place_ships(self):
        """
        Coloca los barcos aleatoriamente en el tablero.

        Para cada tipo de barco definido en SHIPS, genera posiciones
        aleatorias en una dirección (N, S, E, O), asegurando que:
            - el barco no se salga de los límites del tablero
            - no se solape con otros barcos ya colocados

        El proceso se repite hasta colocar correctamente todos los barcos.

        Modifica los tableros de barcos internamente
        """
        # direcciones posibles para colocar los barcos
        direcciones = {
            "N" : (-1, 0),
            "S" : (1, 0),
            "E" : (0, 1),
            "O" : (0, -1)
        }
        
        for cantidad, tamaño in SHIPS.items():
            
            # recorrer cada clave utilizando su rango
            for _ in range(cantidad):

                colocado = False

                while not colocado:
                    fila = np.random.randint(0, self.BOARD_SIZE)
                    columna = np.random.randint(0, self.BOARD_SIZE)
                    
                    # escoger dirección aleatoria del diccionario de direcciones
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

                    # comprobar que tiene el tamaño correcto
                    if len(posiciones) == tamaño:
                        
                        # comprobar que las coordenadas están libres antes de colocar el barco        
                        libre = True
                        for f, c in posiciones:
                            if self.tablero_barcos[f][c] != WATER:
                                libre = False
                                break
                        
                        # colocar el barco tras comprobar que están libres
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
                resultado (str): HIT, MISS, ERROR o REPEAT.
                mensaje (str): Descripción del resultado del disparo.
        """
        
        fila, columna = shot
        
        # comprobar que el disparo está dentro del tablero
        if not (0 <= fila < self.BOARD_SIZE and 0 <= columna < self.BOARD_SIZE):
            return ERROR, "Disparo fuera de rango"
        
        # comprobar que no se ha disparado anteriormente en esa coordenada
        if self.tablero_barcos[fila][columna] in (HIT, MISS):
            return REPEAT, "Ya disparado"
        
        # registrar disparo fallido
        if self.tablero_barcos[fila][columna] == WATER:
            self.tablero_barcos[fila][columna] = MISS
            return MISS, "Agua"
            
        # registrar disparo en barco
        if self.tablero_barcos[fila][columna] == SHIP:
            self.tablero_barcos[fila][columna] = HIT
            return HIT, "Tocado"
        
        # caso inesperado (valor no contemplado en el tablero)
        return ERROR, "Valor desconocido" 
            
    
    
    def display(self, tablero):
        """
        Muestra por pantalla el tablero proporcionado con formato.

        Incluye una cabecera con letras y filas numeradas.

        Este método es utilizado internamente por otros métodos de la clase
        (display_barcos y display_disparos) para evitar duplicar código.

        Args:
            tablero (np.ndarray): Matriz que representa el tablero a mostrar.

        """
        # cabecera del tablero con letras
        print("  " + " ".join(VALID_LETTERS[:self.BOARD_SIZE]))

        # filas del tablero con números a la izquierda
        for i in range(self.BOARD_SIZE):
            numero_fila = str(i + 1).rjust(2)
            fila = " ".join(map(str, tablero[i]))
            print(f"{numero_fila} {fila}")


    def display_barcos(self):
        """
        Muestra el tablero interno con la posición de los barcos.

        Utiliza el método display para formatear la salida.

        """
        self.display(self.tablero_barcos)


    def display_disparos(self):
        """
        Muestra el tablero de disparos realizados.

        Utiliza el método display para formatear la salida.

        """
        self.display(self.tablero_disparos)
        


    