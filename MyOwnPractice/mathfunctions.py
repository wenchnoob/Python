"""
mathfunctions.py
This class is a file full of math functions.

Author: Wenchy Dutreuil
Date: 27 October 2020

"""

"""This function returns the sums of the two arguments"""


def add(a, b):
    return a + b


"""This function returns the difference between first argument to the second"""


def sub(a, b):
    return a - b


"""This function returns the product of the two arguments"""


def mul(a, b):
    return a * b


"""This function returns the value of a/b"""


def divide(a, b):
    return a / b


"""This function returns the remainder when you divide a by b"""


def mod(a, b):
    return a % b


"""This function returns the absolute value of the variable"""


def absval(a):
    if a < 0:
        return -a
    else:
        return a


"""This function returns the value of a raised to b"""


def exp(a, b):
    return a ** b


"""This function returns the greater of the two arguments"""


def larger(a, b):
    if a > b:
        return a
    else:
        return b


"""This function returns the smaller of the two arguments"""


def smaller(a, b):
    if a < b:
        return a
    else:
        return b


"""This function returns the greatest common divisor of the two arguments"""


def gcd(a, b):
    if a > b:
        if (a % b) == 0:
            return b
        return gcd(a % b, b)
    else:
        if (b % a) == 0:
            return a
        return gcd(b % a, a)


"""This function returns the least common multiple of the two arguments"""


def lcm(a, b):
    if b > a:
        if b % a == 0:
            return b
    else:
        if a % b == 0:
            return a


"""This function finds (approximates) the square root of a number. This done by processing an argument x
the value to find the square root of, and an argument epsilon to determine the precision. Recommend epsilon of .00000000000001"""


def sqroot(x, epsilon):
    root = 10 ** (len(str(x)) - 1)
    while abs((root * root) - x) > epsilon:
        print(root)
        root = (root + x/root)/2
    return root
