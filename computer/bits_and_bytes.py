"""Classes that represent bits and bytes"""


from enum import Enum


class BitState(Enum):
    ZERO_BIT = 0
    ONE_BIT = 1


class Bit():
    """One bit of information."""
    def __init__(self, state: BitState) -> None:
        assert state in BitState.__members__
        self.state = state

    def __bool__(self):
        return self.state == BitState.ONE_BIT


class BitString():
    pass


class Byte():
    """Eight bits of information."""

    def __init__(self, bits) -> None:
        pass
