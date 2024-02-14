class Calculator:
    """A simple calculator class for basic arithmetic operations with history tracking."""
    
    history = []  # Class variable to store history of calculations

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the addition of a and b."""
        result = a + b
        Calculator.record_history(result)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Return the subtraction of b from a."""
        result = a - b
        Calculator.record_history(result)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Return the multiplication of a and b."""
        result = a * b
        Calculator.record_history(result)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Return the division of a by b. Raises ValueError on division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        Calculator.record_history(result)
        return result

    @classmethod
    def record_history(cls, result: float):
        """Record a calculation result to the history."""
        cls.history.append(result)

    @classmethod
    def get_last_calculation(cls) -> float:
        """Retrieve the last calculation result from the history."""
        if not cls.history:
            raise ValueError("No calculations in history.")
        return cls.history[-1]

    @classmethod
    def clear_history(cls):
        """Clears the calculation history."""
        cls.history.clear()
