"""Logic gates (implemented with transistors IRL)"""


# TODO Maybe simulate a basic transistor to use for AND, OR and NOT?


def AND(a: str, b: str) -> str:
    return "1" if a == "1" and b == "1" else "0"


def OR(a: str, b: str) -> str:
    return "1" if a == "1" or b == "1" else "0"


def NOT(a: str) -> str:
    return "1" if a == "0" else "0"


def XOR(a: str, b: str) -> str:
    c = AND(a, b)
    d = NOT(c)
    e = OR(a, b)
    return AND(d, e)


def NAND(a: str, b: str) -> str:
    return NOT(AND(a, b))
