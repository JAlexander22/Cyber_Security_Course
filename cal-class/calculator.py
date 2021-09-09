class CalculatorClass:
    op_count = 0
    totalop_count = 0

    @classmethod
    def add_op(cls):
        cls.op_count += 1
    @classmethod
    def addtotal_op(cls):
        cls.totalop_count += 1

    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2


    def add(self):
        self.addtotal_op()
        self.add_op()
        return self.num1 + self.num2

    def sub(self):
        self.add_op()
        return self.num1 - self.num2

    def mul(self):
        self.add_op()
        return self.num1 * self.num2

    def div(self):
        self.add_op()
        try:
            return self.num1 / self.num2
        except ZeroDivisionError as exception_zero:
            print(exception_zero)
            return "No Answer Given/ Can't divide by zero"
        finally:
            print("Let's try divide")
