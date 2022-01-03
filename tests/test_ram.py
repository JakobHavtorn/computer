import pytest

from computer.ram import AndOrLatch, GatedLatch, Register


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
    and_or_latch = AndOrLatch()

    and_or_latch.output = initial_state
    
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
    gated_latch = GatedLatch()

    gated_latch.output = initial_state

    gated_latch.write(data, write_enable)

    assert gated_latch.read() == expected_state



def test_register():
    register = Register()
