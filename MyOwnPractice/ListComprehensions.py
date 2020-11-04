
# Even numbers using list comprehensions
ls = [i for i in range(1, 101) if i % 2 == 0]

# FizzBuzz using list comprehensions
FizzBuzz = ["Fizz" if (not str(i).isalpha() and i % 3 == 0) else i for i in\
            ["FizzBuzz" if (i % 15 == 0) else i for i in range(101)]]

print(ls)
print(FizzBuzz)

