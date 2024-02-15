"""Module for testing the Calculator class.

This module contains a series of pytest tests that verify the functionality of
arithmetic operations (addition, subtraction, multiplication, division) in the Calculator class,
including handling division by zero and ensuring the calculation history works as expected.
"""

import pytest
from calculator import Calculator  # Adjust the import path as necessary

class TestCalculator:
    """Test suite for testing the Calculator class."""

    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Fixture to clear the calculation history before each test."""
        Calculator.clear_history()

    @pytest.mark.slow
    def test_addition(self):
        """Test that addition of two numbers works correctly."""
        assert Calculator.add(1, 2) == 3
        assert Calculator.get_last_calculation() == "Added 1 + 2 = 3"

    def test_subtraction(self):
        """Test that subtraction of two numbers works correctly."""
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.get_last_calculation() == "Subtracted 5 - 3 = 2"

    def test_multiplication(self):
        """Test that multiplication of two numbers works correctly."""
        assert Calculator.multiply(2, 3) == 6
        assert Calculator.get_last_calculation() == "Multiplied 2 * 3 = 6"

    @pytest.mark.slow
    def test_division(self):
        """Test that division of two numbers works correctly and handles decimal results."""
        assert Calculator.divide(10, 2) == 5
        assert Calculator.get_last_calculation() == "Divided 10 / 2 = 5.0"

    def test_division_by_zero(self):
        """Test that division by zero raises a ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            Calculator.divide(1, 0)

    def test_calculation_history(self):
        """Test storing and retrieving calculation history."""
        Calculator.clear_history()
        Calculator.add(1, 2)
        Calculator.subtract(5, 2)
        Calculator.multiply(2, 4)
        Calculator.divide(10, 2)
        expected_history = [
            "Added 1 + 2 = 3",
            "Subtracted 5 - 2 = 3",
            "Multiplied 2 * 4 = 8",
            "Divided 10 / 2 = 5.0"
        ]
        assert Calculator.history == expected_history, \
            "Calculation history does not match expected values"
        last_calculation = Calculator.get_last_calculation()
        assert last_calculation == expected_history[-1], \
            "Last calculation retrieved does not match expected value"
