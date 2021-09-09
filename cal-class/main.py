import calculator


number1 = int(input("Input first number "))
number2 = int(input("Input second number "))

calculatorObject = calculator.CalculatorClass(number1, number2)
sum = calculatorObject.add()
print(sum)
print(f"Total Operations = {calculator.CalculatorClass.op_count}")
