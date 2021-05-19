# FizzBuzz 3
# Run file and outputs to shell
# User specifed numbers and phrases and number counted up to

class Info:
    def __init__(self):
        self.numStart = 0
        self.numEnd = 0
        self.step = 1
        self.relationList = []
        self.count = 0
        #[[3, "Fizz"], [5, "Buzz"]]
    def relSetup(self):
        run = True
        while run == True:
            print("start count: ", self.count)
            if self.count == 0:
                inputRel = input("Input the first number-phrase relation you would like in the format: \n"
                                "3,Fizz \n"
                                "Once you have input the relation, press enter. If you wish to run the standard FizzBuzz game, press enter before entering any relations \n")
            else:
                inputRel = input("Enter the next number-phrase relation in the format: \n"
                                 "3,Fizz \n")
            if len(inputRel) == 0:
                self.count = -5
            if self.count >= 0:
                print("sus")
                self.relationList.append(list(inputRel.split(",")))
                self.count += 1
                self.relSetup()
            else:
                run = False
                
    def setup(self):
        self.numStart = int(input("Input the number you would like to count from\n"))
        self.numEnd = int(input("Input the number you would like to count to\n")) + 1
        if self.numStart < self.numEnd:
            step = -1
        if self.numStart == self.numEnd:
            setup()
        self.count = 0
        while self.count >= 0:
            self.relSetup()

info = Info()
info.setup()

for i in range(info.numStart, info.numEnd, info.step):
    outString = ""
    for relation in info.relationList:
        num = int(relation[0])
        if i % num == 0:
            outString += relation[1]
    if len(outString) == 0:
        print(i)
    else:
        print(outString)
