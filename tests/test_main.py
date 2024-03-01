"""
This module contains pytest test cases for testing the main module of the application.
It includes tests for various command executions and ensures that the application
handles input sequences and produces the expected output correctly.
"""
from unittest.mock import patch, MagicMock
import pytest
import main

@pytest.fixture(autouse=True)
def mock_process(monkeypatch):
    """
    Mock the Process class in multiprocessing to prevent actual process creation.
    This fixture automatically applies to all tests, ensuring that the application's
    multiprocessing behavior is simulated without creating separate processes.
    """
    mock_queue = MagicMock()
    queue_storage = []

    def mock_put(item):
        """Simulate putting an item into the queue."""
        queue_storage.append(item)

    def mock_get():
        """Simulate getting an item from the queue."""
        return queue_storage.pop(0) if queue_storage else ''

    def mock_empty():
        """Simulate checking if the queue is empty."""
        return not queue_storage

    mock_queue.put.side_effect = mock_put
    mock_queue.get.side_effect = mock_get
    mock_queue.empty.side_effect = mock_empty

    class MockProcess:
        """Mock version of the multiprocessing Process class."""
        def __init__(self, target, args, kwargs=None):
            self.target = target
            self.args = list(args)  # Convert tuple to list
            self.kwargs = kwargs if kwargs is not None else {}
            self.args[-1] = mock_queue

        def start(self):
            """Directly execute the target function, bypassing multiprocessing."""
            self.target(*self.args, **self.kwargs)

        def join(self):
            """Mock join method."""

    monkeypatch.setattr(main, "Process", MockProcess)
    monkeypatch.setattr(main, "Queue", lambda: mock_queue)

@pytest.mark.parametrize("input_sequence, expected_output", [
    (['add 2 3', 'exit'], "The result of 2 add 3 is equal to 5"),
    (['subtract 5 3', 'exit'], "The result of 5 subtract 3 is equal to 2"),
    (['multiply 3 3', 'exit'], "The result of 3 multiply 3 is equal to 9"),
    (['divide 8 2', 'exit'], "The result of 8 divide 2 is equal to 4"),
    (['divide 8 0', 'exit'], "Error: Division by zero."),
    (['unknown 2 3', 'exit'], "Unknown operation: unknown"),
    (['add a 3', 'exit'], "Invalid number input: a or 3 is not a valid number."),
    (['menu', 'exit'], "Available commands:"),
    (['exit'], "Exiting the application. Goodbye!")
])
def test_main_flow(input_sequence, expected_output, capsys):
    """
    Test the main flow of the program by simulating user input and verifying the output.
    """
    with patch('builtins.input', side_effect=input_sequence):
        main.main()
        captured = capsys.readouterr()
        assert expected_output in captured.out, (
            f"Expected '{expected_output}' not found in actual output."
        )

def test_invalid_command_format(capsys):
    """
    Test invalid command format handling by verifying the usage message is printed.
    """
    with patch('builtins.input', side_effect=['add 2', 'exit']):
        main.main()
        captured = capsys.readouterr()
        assert "Usage: <command> <number1> <number2>" in captured.out, (
            "Expected usage message not found."
        )
