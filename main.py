from typing import List

from draw import draw
from settings import MAX_X, MAX_Y
from models import Chars


def gen_matrix(x_length: int, y_length: int, chars: Chars) -> List[List[str]]:
    matrix = [[' ' for _ in range(x_length)] for _ in range(y_length)]
    for ch in chars.chars:
        matrix[ch.y][ch.x] = ch.val
        while ch.next:
            ch = ch.next            
            matrix[ch.y][ch.x] = ch.val

    return matrix


def update(chars: Chars):
    chars.step()

    return chars


def start():
    chars = Chars(5)
    while True:
        chars = update(chars)
        matrix = gen_matrix(MAX_X, MAX_Y, chars)
        draw(matrix)


start()
