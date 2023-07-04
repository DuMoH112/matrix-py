from random import randrange


class Colors:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

class Del(Exception):
    pass


def gen_random_char() -> str:
    return chr(randrange(33, 126))


def generate_random_string(length: int) -> str:
    return ' '.join([gen_random_char() for _ in range(length)])



def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in [0, 2, 3, 5]:
        for fg in range(30, 38):
            format = ';'.join([str(style), str(fg)])
            s1 = '\033[{color}m {color} \x1b[0m'.format(color=format)
            print(s1)
        print()
