import sys
from decimal import Decimal, InvalidOperation
# Ensure correct import paths based on your project structure
from calculator import Calculator
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

def display_menu(operation_mappings):
    print("\nAvailable commands:")
    for command in operation_mappings.keys():
        print(f"- {command}")
    print("- menu (to display this menu)")
    print("- exit (to exit the application)")

def calculate_and_print(calc, a, b, operation_name, operation_mappings):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command_class = operation_mappings.get(operation_name)

        if command_class:
            command = command_class(calc, a_decimal, b_decimal)
            result = command.execute()
            print(f"\nThe result of {a} {operation_name} {b} is equal to {result}")
        else:
            print(f"\nUnknown operation: {operation_name}")
    except InvalidOperation:
        print(f"\nInvalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("\nError: Division by zero.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def main():
    calc = Calculator()
    operation_mappings = {
        'add': AddCommand,
        'subtract': SubtractCommand,
        'multiply': MultiplyCommand,
        'divide': DivideCommand
    }

    # Display the menu right at the start before entering the loop
    display_menu(operation_mappings)

    while True:
        command_input = input("\nEnter command, 'menu' to display available commands, or 'exit' to exit: ").strip().lower()
        if command_input == "exit":
            # Displaying exit message without repeating the menu since the application is exiting
            print("Exiting the application. Goodbye!")
            break
        elif command_input == "menu":
            display_menu(operation_mappings)
            continue

        args = command_input.split()
        if len(args) != 3:
            print("Usage: <operation> <number1> <number2>")
            continue

        operation_name, a, b = args
        calculate_and_print(calc, a, b, operation_name, operation_mappings)

if __name__ == '__main__':
    main()
