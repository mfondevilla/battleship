import numpy as np

from src.clases.clases import Tablero
from src.functions.function import (
    mostrar_menu,
    turno_jugador,
    turno_cpu,
    check_winner,
)

def jugar():
    print("Hola")
    opcion_elegida = mostrar_menu()
    jugador = Tablero("Jugador")
    cpu = Tablero("CPU")
    cpu.place_ships() # colocar los barcos random
    jugador.place_ships()
    
    if opcion_elegida == '1':
        while (True):
            #cpu.display_barcos() # test para disparar todos los barcos de cpu
                                  # es para hacer trampa y 
                                  # llegar al final de la partida + rapido
            print("Turno Jugador")

            turno_jugador(cpu) # jugador selecciona coordenadas para atacar tablero de cpu
            print("Tablero cpu")

            cpu.display_disparos()
            print("Turno CPU")

            turno_cpu(jugador)
            print("Tablero jugador")

            jugador.display_barcos()

            cpu_gana = check_winner(jugador)
            jugador_gana = check_winner(cpu)

            if (cpu_gana):
                print("Ha ganado CPU !")

                return False
            elif(jugador_gana):  
                print("Has ganado! Enhorabuena!")
                return False


    elif opcion_elegida == '3':
        return # se sale del juego
jugar()