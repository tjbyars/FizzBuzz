# FizzBuzz 1 - Simple
# Run file and outputs to shell
# Runs through 1 to 100
# Using if...else

for i in range(1, 101):
    out = ""
    if (i % 3 == 0):
        out = "Fizz"
    if (i % 5 == 0):
        out = "Buzz"
    if (i % 3 == 0) and (i % 5 == 0):
        out = "FizzBuzz"
    if len(out) == 0:
        out = i
    print(out)
