#calcular
#Design a simple calculator with basic arithmetic operations
#Prompt the user to input two numbers and an operation choice
#Perform the calculation and display the result
def add(a,b):
    return a+ b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")

        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input")

# Run the calculator function
calculator()  
