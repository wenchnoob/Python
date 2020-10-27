"""This class is a file full of math functions."""

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def divide(a, b):
    return a/b

def mod(a, b):
    return a%b

def absval(a):
    if a < 0:
        return -a
    else:
        return a
    
def exp(a, b):
    return a**b

def larger(a, b):
    if a > b:
        return a
    else:
        return b
def smaller(a, b):
    if a < b:
        return a
    else:
        return b
def gcd(a, b):
    if a > b:
        if (a%b) == 0:
            return b
        return gcd(a%b, b)
    else:
        if (b%a) == 0:
            return a
        return gcd(b%a, a)
        

            

