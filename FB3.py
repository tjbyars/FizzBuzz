# FizzBuzz 3
# Run file and outputs to shell
# User specifed numbers and phrases and number counted up/down to

class Info:
    def __init__(self):
        self.numStart = 0
        self.numEnd = 0
        self.step = 1
        self.relationList = []
    def relSetup(self):
        if len(self.relationList) == 0:
            inputRel = input("Input the first number-phrase relation you would like in the format: 3,Fizz \n"
                            "Once you have input the relation, press enter. If you wish to run the standard FizzBuzz game, press enter before entering any relations \n")
        else:
            inputRel = input("Enter the next number-phrase relation in the format: 3,Fizz \n")
        return inputRel
    def setup(self):
        self.numStart = int(input("Input the number you would like to count from\n"))
        self.numEnd = int(input("Input the number you would like to count to\n"))
        if self.numStart > self.numEnd:
            info.step = -1
            self.numEnd -= 1
        else:
            self.numEnd += 1
        run = True
        while run == True:
            nextInp = self.relSetup()
            containsRel = False
            if len(nextInp) == 0:
                if len(self.relationList) == 0:
                    self.relationList = [[3,"Fizz"],[5,"Buzz"]]
                run = False
            else:
                inpList = list(nextInp.split(","))
                print("relationList: " , self.relationList)
                print("Input: " , inpList)
                if len(self.relationList) == 0:
                    self.relationList.append(inpList)
                else:
                    for relation in self.relationList:
                        if relation[0] == inpList[0]:
                            containsRel = True
                    if containsRel == True:
                        relation[1] = inpList[1]
                    else:
                        self.relationList.append(inpList)

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
