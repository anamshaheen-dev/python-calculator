# Simple Calculator
# Built by: Anum Shaheen

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def calculator():
    print("===========================")
    print("   Welcome to Calculator   ")
    print("===========================")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Thanks for using the calculator. Bye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", round(divide(num1, num2), 2))
        else:
            print("Invalid input! Please enter 1, 2, 3, 4, or 5.")

# This runs the calculator
calculator()
