"""Logic gates (implemented with transistors IRL)"""

from computer.bits_and_bytes import Bit


def AND(a: Bit, b: Bit) -> Bit:
    return a and b


def OR(a: Bit, b: Bit) -> Bit:
    return a or b


def NOT(a: Bit) -> Bit:
    return ~a


def XOR(a: Bit, b: Bit) -> Bit:
    c = AND(a, b)
    d = NOT(c)
    e = OR(a, b)
    return AND(d, e)


def NAND(a: Bit, b: Bit) -> Bit:
    return NOT(AND(a, b))
    return NOT(AND(a, b))
