"""Random access memory

https://www.youtube.com/watch?v=fpnE6UAfbtU&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye&index=7
"""

import math

from typing import Tuple
from computer.bits_and_bytes import Bit, BitString, Byte
from computer.gates import AND, NOT, OR


class AndOrLatch():
    def __init__(self) -> None:
        """A 1-bit memory store using an and, or and not gate."""
        self.or_gate = OR
        self.and_gate = AND
        self.not_gate = NOT
        self.is_set = Bit(0)

    def read(self) -> Bit:
        return self.is_set

    def write(self, set: Bit, reset: Bit):
        set = self.or_gate(set, self.is_set)
        not_reset = self.not_gate(reset)
        self.is_set = self.and_gate(set, not_reset)

    def __repr__(self):
        return f"AndOrLatch(output={self.is_set})"


class Gate():
    def __init__(self) -> None:
        """Converts a data and write enable signal into a set and reset signal e.g. for an and/or latch."""
        self.not_gate = NOT
        self.and_gate_1 = AND
        self.and_gate_2 = AND

    def __call__(self, data: Bit, write_enable: Bit) -> Tuple[Bit, Bit]:
        set = self.and_gate_1(data, write_enable)
        reset = self.and_gate_2(self.not_gate(data), write_enable)
        return set, reset

    def __repr__(self):
        return f"Gate()"


class GatedLatch():
    def __init__(self) -> None:
        """A 1-bit memory store using a gated latch."""
        self.and_or_latch = AndOrLatch()
        self.gate = Gate()

    def read(self) -> Bit:
        return self.and_or_latch.read()

    def write(self, data: Bit, write_enable: Bit):
        set, reset = self.gate(data, write_enable)
        self.and_or_latch.write(set, reset)

    def __repr__(self) -> str:
        return f"GatedLatch({self.and_or_latch.is_set})"


class LinearRegister():
    def __init__(self) -> None:
        """A single `width` long linear register.
        
        These linear registers are inefficient in terms of wires needed.
        
        For a 256-bit linear register we need 513 wires in the linear construction;
        256 wires running to the data pins and 256 running to the outputs along with 1 write enable wire.
        """
        pass


class MatrixRegister():
    def __init__(self, width: int = 16) -> None:
        """A `width` by `width` matrix register of `width^2` latches storing `width^2` bits.

        It uses a number `width^2` of gated latches that each store a single 1-bit value.

        We read and write data by first selecting the address (pair of row and column wires) to access.
        This is achieved by using a MultiPlexer which converts from a memory address into something that selects
        the right row and column. The MultiPlexer needs as many bits and the associated memory registry uses as 
        its `width`.

        To write data we then input `data` via the data wire and turn on the `write_enable` wire.
        To read data we enable the `read_enable` wire and do not input any `data` on the data wire.

        Since there is a maximum of `width` rows (and columns), we can store the row address in log2(width) bits.
        For a 16-bit width register, row addresses are hence 4-bit. A full memory address including both the row
        and column address is thus 8-bit

        To convert from a memory address into something that selects the right row and column wire in the matrix 
        register we use a MultiPlexer. 

        For a 256-bit register (`width=16`) we only need 35 wires in the matrix construction; 
        1 data wire, 1 write_enable wrire, 1 read enable wire, 16 row wires and 16 column wires.
        """
        self.width = width
        self.latches = [[GatedLatch() for _ in range(width)] for _ in range(width)]
        self.and_gates_r = [[AND for _ in range(width)] for _ in range(width)]
        self.and_gates_w = [[AND for _ in range(width)] for _ in range(width)]

    def read(self, row: int, col: int, read_enable: Bit) -> Bit:
        """Read data from the register address at `(row, col)` indexed by a multiplexer."""
        selected = AND(row, col)
        read_enabled = AND(selected, read_enable)
        if read_enabled:
            return self.latches[row][col].read()
        return Bit(0)

    def write(self, row: int, col: int, data: Bit, write_enable: Bit) -> Bit:
        """Write `data` to the register address at `(row, col)` indexed by a MultiPlexer."""
        return self.latches[row][col].write(data, write_enable)

    def __repr__(self):
        return f"MatrixRegister(width={self.width})"


class MultiPlexer():
    def __init__(self, width: int = 16) -> None:
        """A multiplexer that converts binary addresses to column and row indexes into the register.
        
        You input a bitstring and the MultiPlexer returns the 
        
        You need to address the memory one row at a time. For that reason you need a column decoder to select the
        row that you want to access.

        If your memory width does not match you data bus width then you will need a multiplexer to load the memory
        contents onto the bus. If you want 8 bits of your 16 bits wide memory then you need a mux to select the
        high byte or low byte.

        The operation of the decoder and mux can be considered combined as they combine to allow you to access one
        block of memory (one data bus width block) from your memory grid.

        https://www.electronics-tutorials.ws/combination/comb_2.html
        https://www.javatpoint.com/multiplexer-digital-electronics
        https://www.youtube.com/watch?v=fpnE6UAfbtU&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=8

        Args:
            inputs (str): Binary string of `width` bits. 
            address (str): Binary string of `width` bits

        Returns:
            str: the binary value 
        """
        self.width = width
        self.address_bits = int(math.sqrt(width))

    def binary2int(self, binary: str):
        """Convert binary representation of integer as a string to an integer type."""
        return int(binary, 2)

    def select(self, address: BitString) -> int:
        """Converts a memory address to an interger wire index."""
        assert len(address) == self.address_bits
        idx = self.binary2int(address)
        return idx


class MemoryCell():
    def __init__(self, width: int = 16) -> None:
        """A unit of memory comprising a register and two multiplexers.

        one write enable wire
        one read enable wire
        one data wire
        one wire for each row
        one wire for each column
        and gate for row+column selection
        """
        self.row_multiplexer = MultiPlexer(width)
        self.col_multiplexer = MultiPlexer(width)
        self.register = MatrixRegister(width)  # width ^ 2 bits of memory

    def read(self, address: Byte, read_enable: str):
        row_address = address[:4]
        col_address = address[4:]
        row_idx = self.row_multiplexer.select(row_address)
        col_idx = self.col_multiplexer.select(col_address)
        return self.register.read(row_idx, col_idx, read_enable)

    def write(self, address: str, data: str, write_enable: str):
        row_address = address[:4]
        col_address = address[4:]
        row_idx = self.row_multiplexer.select(row_address)
        col_idx = self.col_multiplexer.select(col_address)
        return self.register.write(row_idx, col_idx, data, write_enable)


class SRAM():
    def __init__(self, n_registers: int = 16, register_width: int = 16, precision: int = 8) -> None:
        """A unit of Static Random Access Memory which uses latches
        
        A `width^2` by `n_registers` bit memory cell that can store `n_registers` bits at each of the 
        `width^2` addresses.
        """
        self.cells = dict()
        for address in range(n_registers):
            self.cells[address] = MemoryCell(register_width)

    def write(self, address: str, data: str, write_enable: str):
        """Write..."""
        pass
        # for cell in self.cells:
        #     cell.write(address, )

    def read(self, address: str, read_enable: str):
        """Read... """
        pass
