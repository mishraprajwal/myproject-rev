# Inside commands/divide_command.py
from .command_interface import Command

class DivideCommand(Command):
    def __init__(self, calculator, *args, **kwargs):
        self.calculator = calculator
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        return self.calculator.divide(*self.args, **self.kwargs)
