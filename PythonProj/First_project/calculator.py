def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a ,b):
    try:
        return a / b
    except ZeroDivisionError as exception_zero:
        print(exception_zero)
        return "No Answer Given"
    finally:
        print("Let's carry on")




i = 1
while i != 0:
    for i in range (0, 5):
        number1 = int(input("What's your first number?: "))
        number2 = int(input("What's your second number?: "))


        print(number1, "+", number2, "=", add(number1,number2))
        print(number1, "-", number2, "=", sub(number1, number2))
        print(number1, "*", number2, "=", mul(number1, number2))
        print(number1, "/", number2, "=", div(number1, number2))


        again = str(input("Want to continue?(yes/no): "))
        if again == "no":
            break

