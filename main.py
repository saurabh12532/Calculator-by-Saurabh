import re

def print_menu():
    print("\nSimple CLI Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation():
    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in ('1', '2', '3', '4', '5'):
            return choice
        else:
            print("Invalid choice. Please select a valid option.")

def calculate(op, num1, num2):
    if op == '1':
        return num1 + num2
    elif op == '2':
        return num1 - num2
    elif op == '3':
        return num1 * num2
    elif op == '4':
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return num1 / num2

def main():
    while True:
        print_menu()
        operation = get_operation()

        if operation == '5':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = calculate(operation, num1, num2)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
