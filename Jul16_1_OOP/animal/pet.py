# 강아지 클래스 => 생성자에 이름, 나이 + 그 속성 출력기능

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def printInfo(self):
        print(self.name, self.age)
        
    
d1 = Dog('강아지',10)


if __name__ == "__main__":
    # 여기서 야생동물 불러와서 => 객체 만들어서 출력하는 기능까지
    from animal.wild import Ant
    a  = Ant('동학개미',100000)
    a.printInfo()
    
    
