import calculator

for index in range(0, 5):
    number1 = int(input("Input first number "))
    number2 = int(input("Input second number "))

    calculatorObject = calculator.CalculatorClass(number1, number2)
    add_sum = calculatorObject.add()
    print(add_sum)
    print(f"Individual Operations = {calculator.CalculatorClass.op_count}")

    calculatorObject = calculator.CalculatorClass(number1, number2)
    sub_sum = calculatorObject.sub()
    print(sub_sum)
    print(f"Individual Operations = {calculator.CalculatorClass.op_count}")

    calculatorObject = calculator.CalculatorClass(number1, number2)
    mul_sum = calculatorObject.mul()
    print(mul_sum)
    print(f"Individual Operations = {calculator.CalculatorClass.op_count}")

    calculatorObject = calculator.CalculatorClass(number1, number2)
    div_sum = calculatorObject.div()
    print(div_sum)
    print(f"Individual Operations = {calculator.CalculatorClass.op_count}")
    print("==========================================")
    print(f"Total Operations = {calculator.CalculatorClass.totalop_count}")
