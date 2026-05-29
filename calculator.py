"""
A simple calculator application in Python
Supports basic arithmetic operations: addition, subtraction, multiplication, and division
"""

def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error! Division by zero."
    return x / y


def power(x, y):
    """Raise x to the power of y"""
    return x ** y


def sqrt(x):
    """Calculate square root of a number"""
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    return x ** 0.5


def calculator():
    """Main calculator function with menu"""
    print("=" * 50)
    print("         SIMPLE CALCULATOR")
    print("=" * 50)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5/6/7): ").strip()
        
        if choice == '7':
            print("\nThank you for using the calculator! Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                if choice == '6':
                    num = float(input("Enter number: "))
                    result = sqrt(num)
                else:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    
                    if choice == '1':
                        result = add(num1, num2)
                        operation = "+"
                    elif choice == '2':
                        result = subtract(num1, num2)
                        operation = "-"
                    elif choice == '3':
                        result = multiply(num1, num2)
                        operation = "*"
                    elif choice == '4':
                        result = divide(num1, num2)
                        operation = "/"
                    elif choice == '5':
                        result = power(num1, num2)
                        operation = "^"
                
                if choice == '6':
                    print(f"\n√{num} = {result}")
                else:
                    print(f"\n{num1} {operation} {num2} = {result}")
                    
            except ValueError:
                print("\nError! Please enter valid numbers.")
        else:
            print("\nInvalid choice! Please select a valid operation.")


if __name__ == "__main__":
    calculator()
