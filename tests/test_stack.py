import pytest
from src.services.structures import Stack


class TestStack:
    @pytest.fixture
    def stack(self):
        return Stack()

    def test_empty(self, stack):
        assert len(stack) == 0
        assert stack.is_empty() is True

        with pytest.raises(IndexError, match="пустой"):
            stack.peek()
        with pytest.raises(IndexError, match="пустой"):
            stack.pop()
        with pytest.raises(IndexError, match="пустой"):
            stack.min()

    def test_1(self, stack):
        stack.push(325)
        assert stack.peek() == 325
        assert len(stack) == 1

        assert stack.is_empty() is False

        stack.push(7)
        assert stack.peek() == 7
        assert len(stack) == 2

    def test_2(self, stack):
        stack.push(5)
        assert stack.pop() == 5
        assert stack.is_empty() is True

        stack.push(10)
        stack.push(9)
        assert stack.pop() == 9
        assert stack.pop() == 10
        assert stack.is_empty() is True

    def test_min(self, stack):
        stack.push(6)
        assert stack.min() == 6

        stack.push(-1)
        assert stack.min() == -1

        stack.push(77)
        assert stack.min() == -1

        stack.push(-66)
        assert stack.min() == -66

        stack.pop()
        assert stack.min() == -1

        stack.pop()
        assert stack.min() == -1

        stack.pop()
        assert stack.min() == 6