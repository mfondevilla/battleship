# ── MAIN ───────────────────────────────────────────────────────────────────
import numpy as np
from src.clases.clases import Tablero
from src.functions.function import (
    mostrar_menu,
    mostrar_instrucciones,
    limpiar_pantalla,
    turno_jugador,
    turno_cpu,
    check_winner
)

jugador = Tablero("Jugador")
cpu     = Tablero("CPU")

opcion = mostrar_menu()

if opcion == "3":
    print("¡Hasta luego!")

elif opcion == "1":
    jugador.place_ships()
    cpu.place_ships()

    try:
        while True:

            # turno jugador
            limpiar_pantalla()
            print("\n─── TU TABLERO DE DISPAROS ───")
            jugador.display_disparos()

            print("\n─── TU TURNO ───")
            turno_jugador(cpu)

            if check_winner(cpu):
                print("\n¡Has ganado!")
                break

            # turno cpu
            print("\n─── TURNO DE LA CPU ───")
            turno_cpu(jugador)

            print("\n─── TU TABLERO TRAS EL DISPARO ───")
            jugador.display_barcos()

            if check_winner(jugador):
                print("\n¡Ha ganado la CPU!")
                break

    except SalirJuego:
        print("\nHas abandonado la partida. ¡Hasta luego!")
