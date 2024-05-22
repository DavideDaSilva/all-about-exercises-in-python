class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Cannot divide by zero"
        else:
            return x / y

calc = Calculator()

while True:
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Enter choice(Ex.: 1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the program")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", calc.add(num1, num2))
    elif choice == '2':
        print("Result: ", calc.subtract(num1, num2))
    elif choice == '3':
        print("Result: ", calc.multiply(num1, num2))
    elif choice == '4':
        print("Result: ", calc.divide(num1, num2))
        print("\n")
    else:
        print("Invalid input")
