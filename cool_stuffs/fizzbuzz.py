print("Printing the fizzbuzz pattern from 1 to 100!!!")
a = range(1, 101)

for i in a:
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
print("Welcome!")