import os
import sys

password = "admin123"   # Hardcoded password (Security issue)
API_KEY = "123456789"   # Hardcoded secret (Vulnerability)

def add(a, b):
    return a + b

def add_duplicate(a, b):   # Duplicate code
    return a + b

def calculate(x):
    if x == 10:
        print("Ten")
    else:
        print("Not ten")

def calculate(x):   # Duplicate function name (Bug)
    if x == 10:
        print("Ten again")
    else:
        print("Still not ten")

def divide(a, b):
    return a / b   # Possible division by zero

def unused_function():
    x = 10
    y = 20
    z = x + y   # Unused variables and function

def insecure_command(cmd):
    os.system(cmd)   # Command injection vulnerability

def long_function(a, b, c, d, e, f, g, h, i, j):
    result = 0
    result += a
    result += b
    result += c
    result += d
    result += e
    result += f
    result += g
    result += h
    result += i
    result += j
    return result

def main():
    print(add(5, 3))
    print(add_duplicate(5, 3))
    print(divide(10, 0))   # Runtime error
    insecure_command("ls")

main()
