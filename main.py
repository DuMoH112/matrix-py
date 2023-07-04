from random import randrange
from typing import List

from draw import draw
from utils import *


X, Y = 10, 10


class ColumnChar:
    def __init__(self, x: int, y: int = 0, val: str = None):
        self.x = x
        self.y = y
        self.val = val if val else gen_random_char()
        self.next = None

    def step(self):
        self.next = ColumnChar(self.x, self.y + 1, gen_random_char())


class Chars:
    def __init__(self, count_char: int):
        self.max_size = count_char
        self.chars = [ColumnChar(randrange(0, X)) for _ in range(count_char)]

        return

    def step(self):
        for ch in self.chars:
            ch.step()


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
        matrix = gen_matrix(X, Y, chars)
        draw(matrix)


start()
