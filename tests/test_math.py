import pytest
from src.services.math_service import MathService

class TestMathService:
    @pytest.fixture
    def math_service(self):
        return MathService()

    def test_fact(self, math_service):
        assert math_service.factorial(0) == 1
        assert math_service.factorial(1) == 1
        assert math_service.factorial(7) == 5040
        assert math_service.factorial(33) == 8683317618811886495518194401280000000

    def test_fact_recursive(self, math_service):
        assert math_service.factorial_recursive(0) == 1
        assert math_service.factorial_recursive(1) == 1
        assert math_service.factorial_recursive(7) == 5040
        assert math_service.factorial_recursive(33) == 8683317618811886495518194401280000000

    def test_fact_error(self, math_service):
        with pytest.raises(ValueError, match="неотрицательных"):
            math_service.factorial(-1)
        with pytest.raises(ValueError, match="неотрицательных"):
            math_service.factorial_recursive(-1)

    def test_fibo(self, math_service):
        assert math_service.fibo(0) == 0
        assert math_service.fibo(1) == 1
        assert math_service.fibo(3) == 2
        assert math_service.fibo(5) == 5
        assert math_service.fibo(33) == 3524578

    def test_fibo_recursive(self, math_service):
        assert math_service.fibo_recursive(0) == 0
        assert math_service.fibo_recursive(1) == 1
        assert math_service.fibo_recursive(3) == 2
        assert math_service.fibo_recursive(5) == 5
        assert math_service.fibo_recursive(33) == 3524578

    def test_fibo_error(self, math_service):
        with pytest.raises(ValueError, match="неотрицательными"):
            math_service.fibo(-1)
        with pytest.raises(ValueError, match="неотрицательными"):
            math_service.fibo_recursive(-1)
