# FizzBuzz 1
# Just run file and print outputs to shell
# Runs through 0 to 100

for i in range(1, 100):
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
