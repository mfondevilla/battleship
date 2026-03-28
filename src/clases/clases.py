import numpy as np

dimension = 10
agua = " "

class Tablero:
    def __init__(self, jugador):
        self.jugador = jugador
        self.dimension = dimension
        self.tablero = np.full((dimension, dimension), agua)
        self.disparos = np.full((dimension, dimension), agua)
        
        
print(dimension)
    