"""
This module contains tests for the ExitCommand class in the plugins.exit module.
"""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from plugins.exit import ExitCommand

class TestExitCommand(unittest.TestCase):
    """
    Test case for the ExitCommand class.
    """

    @patch('sys.exit')
    @patch('sys.stdout', new_callable=StringIO)
    def test_execute(self, mock_stdout, mock_exit):
        """
        Test that executing the command prints the exit message and calls sys.exit.
        """
        # Create a mock calculator object
        mock_calculator = MagicMock()

        # Pass the mock calculator object to the ExitCommand
        command = ExitCommand(mock_calculator)
        command.execute()

        self.assertEqual(mock_stdout.getvalue(), "Exiting the application. Goodbye!\n")
        mock_exit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
