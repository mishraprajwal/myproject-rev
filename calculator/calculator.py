# Inside calculator.py
class Calculator:
    """A simple calculator class."""
    
    history = []  # Class variable to store history of calculations

    @staticmethod
    def add(first_number: float, second_number: float) -> float:
        result = first_number + second_number
        Calculator._update_history(f"Added {first_number} + {second_number} = {result}")
        return result

    @staticmethod
    def subtract(first_number: float, second_number: float) -> float:
        result = first_number - second_number
        Calculator._update_history(f"Subtracted {first_number} - {second_number} = {result}")
        return result

    @staticmethod
    def multiply(first_number: float, second_number: float) -> float:
        result = first_number * second_number
        Calculator._update_history(f"Multiplied {first_number} * {second_number} = {result}")
        return result

    @staticmethod
    def divide(first_number: float, second_number: float) -> float:
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        result = first_number / second_number
        Calculator._update_history(f"Divided {first_number} / {second_number} = {result}")
        return result

    @classmethod
    def _update_history(cls, calculation: str) -> None:
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> str:
        return cls.history[-1] if cls.history else "No calculations yet."

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()
        
class Command:
    def __init__(self, calculator, *args):
        self.calculator = calculator
        self.args = args

    def execute(self):
        raise NotImplementedError
