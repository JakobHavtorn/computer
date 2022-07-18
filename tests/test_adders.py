import pytest

from computer.adders import half_adder, full_adder, ripple_carry_adder_8bit
from computer.bits_and_bytes import Bit, BitString, Byte


@pytest.mark.parametrize(
    "a, b, sum, carry",
    [
        ("0", "0", "0", "0"),
        ("0", "1", "1", "0"),
        ("1", "0", "1", "0"),
        ("1", "1", "0", "1")
    ]
)
def test_half_adder(a, b, sum, carry):
    a, b, sum, carry = Bit(a), Bit(b), Bit(sum), Bit(carry)
    s, c = half_adder(a, b)
    assert s == sum
    assert c == carry


@pytest.mark.parametrize(
    "a, b, c, sum, carry",
    [
        ("0", "0", "0", "0", "0"),
        ("0", "1", "0", "1", "0"),
        ("1", "0", "0", "1", "0"),
        ("1", "1", "0", "0", "1"),
        ("0", "0", "1", "1", "0"),
        ("0", "1", "1", "0", "1"),
        ("1", "0", "1", "0", "1"),
        ("1", "1", "1", "1", "1")
    ]
)
def test_full_adder(a, b, c, sum, carry):
    a, b, c, sum, carry = Bit(a), Bit(b), Bit(c), Bit(sum), Bit(carry)
    s, c = full_adder(a, b, c)
    assert s == sum
    assert c == carry


@pytest.mark.parametrize(
    "a, b, sum, carry",
    [
        ("00000000", "00000000", "00000000", "0"),
        ("00000001", "00000001", "00000010", "0"),
        ("00000011", "00000001", "00000100", "0"),
        ("01111111", "00000001", "10000000", "0"),
        ("01111111", "01111111", "11111110", "0"),
        ("01111111", "10000000", "11111111", "0"),
        ("10000000", "10000000", "00000000", "1"),
        ("11111111", "10000000", "01111111", "1"),
    ]
)
def test_ripple_carry_adder(a, b, sum, carry):
    a, b, sum, carry = Byte(a), Byte(b), Byte(sum), Bit(carry)
    s, c = ripple_carry_adder_8bit(a, b)
    
    assert s == sum
    assert c == carry

