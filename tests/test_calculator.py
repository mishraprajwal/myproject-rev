# pylint: disable=redefined-outer-name
"""Module for testing the Calculator class.

This module contains a series of pytest tests that verify the functionality of
arithmetic operations (addition, subtraction, multiplication, division) in the Calculator class,
including handling division by zero and ensuring the calculation history works as expected.
"""

import pytest
from calculator import Calculator  # Adjust the import path as necessary

@pytest.fixture(scope="class")
def calculator_instance():
    """Fixture to create a Calculator instance for use in all tests within this class."""
    calculator = Calculator()
    calculator.clear_history()
    return calculator

class TestCalculator:
    """Test suite for testing the Calculator class."""

    def test_addition(self, calculator_instance):
        """Test that addition of two numbers works correctly."""
        assert calculator_instance.add(1, 2) == 3
        assert calculator_instance.get_last_calculation() == "Added 1 + 2 = 3"

    def test_subtraction(self, calculator_instance):
        """Test that subtraction of two numbers works correctly."""
        assert calculator_instance.subtract(5, 3) == 2
        assert calculator_instance.get_last_calculation() == "Subtracted 5 - 3 = 2"

    def test_multiplication(self, calculator_instance):
        """Test that multiplication of two numbers works correctly."""
        assert calculator_instance.multiply(2, 3) == 6
        assert calculator_instance.get_last_calculation() == "Multiplied 2 * 3 = 6"

    @pytest.mark.slow
    def test_division(self, calculator_instance):
        """Test that division of two numbers works correctly and handles decimal results."""
        assert calculator_instance.divide(10, 2) == 5
        assert calculator_instance.get_last_calculation() == "Divided 10 / 2 = 5.0"

    def test_division_by_zero(self, calculator_instance):
        """Test that division by zero raises a ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            calculator_instance.divide(1, 0)

    def test_calculation_history(self, calculator_instance):
        """Test storing and retrieving calculation history."""
        calculator_instance.clear_history()  # Ensure history is clear at the start of this test
        calculator_instance.add(1, 2)
        calculator_instance.subtract(5, 2)
        calculator_instance.multiply(2, 4)
        calculator_instance.divide(10, 2)
        expected_history = [
            "Added 1 + 2 = 3",
            "Subtracted 5 - 2 = 3",
            "Multiplied 2 * 4 = 8",
            "Divided 10 / 2 = 5.0"
        ]
        assert calculator_instance.history == expected_history, \
            "Calculation history does not match expected values."
        last_calculation = calculator_instance.get_last_calculation()
        assert last_calculation == expected_history[-1], \
            "Last calculation retrieved does not match expected value."
