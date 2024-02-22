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

def pytest_addoption(parser):
    """Add a command-line option to specify the number of test records."""
    parser.addoption("--num_records", action="store", default=5, type=int,
                     help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate tests dynamically based on the generated test data and command-line options."""
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames \
            and "expected" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("--num_records")
        # Generate test data and apply it to the tests
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("a,b,operation,expected", parameters)
