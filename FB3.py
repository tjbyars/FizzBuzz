# FizzBuzz 3
# Run file and outputs to shell
# User specifed numbers and phrases and number counted up to

class Info:
    def __init__(self):
        self.numStart = 0
        self.numEnd = 0
        self.step = 1
        self.relationList = [[3, "Fizz"], [5, "Buzz"]]
    def relSetup(self):
        run = True
        while run == True:
            inputRel = input("Input the number-phrase relations you would like in the format \n"
                            '[3,"Fizz"] \n'
                            "Once you have entered all the relations, press enter. If you wish to run the standard FizzBuzz game, press enter before entering any relations \n")
            if len(inputRel) == 0:
                run = False
            else:
                self.relSetup()
                return False
    def setup(self):
        self.numStart = int(input("Input the number you would like to count from\n"))
        self.numEnd = int(input("Input the number you would like to count to\n")) + 1
        if self.numStart < self.numEnd:
            step = -1
        if self.numStart == self.numEnd:
            setup()
        self.relSetup()

info = Info()
info.setup()
print(info.numStart, "to", info.numEnd, "step", info.step)
print(info.relationList)

for i in range(info.numStart, info.numEnd, info.step):
    outString = ""
    for relation in info.relationList:
        #print(relation)
        numStr = str(relation)
        #print(numStr)
        num = int(numStr)
        if i % num == 0:
            outString += relation[1]
    if len(outString) == 0:
        print(i)
    else:
        print(outString)
