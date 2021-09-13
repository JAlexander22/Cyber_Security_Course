import sqlite3
from contextlib import closing
from cal_package import calculator_module
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

    equation = {
        counter: {
        'Addition' : add_value,
        'Subtraction' : sub_value,
        'Multiplication' : mul_value,
        'Division' : div_value,
        }}

    equation_copy = equation.copy()
    json_object.append(equation_copy)

with closing(sqlite3.connect("data.db")) as connection:
    with closing(connection.cursor()) as cursor:
        #cursor.execute("CREATE TABLE sum_table (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO sum_table (name) VALUES ({'add'}, {'Sub'}, {mul}, {div})")
        #connection.commit()
        cursor.execute("SELECT * from sum_table")
        records = cursor.fetchall()
        print(records)
        for item in cursor:
            print(item)
