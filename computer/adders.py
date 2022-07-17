"""Addition circuits

https://www.youtube.com/watch?v=1I5ZMmrOfnA&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye&index=6
"""


from computer.gates import AND, OR, XOR
from computer.configuration import PRECISION


# TODO Refactor to stateless classes?


def half_adder(a: str, b: str):
    """Add two bits together and returns the sum and carry bit.

    Max output is 2 i.e. sum=0, carry=1.

    ```
    a   b  sum carry
    0   0   0   0
    1   0   1   0
    0   1   1   0
    1   1   0   1
    ```
    """
    sum = XOR(a, b)
    carry = AND(a, b)
    return sum, carry


def full_adder(a: str, b: str, c: str):
    """Add three bits together and return the sum and carry bit.

    Max output is 3 i.e. sum=1, carry=1.

    ```
    a   b   c  sum carry
    0   0   0   0   0
    0   1   0   1   0
    0   0   1   1   0
    0   1   1   0   1
    1   0   0   1   0
    1   1   0   0   1
    1   0   1   0   1
    1   1   1   1   1
    ```
    """
    sum1, carry1 = half_adder(a, b)
    sum, carry2 = half_adder(sum1, c)
    carry = OR(carry1, carry2)
    return sum, carry


def ripple_carry_adder_8bit(a: str, b: str, precision: int = PRECISION):
    """Add two numbers represented as bit strings together and return the sum and carry bit"""
    # allocate memory for the sum and carry
    sum = ["0"] * precision
    carry = "0"
    # from right-most bit, call full-adder and carry the result forward to next bit
    for i in range(1, precision + 1):
        sum[-i], carry = full_adder(a[-i], b[-i], carry)
        print(i, sum[-i], carry)
    sum = "".join(sum)
    return sum, carry


def carry_look_ahead_adder():
    pass
