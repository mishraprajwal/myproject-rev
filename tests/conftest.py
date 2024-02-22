"""
This module generates test data for testing Calculator class operations.
It uses the Faker library to create dynamic, randomized test cases for each
of the arithmetic operations supported by the Calculator, ensuring broad test coverage.
"""

from decimal import Decimal
from faker import Faker
from calculator import Calculator  # Adjust the import path as necessary

# Initialize Faker globally
fake = Faker()

def generate_test_data(num_records):
    """Generate test data using Faker for the specified number of records."""
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))
        # Randomly choose an operation
        operation = fake.random_element(elements=['add', 'subtract', 'multiply', 'divide'])
        # Ensure b is not zero for divide operation to prevent division by zero
        if operation == 'divide' and b == Decimal(0):
            b = Decimal(1)

        # Prepare the expected result based on the operation
        if operation == 'add':
            expected = Calculator.add(a, b)
        elif operation == 'subtract':
            expected = Calculator.subtract(a, b)
        elif operation == 'multiply':
            expected = Calculator.multiply(a, b)
        elif operation == 'divide':
            expected = Calculator.divide(a, b)

        yield a, b, operation, expected
