from computer.bits_and_bytes import Bit
from computer.gates import AND, OR, NOT, XOR, NAND


def test_and():
    assert AND(Bit(0), Bit(0)) == Bit(0)
    assert AND(Bit(0), Bit(1)) == Bit(0)
    assert AND(Bit(1), Bit(0)) == Bit(0)
    assert AND(Bit(1), Bit(1)) == Bit(1)


def test_or():
    assert OR(Bit(0), Bit(0)) == Bit(0)
    assert OR(Bit(0), Bit(1)) == Bit(1)
    assert OR(Bit(1), Bit(0)) == Bit(1)
    assert OR(Bit(1), Bit(1)) == Bit(1)


def test_not():
    assert NOT(Bit(0)) == Bit(1)
    assert NOT(Bit(1)) == Bit(0)


def test_xor():
    assert XOR(Bit(0), Bit(0)) == Bit(0)
    assert XOR(Bit(0), Bit(1)) == Bit(1)
    assert XOR(Bit(1), Bit(0)) == Bit(1)
    assert XOR(Bit(1), Bit(1)) == Bit(0)


def test_nand():
    assert NAND(Bit(0), Bit(0)) == Bit(1)
    assert NAND(Bit(0), Bit(1)) == Bit(1)
    assert NAND(Bit(1), Bit(0)) == Bit(1)
    assert NAND(Bit(1), Bit(1)) == Bit(0)
