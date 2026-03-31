

















### ÚLTIMO BUCLE DEL MAIN, PARA INTERCALAR ENTRE TURNOS

while True:

    # --- turno del jugador ---
    print("\nTu tablero de disparos:")
    print(tablero_disparos_player)
    shot(board_pc, tablero_disparos_player, SHIP, WATER, HIT, MISS)

    if check_winner(board_pc, SHIP):
        print("¡Has ganado!")
        break

    # --- turno del pc ---
    print("\nEl pc dispara...")
    random_shot(board_player, tablero_disparos_pc, SHIP, WATER, HIT, MISS)
    
    print("\nTu tablero tras el disparo del pc:")
    print(board_player)

    if check_winner(board_player, SHIP):
        print("¡Ha ganado el pc!")
        break