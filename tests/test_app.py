import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, subtract, multiply, divide, log, square, sin, cos, square_root, percentage
from math import pi

def test_add_1():
    assert add(5, 6) == 11

def test_add_2():
    assert add(5, 6) != 10

def test_subtract_1():
    assert subtract(10, 4) == 6

def test_subtract_2():
    assert subtract(10, 4) != 5

def test_multiply_1():
    assert multiply(3, 7) == 21

def test_multiply_2():
    assert multiply(3, 7) != 20

def test_divide_1():
    assert divide(20, 4) == 5

def test_divide_2():
    assert divide(20, 4) != 6

def test_divide_by_zero():
    error = False
    try:
        divide(10, 0)
    except ValueError as e:
        error = True
        assert str(e) == "Cannot divide by zero."
    assert error

def test_log_1():
    assert log(100, 10) == 2

def test_log_2():
    assert log(100, 10) != 1

def test_square_1():
    assert square(5) == 25

def test_square_2():
    assert square(7) == 49

def test_sin_1():
    assert sin(pi / 2) == 1

def test_sin_2():
    assert sin(0) == 0

def test_cos_1():
    assert cos(0) == 1

def test_cos_2():
    assert cos(pi) == -1

def test_square_root_1():
    assert square_root(49) == 7

def test_square_root_2():
    assert square_root(64) == 8

def test_percentage_1():
    assert percentage(25, 200) == 12.5

def test_percentage_2():
    assert percentage(50, 400) == 12.5

