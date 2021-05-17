# FizzBuzz 2
# Run file and outputs to file
# User specifed numbers and phrases and number counted up to

class Info:
    def __init__(self):
        self.numStart = 0
        self.numEnd = 0
        self.step = 1
    def setup(self):
        self.numStart = int(input("Input the number you would like to count from\n"))
        self.numEnd = int(input("Input the number you would like to count to\n"))
        if self.numStart < self.numEnd:
            step = -1
        if self.numStart == self.numEnd:
            setup()

info = Info()
info.setup() # Is true if increasing, false if decreasing
print(info.numStart, "to", info.numEnd, "step", info.step)

for i in range(info.numStart, info.numEnd, info.step):
    outString = ""
    if i % 3 == 0:
        outString += "Fizz"
    if i % 5 == 0:
        outString += "Buzz"
    if len(outString) == 0:
        print(i)
    else:
        print(outString)
