# pylint: disable=redefined-outer-name
"""Module for testing the command implementations in the Calculator application.

This includes tests for addition, subtraction, multiplication, and division commands,
verifying correct execution and handling of division by zero.
"""

import pytest
from calculator.calculator import Calculator
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

@pytest.fixture
def calculator():
    """Provides a Calculator instance for use in tests."""
    return Calculator()

def test_add_command(calculator):
    """Test that the AddCommand correctly adds two numbers."""
    command = AddCommand(calculator, 5, 3)
    assert command.execute() == 8, "Expected addition result to be 8"

def test_subtract_command(calculator):
    """Test that the SubtractCommand correctly subtracts two numbers."""
    command = SubtractCommand(calculator, 5, 3)
    assert command.execute() == 2, "Expected subtraction result to be 2"

def test_multiply_command(calculator):
    """Test that the MultiplyCommand correctly multiplies two numbers."""
    command = MultiplyCommand(calculator, 5, 3)
    assert command.execute() == 15, "Expected multiplication result to be 15"

def test_divide_command(calculator):
    """Test that the DivideCommand correctly divides two numbers."""
    command = DivideCommand(calculator, 6, 3)
    assert command.execute() == 2, "Expected division result to be 2"

def test_divide_command_zero_division(calculator):
    """Test DivideCommand raises ValueError when dividing by zero."""
    command = DivideCommand(calculator, 1, 0)
    with pytest.raises(ValueError) as exc_info:
        command.execute()
    assert str(exc_info.value) == "Cannot divide by zero.", \
        "Expected ValueError when attempting to divide by zero"
