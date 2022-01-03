
from typing import Optional


OVERFLOW = 


class ALU():
    OP_CODES = dict(
        
    )

    def __init__(self, precision: int = 8, op_code_bits: int = 4) -> None:
        self.precision = precision
        self.op_code_bits = op_code_bits

    def __call__(self, op_code: str, a: str, b: Optional[str] = "") -> str:
        flags = ()
        

    def add(self, a: str, b: str):
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

