import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, subtract, multiply, divide, log, square, sin, cos, tan, square_root, percentage, power, root
from math import pi

def test_add():
    assert add(5, 6) == 11

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 7) == 21

def test_divide():
    assert divide(20, 4) == 5

def test_divide_invalid_b():
    error = False
    try:
        divide(10, 0)
    except ValueError as e:
        error = True
        assert str(e) == "b cannot be 0. Divide by zero error."
    assert error

def test_log():
    assert log(100, 10) == 2

def test_log_invalid_a():
    error = False
    try:
        log(-5, 10)
    except ValueError as e:
        error = True
        assert str(e) == "a must be positive. Log is undefined for non-positive values."
    assert error

def test_log_invalid_b():
    error = False
    try:
        log(100, 1)
    except ValueError as e:
        error = True
        assert str(e) == "b cannot be 1. Log base cannot be 1."
    assert error

def test_log_invalid_negative_b():
    error = False
    try:
        log(100, -5)
    except ValueError as e:
        error = True
        assert str(e) == "b must be positive. Log base is undefined for non-positive values."
    assert error

def test_square():
    assert square(5) == 25

def test_sin():
    assert sin(pi / 2) == 1

def test_cos():
    assert cos(0) == 1

def test_tan():
    assert abs(tan(pi / 4) - 1.0) < 1e-10

def test_tan_invalid_a():
    error = False
    try:
        tan(pi / 2)
    except ValueError as e:
        error = True
        assert str(e) == "Tangent is undefined at odd multiples of π/2."
    assert error

def test_square_root():
    assert square_root(49) == 7

def test_square_root_invalid_a():
    error = False
    try:
        square_root(-4)
    except ValueError as e:
        error = True
        assert str(e) == "a cannot be negative. The square root of a negative number is undefined."
    assert error

def test_percentage():
    assert percentage(25, 200) == 12.5

def test_percentage_invalid_b():
    error = False
    try:
        percentage(25, 0)
    except ValueError as e:
        error = True
        assert str(e) == "b cannot be zero. Divide by zero error."
    assert error

def test_power():
    assert power(2, 3) == 8

def test_power_invalid_a_negative_b():
    error = False
    try:
        power(0, -1)
    except ValueError as e:
        error = True
        assert str(e) == "a cannot be 0 when b is less than 0. Cannot raise 0 to a negative power."
    assert error

def test_root():
    assert abs(root(8, 3) - 2.0) < 1e-10

def test_root_invalid_b():
    error = False
    try:
        root(8, 0)
    except ValueError as e:
        error = True
        assert str(e) == "b cannot be zero."
    assert error

def test_root_invalid_negative_a_even_b():
    error = False
    try:
        root(-4, 2)
    except ValueError as e:
        error = True
        assert str(e) == "a cannot be less than 0 when b is even. Cannot calculate the even root of a negative number"
    assert error

def test_root_negative_a_odd_b():
    assert abs(root(-8, 3) - (-2.0)) < 1e-10

