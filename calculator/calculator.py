# calculator.py

class Calculator:
    """A simple calculator class that supports basic arithmetic operations with a history feature."""

    history = []  # Class variable to store history of calculations

    @staticmethod
    def add(first_number: float, second_number: float) -> float:
        """Add two numbers."""
        result = first_number + second_number
        Calculator._update_history(f"Added {first_number} + {second_number} = {result}")
        return result

    @staticmethod
    def subtract(first_number: float, second_number: float) -> float:
        """Subtract second number from first number."""
        result = first_number - second_number
        Calculator._update_history(f"Subtracted {first_number} - {second_number} = {result}")
        return result

    @staticmethod
    def multiply(first_number: float, second_number: float) -> float:
        """Multiply two numbers."""
        result = first_number * second_number
        Calculator._update_history(f"Multiplied {first_number} * {second_number} = {result}")
        return result

    @staticmethod
    def divide(first_number: float, second_number: float) -> float:
        """Divide first number by second number. Throws ValueError on division by zero."""
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        result = first_number / second_number
        Calculator._update_history(f"Divided {first_number} / {second_number} = {result}")
        return result

    @classmethod
    def _update_history(cls, calculation: str) -> None:
        """Private class method to update calculation history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> str:
        """Return the last calculation from history."""
        return cls.history[-1] if cls.history else "No calculations yet."

    @classmethod
    def clear_history(cls) -> None:
        """Clear the calculation history."""
        cls.history.clear()
