"""Classes that represent bits and bytes"""


from enum import Enum
from typing import Union
from typing_extensions import Self


class Bit():
    """One bit of information."""

    def __init__(self, state: Union[int, str]) -> None:
        state = str(state)
        assert len(state) == 1
        assert state in ["0", "1"]
        self.state = state

    def __bool__(self) -> bool:
        """The `bool` operator."""
        return self.state == "1"

    def __invert__(self) -> Self:
        """The ~ operator."""
        return Bit("0" if self.state == "1" else "1")

    def __or__(self, bit: Self) -> Self:
        """The `or` operator."""
        return self.state == "1" or bit.state == "1"

    def __and__(self, bit: Self) -> Self:
        """The `and` operator."""
        return self.state == "1" and bit.state == "1"

    def __eq__(self, bit: Self) -> bool:
        """The `==` operator."""
        if isinstance(bit, Bit):
            return self.state == bit.state

        return False

    def __repr__(self) -> str:
        return f"Bit({self.state})"


class BitString():
    """Some number of bits of information."""

    def __init__(self, bits: str) -> None:
        assert all(b in ["0", "1"] for b in bits)
        self._bits = list(bits)

    @property
    def bits(self):
        return "".join(self._bits)

    def __getitem__(self, index: int) -> Bit:
        return Bit(self._bits[index])

    def __setitem__(self, index: int, bit: Bit) -> None:
        self._bits[index] = bit.state

    def __eq__(self, bitstring: Self) -> bool:
        return all(b1 == b2 for b1, b2 in zip(self._bits, bitstring._bits))

    def __repr__(self):
        return f"BitString({self.bits})"


class Byte(BitString):
    """Eight bits of information."""

    def __init__(self, bits: int) -> None:
        super().__init__(bits)
        assert len(bits) == 8

    def __repr__(self):
        return f"Byte({self.bits})"
