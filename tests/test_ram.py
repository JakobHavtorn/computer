import pytest
from computer.bits_and_bytes import Bit

from computer.ram import AndOrLatch, GatedLatch, MatrixRegister


@pytest.mark.parametrize(
    "set, reset, initial_state, expected_state",
    [
        ("0", "0", "0", "0"),  # set and reset off, output off
        ("0", "0", "1", "1"),  # set and reset off, output on
        ("1", "0", "0", "1"),  # set on
        ("1", "1", "0", "0"),  # reset with set on
        ("0", "1", "0", "0"),  # reset with set off
    ]
)
def test_and_or_latch(set, reset, initial_state, expected_state):
    set, reset, initial_state, expected_state = Bit(set), Bit(reset), Bit(initial_state), Bit(expected_state)
    and_or_latch = AndOrLatch()

    and_or_latch.is_set = initial_state

    and_or_latch.write(set, reset)

    assert and_or_latch.read() == expected_state


@pytest.mark.parametrize(
    "data, write_enable, initial_state, expected_state",
    [
        ("0", "0", "0", "0"),  # data and enable off, output off
        ("0", "0", "1", "1"),  # data and enable off, output on
        ("1", "0", "0", "0"),  # data on and enable off, output off
        ("1", "1", "0", "1"),  # data and enable on, output on
        ("1", "1", "1", "1"),  # data and enable on, output already on remains on
        ("0", "1", "1", "0"),  # data off and enable on, output turns off
    ]
)
def test_gated_latch(data, write_enable, initial_state, expected_state):
    data, write_enable, initial_state, expected_state = Bit(data), Bit(write_enable), Bit(initial_state), Bit(expected_state)
    
    gated_latch = GatedLatch()
    gated_latch.and_or_latch.is_set = initial_state

    gated_latch.write(data, write_enable)

    assert gated_latch.read() == expected_state


@pytest.mark.parametrize(
    "data, read_enable, write_enable, expected_state",
    [
        ("0", "0", "0", "0"),  # data and read and write enable off
        ("0", "0", "1", "0"),  # data and read enable off, write enable on
        ("0", "1", "0", "0"),  # data and write enable off, read enable on
        ("0", "1", "1", "0"),  # data off, read and write enable on
        ("1", "0", "0", "0"),  # data on and read and write enable off
        ("1", "0", "1", "0"),  # data on and read enable off, write enable on
        ("1", "1", "0", "0"),  # data and read enable on, write enable off
        ("1", "1", "1", "1"),  # data and read and write enable on
    ]
)
def test_register(data, read_enable, write_enable, expected_state):
    data, read_enable, write_enable, expected_state = Bit(data), Bit(read_enable), Bit(write_enable), Bit(expected_state)
    
    register = MatrixRegister(width=16)
    
    # all start at zero
    for r in range(16):
        for c in range(16):
            assert register.read(r, c, read_enable=Bit(1)) == Bit(0)

    register.write(0, 0, data, write_enable)

    if read_enable and write_enable:
        assert register.read(0, 0, read_enable) == data
    else:
        assert register.read(0, 0, read_enable) == Bit(0)