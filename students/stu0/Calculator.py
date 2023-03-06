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

