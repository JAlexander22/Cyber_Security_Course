import calculator_module

i = 1
while i != 0:
    for i in range (0, 5):
        number1 = int(input("What's your first number?: "))
        number2 = int(input("What's your second number?: "))

        add_value = calculator_module.add(number1, number2)
        print(number1, "+", number2, "=", add_value)

        sub_value = calculator_module.sub(number1, number2)
        print(number1, "-", number2, "=", sub_value)

        mul_value = calculator_module.mul(number1, number2)
        print(number1, "*", number2, "=", mul_value)

        div_value = calculator_module.div(number1, number2)
        print(number1, "/", number2, "=", div_value)


        again = str(input("Want to continue?(yes/no): "))
        if again == "no":
            break


