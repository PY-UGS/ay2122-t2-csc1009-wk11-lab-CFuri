class Calculator:
    tempstore = 0
    def __init__(self) -> None:
        pass
    def adder(self,v1,v2):
        if v1 == "ans":#if ans is input, use the stored result from previous operation
            self.tempstore = self.tempstore + float(v2)
        elif v2 == "ans":
            self.tempstore = float(v1) + self.tempstore
        else:
            self.tempstore = float(v1) + float(v2)
        return self.tempstore  
    def subtractor(self,v1,v2):
        if v1 == "ans":#depending of the position of ans, use it as v1 or v2
            self.tempstore = self.tempstore - float(v2)
        elif v2 == "ans":
            self.tempstore = float(v1) - self.tempstore
        else:
            self.tempstore = float(v1) - float(v2)
        return self.tempstore   
    def multiplier(self,v1,v2):
        if v1 == "ans":
            self.tempstore = self.tempstore * float(v2)
        elif v2 == "ans":
            self.tempstore = float(v1) * self.tempstore
        else:
            self.tempstore = float(v1) * float(v2)
        return self.tempstore  

    def divider(self,v1,v2):
        if v1 == "ans":
            self.tempstore = self.tempstore/float(v2)
        elif v2 == "ans":
            self.tempstore = float(v1)/self.tempstore
        else:
            self.tempstore = float(v1)/float(v2)
        return self.tempstore  
    def clear(self):#clear the stored result
        self.tempstore = 0
        print("Reset stored value to 0")
    def getOperation(self,result):
        temp = result.split(" ")#take input and split it up
        if temp[1] == "+":#depending on the operation signed used, use the different operations
            print(result + " = " + str(self.adder(temp[0],temp[2])))
        elif temp[1] == "-":
            print(result + " = " + str(self.subtractor(temp[0],temp[2])))  
        elif temp[1] == "*":
            print(result + " = " + str(self.multiplier(temp[0],temp[2])))    
        elif temp[1] == "/":
            print(result + " = " + str(self.divider(temp[0],temp[2])))  
        if temp[0] == "clear":
            self.clear
        


c = Calculator()
while True:#keep looping while program is active
    temp = input("Enter Operation with spacings: ")
    c.getOperation(temp)
    

