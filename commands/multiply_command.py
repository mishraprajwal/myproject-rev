# Inside commands/multiply_command.py
from .command_interface import Command

class MultiplyCommand(Command):
    def __init__(self, calculator, *args, **kwargs):
        self.calculator = calculator
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        return self.calculator.multiply(*self.args, **self.kwargs)
