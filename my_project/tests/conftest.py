import pytest
from my_project.src.calculator import Calculator


@pytest.fixture
def calculator():
    calculator = Calculator()

    return calculator
