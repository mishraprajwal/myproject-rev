# Inside commands/subtract_command.py
from .command_interface import Command

class SubtractCommand(Command):
    def __init__(self, calculator, *args, **kwargs):
        self.calculator = calculator
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        return self.calculator.subtract(*self.args, **self.kwargs)
