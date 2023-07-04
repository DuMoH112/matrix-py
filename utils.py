from random import randrange


class Del(Exception):
    pass


def gen_random_char() -> str:
    return chr(randrange(33, 126))


def generate_random_string(length: int) -> str:
    return ' '.join([gen_random_char() for _ in range(length)])
