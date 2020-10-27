def factorial(n):
    if (not isinstance(n, int)):
        print("Factorials are only defined for integers, your input "\
              "does not have a defined factorial function.")
        return
    else:
        if (n < 0):
            print("The factorial function is not defined for "\
                  "negative values.")
            return
        elif (n == 0):
            return 1
        else:
            n = n * factorial(n - 1)
            return n
    return n
            