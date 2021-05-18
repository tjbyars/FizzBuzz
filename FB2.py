# FizzBuzz 2
# Run file and outputs to file, overwriting with standard FizzBuzz output
# Runs through 1 to 100

f = open("FizzBuzz.txt", "w")
for i in range(1, 101):
    out = ""
    if (i % 3 == 0):
        out += "Fizz"
    if (i % 5 == 0):
        out += "Buzz"
    if len(out) == 0:
        out = str(i)
    # print to file
    out += "\n"
    f.write(out)

f.close()
