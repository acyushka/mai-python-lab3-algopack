import pytest
from src.dependencies.container import get_container

# ФИКСТУРЫ

@pytest.fixture
def container():
    return get_container()


@pytest.fixture
def math_service(container):
    return container.math_service


@pytest.fixture
def sort_service(container):
    return container.sorting


@pytest.fixture
def stack(container):
    return container.structure