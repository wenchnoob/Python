
# Even numbers using list comprehensions
ls = [i for i in range(1, 101) if i % 2 == 0]

# FizzBuzz using list comprehensions
FizzBuzz = ["Fizz" if (not str(i).isalpha() and i % 3 == 0) else i for i in\
            ["FizzBuzz" if (i % 15 == 0) else i for i in range(101)]]

print(ls)
print(FizzBuzz)

# Generator does a similar thing to list comprehensions, but it does not generate values all at once, but rather one
# at a time
g = (i**2 for i in range(5, 11))
# drop five for no reason and then proceed with 6 to 10
next(g)
for i in g:
    print(i, end=" ")
print()


