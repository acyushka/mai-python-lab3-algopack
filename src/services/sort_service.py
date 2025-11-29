import math
from dataclasses import dataclass
from typing import TypeVar, Any, Generic

T = TypeVar('T')


@dataclass
class SortingService(Generic[T]):
    def bubble_sort(self, a: list[int]) -> list[int]:
        """
        Обычная реализация бабл сорт: ходим по каждым двум рядом стоящим элементам в списке, сравниваем их между собой
        """
        n = len(a)

        for i in range(n - 1):
            for j in range(n - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a

    def quick_sort(self, a: list[int]) -> list[int]:
        """
        Задаем сначала базоый случай рекурсии.
        Выбираем опорное число pivot: я беру середину.
        Делим числа на 3 категории относительно pivot: меньшие, равные, большие.
        Вызываем рекурсию, пока не доберемся до опорного случая.
        """
        n = len(a)
        if n < 2:
            return a

        pivot = a[n // 2]

        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)

    def counting_sort(self, a: list[int]) -> list[int]:
        """
        Делаем список counter из константного кол-ва нулей. Это счетчик каждого числа встреченного в заданном списке.
        Проходимся по списку и отмечаем в counter встреченные числа, инкрементируем счетчики на позициях counter, равных встреченным числам.
        Проходимся по counter еще раз, если какое-то число там != 0: ставим его в нужную позицию в исходном списке. Готово
        """
        if not a:
            return []

        n = len(a)

        counter: list[int] = [0] * 10000

        for i in range(n):
            counter[a[i]] += 1

        pos = 0
        for number in range(10000):
            for i in range(counter[number]):
                a[pos] = number
                pos += 1

        return a

    def radix_sort(self, a: list[int], base: int = 10) -> list[int]:
        """
        Проходимся по разрядам чисел, для этого сначала по максимальному числу находим максимальный разряд.
        Потом собственно по разрядам идем, от меньшего к большему. На каждом проходе делаем counting sort, делая вспомогательный список из 0 длиной в заданную base.
        """
        if not a:
            return []

        n = len(a)
        b = [0] * n # начальный временный массив

        max_val = max(a)
        m = 1
        temp = max_val
        while temp > 0:
            m += 1
            temp //= base

        for i in range(m):
            counter = [0] * base

            for j in range(n):
                digit = (a[j] // (base ** i)) % base
                counter[digit] += 1

            count = 0
            for j in range(base):
                temp_count = counter[j]
                counter[j] = count
                count += temp_count

            for j in range(n):
                digit = (a[j] // (base ** i)) % base
                b[counter[digit]] = a[j]
                counter[digit] += 1

            a, b = b, a

        return a

    def bucket_sort(self, a: list[float], buckets: int | None = None) -> list[float]:
        """
        Задаем сначала базовый случай рекурсии. Потом считаем кол-во корзин, если не задано.
        Делаем список корзин. Проходимся по каждому элементу заданного списка. Нормализуем каждый элемент.
        Потом сортируем каждую корзину рекурсивно.
        """
        try:
            if len(a) < 2:
                return a

            n = len(a)
            if buckets is None:
                buckets = int(math.sqrt(n))

            min_val = min(a)
            max_val = max(a)
            range_val = max_val - min_val
            if range_val == 0:
                return a

            buckets_list = [[] for _ in range(buckets)]

            for x in a:
                idx = int(((x - min_val) * buckets) / (range_val + 1e-9))
                idx = min(idx, buckets - 1)
                buckets_list[idx].append(x)

            output = []
            for b in buckets_list:
                sorted_bucket = self.bucket_sort(b, buckets)
                output.extend(sorted_bucket)

            return output
        except RecursionError as e:
            raise RecursionError("Вы закинули во входные данные фигню, возникла бесконечная рекурсия")

    def heap_sort(self, a: list[int]) -> list[int]:
        """
        Первый цикл: проходимся по всем узлам списка и делаем кучу с помощью heapify.
        Второй цикл: выставляем итерационно верхушки кучи, при этом пересчитываем кучу.
        """
        n = len(a)

        def heapify(n: int, i: int) -> None:
            """Функция выстраивания кучи"""
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and a[left] > a[largest]:
                largest = left
            if right < n and a[right] > a[largest]:
                largest = right

            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                heapify(n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]
            heapify(i, 0)

        return a
