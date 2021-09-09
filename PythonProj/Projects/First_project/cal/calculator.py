import calculator_module
import json


counter = 0
equation = {

}

json_object = []

for i in range (counter, 5):
    counter +=1
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

    equation :{
        counter: {
        'Add' : add_value,
        'Sub' : sub_value,
        'Mul' : mul_value,
        'div' : div_value,
        }}

    equation_copy = equation_copy()
    json_object.append(equation_copy)

    with open("log.solution1.json", "a+")as file:
        json.dump(json_object, file, indent = 4)
