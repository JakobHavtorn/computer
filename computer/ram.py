"""Random access memory"""

from computer.gates import AND, NOT, OR


class AndOrLatch():
    def __init__(self) -> None:
        """A 1-bit memory store using an and, or and not gate"""
        self.or_gate = OR
        self.and_gate = AND
        self.not_gate = NOT
        self.output = "0"

    def read(self):
        return self.output

    def write(self, set: str, reset: str):
        set = self.or_gate(set, self.output)
        not_reset = self.not_gate(reset)
        new_output = self.and_gate(set, not_reset)
        self.output = new_output

    def __repr__(self):
        return f"AndOrLatch(output={self.output})"


class Gate():
    def __init__(self) -> None:
        """A gate the converts a combined set and reset signal into a combined data and write enable signal"""
        self.not_gate = NOT
        self.and_gate_1 = AND
        self.and_gate_2 = AND

    def __call__(self, data: str, write_enable: str):
        set = self.and_gate_1(data, write_enable)
        reset = self.and_gate_2(self.not_gate(data), write_enable)
        return set, reset

    def __repr__(self):
        return f"Gate()"


class GatedLatch():
    def __init__(self) -> None:
        """A 1-bit memory store using a gated latch"""
        self.and_or_latch = AndOrLatch()
        self.gate = Gate()

    @property
    def output(self):
        return self.and_or_latch.output

    @output.setter
    def output(self, value: str):
        self.and_or_latch.output = value

    def read(self):
        return self.and_or_latch.output

    def write(self, data: str, write_enable: str):
        set, reset = self.gate(data, write_enable)
        self.and_or_latch.write(set, reset)


class Register():
    def __init__(self, width: int = 16) -> None:
        """A matrix register of gated latches that can store `width^2` 1-bit values"""
        import IPython; IPython.embed(using=False)
        self.width = width
        self.latches = [[GatedLatch() for _ in range(width)] for _ in range(width)]
        self.and_gates = [[AND for _ in range(width)] for _ in range(width)]

    def read(self, row: int, col: int, read_enable: str):
        """Read the register using a multiplexer to create the address"""
        
        return self.latches[row][col].output

    def write(self, row: int, col: int, data: str, write_enable: str, read_enable: str):
        """https://youtu.be/fpnE6UAfbtU?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&t=368"""
        write_eabnel = row and col and write_enable  # TODO row and col are ints so not true
        self.latches[row][col].write(data, write_enable)

    def __repr__(self):
        return f"Register(width={self.width})"


class MultiPlexer():
    def __init__(self, width: int = 16) -> None:
        """A multiplexer that converts binary addresses to column and row indexes into the register
        
        You need to address the memory one row at a time. For that reason you need a column decoder to select the
        row that you want to access.

        If your memory width does not match you data bus width then you will need a multiplexer to load the memory
        contents onto the bus. If you want 8 bits of your 16 bits wide memory then you need a mux to select the
        high byte or low byte.

        The operation of the decoder and mux can be considered combined as they combine to allow you to access one
        block of memory (one data bus width block) from your memory grid.

        Args:
            inputs (str): Binary string of `width` bits.
            address (str): Binary string of `width` bits

        Returns:
            str: the binary value 
        """
        # https://www.electronics-tutorials.ws/combination/comb_2.html
        # https://www.javatpoint.com/multiplexer-digital-electronics
        # https://www.youtube.com/watch?v=fpnE6UAfbtU&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=8
        

    def __call__(self, inputs: str, address: str):
        """[summary]

        Args:
            inputs (str): [description]
            address (str): [description]
        """
        return 


class MemoryCell():
    def __init__(self, n_registers: int = 16, width: int = 16) -> None:
        """A `width * n_registers` bit memory cell that can store   8 bits at each address (register)"""
        self.row_multiplexer = MultiPlexer(width)
        self.col_multiplexer = MultiPlexer(width)
        self.register = Register(width)
        # one write enable wire
        # one read enable wire
        # one data wire
        # one wire for each row
        # one wire for each column
        # and gate for row+column selection

    def read(self, address: str, read_enable: str):
        row_address = address[:4]
        col_address = address[4:]
        row_idx = self.row_multiplexer(row_address)
        col_idx = self.col_multiplexer(col_address)
        return self.register.read(row_idx, col_idx)

    def write(self, address: str, data: str, write_enable: str):
        row_address = address[:4]
        col_address = address[4:]
        row_idx = self.row_multiplexer(row_address)
        col_idx = self.col_multiplexer(col_address)
        return self.register.write(row_idx, col_idx, data, write_enable)


class SRAM():
    def __init__(self, n_cells: int = 16, n_registers: int = 16, register_width: int = 16, precision: int = 8) -> None:
        self.cells = dict()
        for address in range(n_cells):
            # address = int2binary(address, precision)
            self.cells[address] = MemoryCell(n_registers, register_width)

    def write(self, address: str, data: str, write_enable: str):
        for cell in self.cells:
            cell.write(address, )
