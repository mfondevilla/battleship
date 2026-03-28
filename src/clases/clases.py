import numpy as np

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
            for c in range(cantidad):
            
    
jugador = Tablero("Jugador")
maquina = Tablero("Maquina")
disparos = Tablero("Disparos")

jugador.colocar_barcos()
    