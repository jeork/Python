class Book:
    # def __init__(self):
        # print('기본생성자 - 책 생성')
        
    # 생성자 : 객체가 메모리상에 만들어질 때 호출하는 메소드
    # overloading이 안되니깐 => 생성자를 하나만 만들어야 함
    def __init__(self, title, price):
        print('오버로딩 된 생성자?!')  
        self.title = title # 보통은 이렇게 생성자에서 멤버변수를 만들어서 결정
        self.price = price 
        
    def printInfo(self):
        print(self.title, self.price)
        
    # 소멸자(destructor)
    def __del__(self):
        print('책 삭제')
# 사람 클래스 : 이름, 나이 / 그 속성을 출력하는 기능 / 생성자, 소멸자 / 2개
class Person:
    def __init__(self,name,age):    # 생성자
        self.name = name
        self.age = age
        
    def printInfo(self):
        print('이름 : {}, 나이 : {}'.format(self.name,self.age))  # 속성 출력
        
    def __del__(self):              # 소멸자
        print('삭제!')    
        
##########################################
# b1 = Book()
b2 = Book('요리책', 5000)
b2.printInfo()
print('----------')
##########################################
#Garbage Collector : 그 객체를 가리키는 변수가 없게되면 Heap영역을 자동으로 정리
p1 = Person('오제록',27)
p1.printInfo()
p2 = Person('오제록2',135)
p2.printInfo()
print('----------')

p3 = p1
p3.printInfo()
print('----------')
p1=None
p3=None
print('111111111111')