from random import randrange
from settings import MAX_X
from utils import gen_random_char


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
        self.chars = [ColumnChar(randrange(0, MAX_X)) for _ in range(count_char)]

        return

    def step(self):
        for ch in self.chars:
            ch.step()