# plugins/multiply.py
from calculator.calculator import Command

class MultiplyCommand(Command):
    def execute(self):
        a, b = self.args
        return self.calculator.multiply(a, b)
