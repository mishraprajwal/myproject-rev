"""
Test cases for the main module.
"""
from unittest.mock import patch
import pytest
import main

@pytest.mark.parametrize("input_sequence, expected_outputs", [
    (['add 2 3', 'exit'], ["The result of 2 add 3 is equal to 5"]),
    (['subtract 5 3', 'exit'], ["The result of 5 subtract 3 is equal to 2"]),
    (['multiply 3 3', 'exit'], ["The result of 3 multiply 3 is equal to 9"]),
    (['divide 8 2', 'exit'], ["The result of 8 divide 2 is equal to 4"]),
    (['divide 8 0', 'exit'], ["An error occurred: Cannot divide by zero."]),
    (['unknown 2 3', 'exit'], ["Unknown operation: unknown"]),
    (['add a 3', 'exit'], ["Invalid number input: a or 3 is not a valid number."]),
    (
        ['menu', 'exit'],
        [
            "Available commands:", 
            "add", 
            "subtract", 
            "multiply", 
            "divide",
            "menu (to display this menu)", 
            "exit (to exit the application)"
        ]
    ),
    (['exit'], ["Exiting the application. Goodbye!"])
])
def test_main_flow(input_sequence, expected_outputs):
    """
    Test the main flow of the program.
    """
    with patch('builtins.input', side_effect=input_sequence), \
            patch('builtins.print') as mock_print:
        main.main()

        actual_outputs = [call_arg for call in mock_print.call_args_list for call_arg in call[0]]

        for expected_output in expected_outputs:
            assert any(expected_output in actual_output for actual_output in actual_outputs), \
                f"Expected '{expected_output}' not found in actual outputs"

def test_invalid_command_format():
    """
    Test invalid command format handling.
    """
    with patch('builtins.input', side_effect=['add 2', 'exit']), \
            patch('builtins.print') as mock_print:
        main.main()
        mock_print.assert_any_call("Usage: <operation> <number1> <number2>")
