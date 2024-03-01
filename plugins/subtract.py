# plugins/subtract.py
from calculator.calculator import Command

class SubtractCommand(Command):
    def execute(self):
        a, b = self.args
        return self.calculator.subtract(a, b)
