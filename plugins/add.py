# plugins/add.py
from calculator.calculator import Command

class AddCommand(Command):
    def execute(self):
        a, b = self.args
        return self.calculator.add(a, b)
