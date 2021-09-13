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