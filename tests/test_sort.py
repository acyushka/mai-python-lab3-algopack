import pytest
from src.services.sort_service import SortingService


class TestSortingService:
    @pytest.fixture
    def sorting(self):
        return SortingService()

    @pytest.mark.parametrize("input,expected", [
        ([], []),
        ([7], [7]),
        ([26, 6, 16], [6, 16, 26]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([23, 57, 23, 1, 1, 334], [1, 1, 23, 23, 57, 334]),
    ])
    def test_bubble(self, sorting, input, expected):
        assert sorting.bubble_sort(input) == expected

    @pytest.mark.parametrize("input,expected", [
        ([], []),
        ([7], [7]),
        ([26, 6, 16], [6, 16, 26]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([23, 57, 23, 1, 1, 334], [1, 1, 23, 23, 57, 334]),
    ])
    def test_quick(self, sorting, input, expected):
        assert sorting.quick_sort(input) == expected

    @pytest.mark.parametrize("input,expected", [
        ([], []),
        ([7], [7]),
        ([26, 6, 16], [6, 16, 26]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([23, 57, 23, 1, 1, 334], [1, 1, 23, 23, 57, 334]),
    ])
    def test_counting(self, sorting, input, expected):
        assert sorting.counting_sort(input) == expected

    @pytest.mark.parametrize("input,expected", [
        ([], []),
        ([7], [7]),
        ([26, 6, 16], [6, 16, 26]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([23, 57, 23, 1, 1, 334], [1, 1, 23, 23, 57, 334]),
    ])
    def test_radix(self, sorting, input, expected):
        assert sorting.radix_sort(input) == expected

    @pytest.mark.parametrize("input,expected", [
        ([], []),
        ([7], [7]),
        ([26, 6, 16], [6, 16, 26]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([23, 57, 23, 1, 1, 334], [1, 1, 23, 23, 57, 334]),
    ])
    def test_heap(self, sorting, input, expected):
        assert sorting.heap_sort(input) == expected

    @pytest.mark.parametrize("input,buckets,expected", [
        ([], None, []),
        ([5.3], None, [5.3]),
        ([1.5, 0.15, 2.88, 1.33], None, [0.15, 1.33, 1.5, 2.88]),
        ([10.5333, 3.22, 7.8, 1.1], None, [1.1, 3.22, 7.8, 10.5333]),
        ([100, 50, 75, 25], None, [25.0, 50.0, 75.0, 100.0]),
        ([-1.99, -0.55, -2.34, -1.787], None, [-2.34, -1.99, -1.787, -0.55]),
        ([-10000.5, -3.2, -7.8, -1.11], None, [-10000.5, -7.8, -3.2, -1.11]),
        ([-2.5, 1.5, -0.5, 3.0, -1.0], None, [-2.5, -1.0, -0.5, 1.5, 3.0]),
        ([-10, 5, -3, 8.11, 0], None, [-10.0, -3.0, 0.0, 5.0, 8.11]),
        ([1, 2, 3], 10, [1.0, 2.0, 3.0]),
        ([1, 2, 3], 100, [1.0, 2.0, 3.0]),
    ])
    def test_bucket(self, sorting, input, buckets, expected):
        assert sorting.bucket_sort(input, buckets) == expected