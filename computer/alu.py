"""https://www.youtube.com/watch?v=1I5ZMmrOfnA&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye&index=6"""


from abc import ABC, abstractmethod
from typing import Optional


OVERFLOW = ""
ZERO = ""
NEGATIVE = ""


class AbstractALU(ABC):
    OP_CODES = dict()
    FLAGS = dict()

    def __init__(self) -> None:
        """Simulation of an Arithmetic Logic Unit (ALU).

        Takes two input bitstrings `a` and `b` as well as an operation code `c` that specifies the operation to run.
        Returns an output bitstring along with flag bits indicating opreation status and output properties such as
        overflow, zero and negative.
        """
        super().__init__()

    @abstractmethod
    def add(self, a: str, b: str):
        """Add two bit strings."""
        pass

    @abstractmethod
    def add_with_carry(self, a: str, b: str, carry: str):
        """Add two bit strings and a carry bit."""
        pass

    @abstractmethod
    def subtact(self, a: str, b: str):
        """Subtract bitstring `b` from bitstring `a`."""
        pass

    @abstractmethod
    def subtract_with_borrow(self, a: str, b: str, carry: str):
        """Subtract bitstring `b` from bitstring `a`. with borrow `carry`."""
        pass

    @abstractmethod
    def negate(self, a: str):
        """Negative the sign of a bitstring by subtracting it from zero."""
        pass

    @abstractmethod
    def increment(self, a: str):
        """Add 1 to a bitstring."""
        pass

    @abstractmethod
    def decrement(self, a: str):
        """Subtract 1 from a bitstring."""
        pass

    @abstractmethod
    def multiply(self, a: str, b: str):
        """Multiply together two bitstrings."""
        pass

    @abstractmethod
    def divide(self, a: str, b: str):
        """Divide bitstring `a` by bitstring `b`."""

    @abstractmethod
    def pass_through(self, a: str):
        """All bits of a bitstring are passed through without modification."""
        return a


class ALU8Bit(AbstractALU):
    OP_CODES = dict(
        
    )

    def __init__(self, precision: int = 8, op_code_bits: int = 4) -> None:
        self.precision = precision
        self.op_code_bits = op_code_bits

    def __call__(self, op_code: str, a: str, b: Optional[str] = "") -> str:
        flags = ()
        

    def add(self, a: str, b: str):
        """Add two """
        pass

    def add_with_carry(self, a: str, b: str):
        pass

    def subtact(self, a: str, b: str):
        pass

    def subtract_with_borrow(self, a: str, b: str):
        pass

    def negate(self, a: str):
        pass

    def increment(self, a: str):
        pass

    def decrement(self, a: str):
        pass

    def pass_through(self, a: str):
        return a

# Add
# Add with carry
# Subtract
# Subtract with borrow
# Negate
# Increment
# Decrement
# Pass through

