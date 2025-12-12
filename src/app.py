# Finished app.py

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be 0. Divide by zero error.")
    return a / b

def log(a, b=10):
    if a <= 0:
        raise ValueError("a must be positive. Log is undefined for non-positive values.")
    if b <= 0:
        raise ValueError("b must be positive. Log base is undefined for non-positive values.")
    if b == 1:
        raise ValueError("b cannot be 1. Log base cannot be 1.")
    return math.log(a, b)

def square(a):
    return a * a

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    if abs(math.cos(a)) < 1e-12:
        raise ValueError("Tangent is undefined at odd multiples of π/2.")
    return math.tan(a)

def square_root(a):
    if a < 0:
        raise ValueError("a cannot be negative. The square root of a negative number is undefined.")
    return math.sqrt(a)

def percentage(a, b):
    if b == 0:
        raise ValueError("b cannot be zero. Divide by zero error.")
    return (a / b) * 100

def power(a, b):
    if a == 0 and b < 0:
        raise ValueError("a cannot be 0 when b is less than 0. Cannot raise 0 to a negative power.")
    return a**b

def root(a, b):
    if b == 0:
        raise ValueError("b cannot be zero.")
    if a < 0 and b % 2 == 0:
        raise ValueError("a cannot be less than 0 when b is even. Cannot calculate the even root of a negative number")
    # Handles odd roots of negative numbers
    if a < 0 and b % 2 != 0:
       return -(-a)**(1/b)
    return a**(1/b)