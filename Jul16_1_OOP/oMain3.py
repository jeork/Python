from random import randint
# randint

# 패키지에 있는 Class 불러오기 

# import animal.pet   # import 패키지명.모듈명 => 써먹을 수 있게 불러온 것
                    # # pet.pt의  소스가 여기로 들어온 셈
# d = animal.pet.Dog('댕댕이',14) 
# d.printInfo()

# import animal.pet as ap  # import 패키지명.모듈명as 별명
# d=ap.Dog('멍',1)        # 별명.클래스명(...)
# d.printInfo()

# from animal.pet import Dog  #from  패키지명.모듈명 import 가져올 거
#
# d=Dog('댕',3)
# d.printInfo()

# from animal.pet import Dog as dd
# d = dd('댕2',6)
# d.printInfo()

import animal.pet as ap

class Dog:
    def punch(self):
        print('댕댕펀치')


d = ap.Dog('댕댕이',1)
d.printInfo()

# 클래스명이 중복된다면, 가까운걸로 판정
d2 = Dog()        
d2.punch()
        
