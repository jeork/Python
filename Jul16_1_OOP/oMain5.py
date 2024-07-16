class Avengers():

    def __init__(self, realName):
        self.realName = realName
        
    def attack(self):
        print("무찐공격")
    
    def printInfo(self):
        print(self.realName)


######################################
class Human:

    def __init__(self, age):
        self.age = age

    def eat(self):
        print("쩝쩝박사")

    def attack(self):
        print("발차기")

    def printInfo(self):
        print(self.age)
######################################

class Ironman(Avengers, Human):

    def __init__(self, realName, age):
        Avengers.__init__(self, realName)
        Human.__init__(self, age)
        
    def attack(self):
        Avengers.attack(self)
        Human.attack(self)
        
    def printInfo(self):
        Avengers.printInfo(self)
        Human.printInfo(self)
######################################

if __name__ =="__main__":
    i = Ironman("토니스타크",40)
    i.attack()
    i.eat()
    i.printInfo()
    
        
        
