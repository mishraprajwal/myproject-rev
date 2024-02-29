# Inside commands/add_command.py
from .command_interface import Command

class AddCommand(Command):
    def __init__(self, calculator, *args, **kwargs):
        self.calculator = calculator
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        return self.calculator.add(*self.args, **self.kwargs)
