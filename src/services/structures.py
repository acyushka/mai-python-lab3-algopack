class Stack:
    def __init__(self):
        self.items = []
        self.current_size = 0

    def __len__(self) -> int:
        """Вывести текущую длину стека"""
        return self.current_size

    def is_empty(self) -> bool:
        """Проверить стек на пустоту"""
        return self.__len__() == 0

    def push(self, x: int) -> None:
        """Добавить в стек новый элемент"""
        if self.is_empty():
            self.items.append((x, x))
        else:
            current_minimum = self.items[-1][-1]
            if x >= current_minimum:
                self.items.append((x, current_minimum))
            else:
                self.items.append((x, x))

        self.current_size += 1

    def peek(self) -> int:
        """Вывести верхний элемент стека без удаления"""
        if self.is_empty():
            raise IndexError("Стек пустой")

        return self.items[-1][0]

    def pop(self) -> int:
        """Вывести верхний элемент стека с удалением"""
        result = self.peek()
        del self.items[-1]
        self.current_size -= 1

        return result

    def min(self) -> int:
        """Вывести текущий минимум в стеке, работает за константное время"""
        if self.is_empty():
            raise IndexError("Стек пустой")
        
        return self.items[-1][-1]

