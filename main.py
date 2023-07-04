from draw import draw, gen_matrix
from settings import MAX_X, MAX_Y
from models import Chars


def update(chars) -> None:
    chars.step()


def start() -> None:
    chars = Chars(MAX_X)
    flag = False
    while True:
        if flag:
            update(chars)
        else:
            flag = True
        matrix = gen_matrix(MAX_X, MAX_Y, chars)
        draw(matrix)

if __name__ == "__main__":
    start()
