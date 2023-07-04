import os
from time import sleep
from typing import List


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw(matrix: List[List[str]]) -> None:
    for row in matrix:
        print(' '.join(row))

    sleep(0.2)
    clear_console()

    return
