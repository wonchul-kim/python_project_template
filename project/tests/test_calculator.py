# test_code.py


def test_add(calculator):
    """Test functionality of add."""
    assert calculator.add(1, 2) == 3
    assert calculator.add(2, 2) == 4
    assert calculator.add(9, 2) == 11


def test_subtract(calculator):
    """Test functionality of subtract."""
    assert calculator.subtract(5, 1) == 4
    assert calculator.subtract(3, 2) == 1
    assert calculator.subtract(10, 2) == 8


def test_multiply(calculator):
    """Test functionality of multiply."""
    assert calculator.multiply(2, 2) == 4
    assert calculator.multiply(5, 6) == 30
    assert calculator.multiply(9, 3) == 27
