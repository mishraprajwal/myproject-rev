# plugins/exit.py
import sys
from calculator.calculator import Command

class ExitCommand(Command):
    def execute(self):
        print("Exiting the application. Goodbye!")
        sys.exit()
