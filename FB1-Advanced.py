# FizzBuzz 1 - Advanced
# Just run file and outputs to shell
# Runs through 0 to 100
# Using string concatenation

for i in range(1, 101):
    out = ""
    if (i % 3 == 0):
        out += "Fizz"
    if (i % 5 == 0):
        out += "Buzz"
    if len(out) == 0:
        out = i
    print (out)
