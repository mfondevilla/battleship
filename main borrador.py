# ── MAIN ───────────────────────────────────────────────────────────────────
import numpy as np
from src.clases.clases import Tablero, SalirJuego
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

    partida_activa = True

    while partida_activa:
        try:
            # turno jugador
            limpiar_pantalla()
            print("\n─── EL TABLERO DE LA CPU ───")
            cpu.display_disparos()

            print("\n─── TU TURNO ───")
            turno_jugador(cpu)

            if check_winner(cpu):
                print("\n¡Has ganado!")
                partida_activa = False
                continue

            # turno cpu
            print("\n─── TURNO DE LA CPU ───")
            turno_cpu(jugador)

            print("\n─── TU TABLERO TRAS EL DISPARO ───")
            jugador.display_barcos()

            if check_winner(jugador):
                print("\n¡Ha ganado la CPU!")
                partida_activa = False

        except Exception as e:
            if type(e).__name__ == "SalirJuego":
                print("\nHas abandonado la partida. ¡Hasta luego!")
                partida_activa = False
            else:
                raise