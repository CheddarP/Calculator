from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    number1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:

        for signs in operations:
            print(signs)
        operation_symbol = input("Pick an operation to perform: ")

        number2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(number1, number2)

        print(f"{number1} {operation_symbol} {number2} = {answer}")

        keep_going = input(f"Type 'yes' to keep calculating with {answer}, or type 'no' to start a new calculation:  ").lower()
        if keep_going == 'no':
            should_continue = False
            calculator()
        else:
            number1 = answer

calculator()

