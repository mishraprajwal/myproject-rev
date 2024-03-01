# plugins/divide.py
from calculator.calculator import Command

class DivideCommand(Command):
    def execute(self):
        a, b = self.args
        # Error handling for division by zero could also be managed here if preferred,
        # but it's typically better to handle it in the Calculator class or the main application logic.
        if b == 0:
            return "Error: Division by zero."
        return self.calculator.divide(a, b)
