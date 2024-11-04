class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def main():
    calc = Calculator()
    
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1-4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"Result: {calc.add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {calc.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {calc.multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"Result: {calc.divide(num1, num2)}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
