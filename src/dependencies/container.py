from dataclasses import dataclass

from src.services.math_service import MathService
from src.services.sort_service import SortingService
from src.services.structures import Stack


@dataclass
class Container:
    math_service: MathService
    sorting: SortingService
    structure: Stack


def get_container() -> Container:
    return Container(
        math_service=MathService(),
        sorting=SortingService(),
        structure=Stack()
    )