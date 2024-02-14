"""Module to test the Calculator class functionality."""

import pytest
from calculator.calculator import Calculator  # Adjust the import path as necessary

@pytest.fixture
def calc():
    """Fixture to create a Calculator instance before each test."""
    Calculator.clear_history()  # Assuming clear_history is a class method to reset history
    return Calculator()

def test_add(calc):
    """Test the addition functionality ensures correct result."""
    assert calc.add(1, 2) == 3, "Addition of 1 and 2 should return 3"

def test_subtract(calc):
    """Test the subtraction functionality ensures correct result."""
    assert calc.subtract(5, 3) == 2, "Subtraction of 5 by 3 should return 2"

def test_multiply(calc):
    """Test the multiplication functionality ensures correct result."""
    assert calc.multiply(2, 3) == 6, "Multiplication of 2 by 3 should return 6"

def test_divide(calc):
    """Test the division functionality ensures correct result."""
    assert calc.divide(6, 2) == 3, "Division of 6 by 2 should return 3"

def test_divide_by_zero(calc):
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(1, 0)

def test_history_operations(calc):
    """Test that history captures the results of operations correctly."""
    calc.add(1, 2)
    calc.subtract(5, 3)
    calc.multiply(3, 2)
    calc.divide(8, 2)
    expected_results = [3, 2, 6, 4]
    assert calc.history == expected_results, "History should reflect the performed calculations"
