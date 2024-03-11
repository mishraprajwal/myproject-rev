"""Module docstring to satisfy pylint's missing-module-docstring warning."""
from unittest.mock import patch, MagicMock
import pytest
import main

@pytest.fixture(autouse=True)
def mock_process_queue(monkeypatch):
    """Mock multiprocessing's Process and Queue."""
    mock_queue = MagicMock()
    queue_storage = []

    def mock_put(item):
        queue_storage.append(item)

    def mock_get():
        return queue_storage.pop(0) if queue_storage else ''

    def mock_empty():
        return not queue_storage

    mock_queue.put.side_effect = mock_put
    mock_queue.get.side_effect = mock_get
    mock_queue.empty.side_effect = mock_empty

    def start_process_mock(target, args, kwargs):
        target(*args, **kwargs)

    process_mock = MagicMock()
    process_mock.side_effect = lambda *args, **kwargs: MagicMock(
        start=patch('multiprocessing.Process.start',
                    new=MagicMock(side_effect=lambda: start_process_mock(*args, **kwargs))),
        join=MagicMock())

    monkeypatch.setattr('multiprocessing.Process', process_mock)
    monkeypatch.setattr('multiprocessing.Queue', lambda: mock_queue)

@pytest.mark.parametrize("input_sequence, expected_output", [
    (['add 2 3', 'exit'], "The result of 2 add 3 is equal to 5"),
    (['subtract 5 3', 'exit'], "The result of 5 subtract 3 is equal to 2"),
    (['multiply 3 3', 'exit'], "The result of 3 multiply 3 is equal to 9"),
    (['divide 8 2', 'exit'], "The result of 8 divide 2 is equal to 4"),
    (['divide 8 0', 'exit'], "Error: Division by zero."),
    (['unknown 2 3', 'exit'], "Unknown operation: unknown"),
    (['add a 3', 'exit'], "Invalid number input: a or 3 is not a valid number."),
    (['menu', 'exit'], "Available commands:"),
    (['exit'], "Exiting the application. Goodbye!"),
])
def test_main_flow(input_sequence, expected_output, capsys):
    """Test the main flow of the application with various input sequences."""
    with patch('builtins.input', side_effect=input_sequence):
        main.main()
        captured = capsys.readouterr()
        assert expected_output in captured.out

def test_invalid_command_format(capsys):
    """Test the application's response to an invalid command format."""
    with patch('builtins.input', side_effect=['add 2', 'exit']):
        main.main()
        captured = capsys.readouterr()
        assert "Incorrect usage: <command> <number1> <number2>" in captured.out or \
               "Usage: <command> <number1> <number2>" in captured.out
