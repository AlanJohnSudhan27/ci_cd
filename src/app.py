import math

def  add (a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def log(a, base=10):
    return math.log(a, base)

def square(a):
    return a * a

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def square_root(a):
    return math.sqrt(a)

def percentage(a, total):
    return (a / total) * 100
