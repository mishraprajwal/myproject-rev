import sys
from decimal import Decimal, InvalidOperation
import pkgutil
import importlib
from multiprocessing import Process, Queue
from pathlib import Path
from calculator import Calculator, Command

# Global flag to control the use of multiprocessing
use_multiprocessing = True

def load_plugins(plugin_path='plugins'):
    command_classes = {}
    plugins_dir = Path(__file__).resolve().parent / plugin_path
    for _, module_name, _ in pkgutil.iter_modules([str(plugins_dir)]):
        module = importlib.import_module(f"{plugin_path}.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                command_classes[module_name] = attribute
    return command_classes

def display_menu(operation_mappings):
    print("\nAvailable commands:")
    for command in operation_mappings.keys():
        print(f"- {command}")
    print("- menu (to display this menu)")
    print("- exit (to exit the application)")

def calculate_and_print(calc, a, b, operation_name, operation_mappings, result_queue):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command_class = operation_mappings.get(operation_name)
        if command_class:
            command_instance = command_class(calc, a_decimal, b_decimal)
            result = command_instance.execute()
            result_queue.put(f"\nThe result of {a} {operation_name} {b} is equal to {result}")
        else:
            result_queue.put(f"\nUnknown operation: {operation_name}")
    except InvalidOperation:
        result_queue.put(f"\nInvalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        result_queue.put("\nError: Division by zero.")
    except Exception as e:
        result_queue.put(f"\nAn error occurred: {e}")

def main():
    calc = Calculator()
    operation_mappings = load_plugins()
    display_menu(operation_mappings)

    while True:
        command_input = input("\nEnter command, 'menu' to display available commands, or 'exit' to exit: ").strip().lower()
        if command_input == "exit":
            print("Exiting the application. Goodbye!")
            break
        elif command_input == "menu":
            display_menu(operation_mappings)
            continue

        args = command_input.split()
        if len(args) != 3:
            print("Usage: <command> <number1> <number2>")
            continue

        operation_name, a, b = args[0], args[1], args[2]
        result_queue = Queue()

        if use_multiprocessing:
            process = Process(target=calculate_and_print, args=(calc, a, b, operation_name, operation_mappings, result_queue))
            process.start()
            process.join()
        else:
            calculate_and_print(calc, a, b, operation_name, operation_mappings, result_queue)

        while not result_queue.empty():
            print(result_queue.get())

if __name__ == '__main__':
    main()
