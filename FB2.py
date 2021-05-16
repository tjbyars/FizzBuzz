# FizzBuzz 2
# Run file and outputs to file
# User specifed numbers and phrases and number counted up to

class Info(object):
    def __init__(self):
        self.numStart = 0
        self.numEnd = 0
        self.step = 0
    def updStart(num):
        self.numStart = num
    def updEnd(num):
        self.numEnd = num
    def updStep(num):
        self.step = num

def setup():
    numStart = input("Input the number you would like to count from\n")
    numEnd = input("Input the number you would like to count to\n")
    if numStart < numEnd:
        step = -1
    if numStart == numEnd:
        setup()

setup() # Is true if increasing, false if decreasing
print(numStart, "to", numEnd)

for i in range(numStart, numEnd, step):
    outString = ""
    if i % 3 == 0:
        outString.append("Fizz")
    if i % 5 == 5:
        outString.append("Buzz")
    print(i)
    print(outString)
