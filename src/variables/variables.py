#variables/variables.py

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
