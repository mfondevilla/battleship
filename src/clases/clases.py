import numpy as np

seed_partida = 1
np.random.seed(seed_partida)

dimension = 10
agua = " "

barcos = {
    4 : 1,
    3 : 2,
    2 : 3,
    1 : 4
}

class Tablero:
    def __init__(self, jugador):
        self.jugador = jugador
        self.dimension = dimension
        self.tablero_barcos = np.full((dimension, dimension), agua)
        self.tablero_disparos = np.full((dimension, dimension), agua)
        
    def colocar_barcos(self):
        for cantidad, tamaño in barcos.items():
            for _ in range(cantidad):

                colocado = False

                while not colocado:
                    fila = np.random.randint(0, self.dimension)
                    columna = np.random.randint(0, self.dimension)

                    # comprobar que cabe horizontalmente
                    if columna + tamaño <= self.dimension:

                        # comprobar que no hay barcos ya colocados
                        libre = True
                        for i in range(tamaño):
                            if self.tablero_barcos[fila][columna + i] != agua:
                                libre = False
                                break

                        # si está libre, colocamos
                        if libre:
                            for i in range(tamaño):
                                self.tablero_barcos[fila][columna + i] = "O"
                            colocado = True

        return self.tablero_barcos


jugador = Tablero("Jugador")
maquina = Tablero("Maquina")
jugador.colocar_barcos() 
maquina.colocar_barcos()

print(jugador.tablero_barcos)

    