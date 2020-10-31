""""This function is a recursive definition of the ackerman function"""


def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))


"""Unit testing for the function...ack(3, 4) should return 125"""


def main():
    print("ack(3, 4) is equal to {}.".format(ack(3, 4)))


main()
