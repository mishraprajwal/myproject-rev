"""
This module contains tests for the Menu class in the plugins.menu module.
"""

import unittest
from unittest.mock import patch
from io import StringIO
# Correcting the import to match the class name we're testing
from plugins.menu import MenuCommand

class TestMenu(unittest.TestCase):
    """
    Test case for the Menu class.
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        """
        Test that displaying the menu prints the menu items.
        """
        # Assuming Menu class is initialized with a list of items
        items = ['item1', 'item2', 'item3']
        menu = MenuCommand(items)
        menu.display()

        # Build the expected output
        expected_output = '\n'.join(items) + '\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
