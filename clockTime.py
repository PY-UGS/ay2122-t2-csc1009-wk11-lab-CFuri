class clockTime():
    hours = 0
    minutes = 0
    seconds = 0
    def __init__(self) -> None:#dont intialize any value at the start
        pass
    def setHour(self,input):
        if int(input) >= 24 or int(input) < 0:#if the hour is less than 0 or more than or equal to 24
            print("invalid amount of hours entered")#reject input
        else:
            self.hours = int(input)#otherwise update the hours stored in self
    def setMinute(self,input):
        if int(input) >= 60 or int(input) < 0:#if the minute is less than 0 or more than or equal to 60
            print("invalid amount of minutes entered")#reject input
        else:
            self.minutes = int(input)#otherwise update the minutes stored in self
    def setSecond(self,input):
        if int(input) >= 60 or int(input) < 0:#if the second is less than 0 or more than or equal to 60
            print("invalid amount of seconds entered")#reject input
        else:
            self.seconds = int(input)#otherwise update the seconds stored in self
    def setTime(self,input1,input2,input3):

        if int(input1) >= 24 or int(input1) < 0:
            print("invalid amount of hours entered")
        else:
            self.hours = int(input1)
        if int(input2) >= 60 or int(input2) < 0:
            print("invalid amount of minutes entered")
        else:
            self.minutes = int(input2)
        if int(input3) >= 60 or int(input3) < 0:
            print("invalid amount of seconds entered")
        else:
            self.seconds = int(input3)
    def showTime(self):
        print("The time is "+str(self.hours) + ":" + str(self.minutes)+":"+str(self.seconds))
    def chooseOp(self,choice):#call method depending on choice of operation
        if choice == '1':
            val = input("please enter the new hour")
            self.setHour(val)
        if choice == '2':
            val = input("please enter the new minute")
            self.setMinute(val)    
        if choice == '3':
            val = input("please enter the new second")
            self.setSecond(val) 
        if choice == '4':
            val1 = input("please enter the new hour")
            val2 = input("please enter the new minute")
            val3 = input("please enter the new second")
            self.setTime(val1,val2,val3)
        if choice == '5':
            self.showTime()

clock = clockTime()
while True:#keep looping until program close
    print("1. Set Hour")
    print("2. Set Minute")
    print("3. Set Second")
    print("4. Set Hour,Minute and Second")
    print("5. Display Time")
    choice = input("please choose an operation")
    clock.chooseOp(choice)