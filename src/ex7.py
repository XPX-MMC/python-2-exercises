
class Calculator:

    def __init__(self, op1, op2):
        self._result = 0.0
        self._op1 = op1
        self._op2 = op2

    def add(self):
        self._result = self._op1 + self._op2

    def sub(self):
        self._result = self._op1 - self._op2

    def mul(self):
        self._result = self._op1 * self._op2

    def div(self):
        self._result = self._op1 / self._op2

    def get_result(self):
        return self._result




calculator1 = Calculator(4, 3)
calculator1.add()
print(calculator1.get_result())

calculator2 = Calculator(4, 3)
calculator2.sub()
print(calculator2.get_result())

calculator3 = Calculator(2, 3)
calculator3.mul()
print(calculator3.get_result())

calculator4 = Calculator(8, 2)
calculator4.div()
print(calculator4.get_result())