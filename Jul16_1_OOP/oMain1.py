class Shop():
    def showInfo(self):
        print(self.name, self.floor)
        
class Dog:
    name="bb"   # 의미 없음
                # 24번줄에서 넣은 값이 6번줄의 name에 담기는 것이 아님
                # 단순 기본값 처리용
                # 멤버변수는 생성자에서 만들어 줄것!

    def bark(self):
        print('멍')
    def printInfo(self):
        # Java : this.name => this.은 생략이 가능 => name
        # Python : self.name => self.은 생략이 불가능 => self.name으로 써야함
        print(self.name, self.age)  
    # overloading 지원 안됨 => 모든 메소드명은 다 달라야 함
    def printInfo2(self,c):
        for _ in range(c):
            print(self.name, self.age)
    # static method : 객체 만들지 않고 사용할 수 있는 메소드
    # @ : decorator(데코레이터)       
    @staticmethod
    def staticMethodTest(self):
        print('method')        
###################################################
Dog.staticMethodTest()        

s = Shop()
s.name = '카페'
s.floor = 1
s.showInfo()
print('-------------')

d=Dog()
d.name="댕댕이"
d.age=100
print(d,type(d))
d.printInfo()
d.bark()    # 메소드 호출방법1
Dog.bark(d) # 메소드 호출방법2
print('--------------')
d.printInfo2(3)