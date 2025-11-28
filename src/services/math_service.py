class MathService:
    def __init__(self):
        self._factorial_cache = {0: 1, 1: 1}
        self._fibo_cache = {0: 0, 1: 1}

    def factorial(self, number: int) -> int:
        if number < 0:
            raise ValueError("Факториал вычисляется только у неотрицательных чисел")

        output: int = 1

        for i in range(1, number + 1):
            output *= i

        return output

    def factorial_recursive(self, number: int) -> int:
        if number < 0:
            raise ValueError("Факториал вычисляется только у неотрицательных чисел")

        if number in self._factorial_cache:
            return self._factorial_cache[number]

        output: int = number * self.factorial_recursive(number - 1)
        self._factorial_cache[number] = output
        return output

    def fibo(self, number: int) -> int:
        if number < 0:
            raise ValueError("Метод Фибоначчи работает только с неотрицательными числами")
        elif number in (0,1):
            return number

        a, b = 0, 1
        for i in range(2, number + 1):
            a, b = b, a + b
        return b


    def fibo_recursive(self, number: int) -> int:
        if number < 0:
            raise ValueError("Метод Фибоначчи работает только с неотрицательными числами")

        if number in self._fibo_cache:
            return self._fibo_cache[number]

        output: int = self.fibo_recursive(number - 1) + self.fibo_recursive(number - 2)
        self._fibo_cache[number] = output
        return output