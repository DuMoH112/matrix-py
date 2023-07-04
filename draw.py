import os
from time import sleep
from typing import List

from models import Chars
from utils import Colors


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def gen_matrix(x_length: int, y_length: int, chars: Chars) -> List[List[str]]:
    matrix = [[' ' for _ in range(x_length)] for _ in range(y_length)]

    for ch in chars:
        while ch.next:
            matrix[ch.y][ch.x] = ch.color + ch.val + Colors.endc
            # matrix[ch.y][ch.x] = ch.val
            ch = ch.next
        matrix[ch.y][ch.x] = ch.val

    return matrix


def draw(matrix: List[List[str]]) -> None:
    for row in matrix:
        print(' '.join(row))

    sleep(1)
    clear_console()

    return
