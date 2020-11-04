def binary_to_decimal(binary: str):
    decimal = 0
    for i in range(1, len(binary) + 1):
        decimal += int(binary[-i]) * 2 ** (i - 1)
    return decimal


def binary_to_decimal_list_comprehension(binary: str):
    return sum([int(binary[::-1][i]) * (2 ** i) for i in range(len(binary))])


five = binary_to_decimal("101")  # should be 5
twelve = binary_to_decimal("1100")  # should be 12

ten = binary_to_decimal_list_comprehension("1010")  # should be 10
twelve_with_list_comprehension = binary_to_decimal_list_comprehension("1100")  # should be 12
five_with_list_comprehension = binary_to_decimal_list_comprehension("101")  # should be 5

print(five, twelve, ten, twelve_with_list_comprehension, five_with_list_comprehension)


