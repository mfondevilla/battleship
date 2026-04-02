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