from random import randint
from typing import Self

from utils import Colors, gen_random_char
from settings import MAX_Y


class ColumnChar:
    def __init__(self, x: int, y: int, color: str = Colors.green):
        self.x = x
        self.y = y
        self.val = gen_random_char()
        # self.length = randint(2, MAX_Y)
        self.length = randint(2, 5)
        self.next = None
        self.color = color

    def step(self):
        if self.y < (MAX_Y - 2):
            self.y += 1
        else:
            self.y = 0
            self.val = gen_random_char()
            self.length = randint(2, MAX_Y)


class Chars:
    def __init__(self, count_char: int):
        self.max_size = count_char
        self.chars = [ColumnChar(x, 0) for x in range(count_char)]

        return

    def step(self):
        for ch in self.chars:
            l = ch.length
            c = 1
            while ch.next:
                ch.step()
                ch = ch.next
                c += 1
            ch.step()

            # tail constraint
            if c < l:
                ch.next = ColumnChar(ch.x, ch.y + 1)

    def __iter__(self) -> Self:
        self.counter = 0
        return self

    def __next__(self) -> ColumnChar:
        if (self.counter >= self.max_size):
            raise StopIteration

        response = self.chars[self.counter]
        self.counter += 1
        return response
