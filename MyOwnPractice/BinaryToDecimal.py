def binary_to_decimal(binary: str):
    decimal = 0
    for i in range(1, len(binary) + 1):
        decimal += int(binary[-i]) * 2 ** (i - 1)
    return decimal


def binary_to_decimal_list_comprehension(binary: str):
    ls = [(binary.index(i) + 1) * 2 ** (binary.index(i)) for i in binary[::-1]]
    return sum(ls)


five = binary_to_decimal("101")  # should be 5
twelve = binary_to_decimal("1100")  # should be 12

ten = binary_to_decimal_list_comprehension("1010")


print(five, twelve, ten)
