# conftest.py
import pytest
from calculator.calculator import Calculator
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

@pytest.fixture
def calculator():
    """Fixture to provide a Calculator instance for testing."""
    return Calculator()

@pytest.fixture
def add_command(calculator):
    """Fixture to provide an AddCommand instance for testing."""
    return AddCommand(calculator, 0, 0)

@pytest.fixture
def subtract_command(calculator):
    """Fixture to provide a SubtractCommand instance for testing."""
    return SubtractCommand(calculator, 0, 0)

@pytest.fixture
def multiply_command(calculator):
    """Fixture to provide a MultiplyCommand instance for testing."""
    return MultiplyCommand(calculator, 0, 0)

@pytest.fixture
def divide_command(calculator):
    """Fixture to provide a DivideCommand instance for testing."""
    return DivideCommand(calculator, 0, 0)
