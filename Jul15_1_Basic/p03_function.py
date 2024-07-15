def test():
    print("a")

    
test()


def test2():  # : 을 썼으면 그 다음줄에는 무조건 들여쓰기
    pass  # : 뒤에 코드 적을것이 없을 때, 자리 채우는 의미

# 정수 2개를 넣으면 그 합을 '출력' 하는 함수


def add(a=5, b=8):  # 호출할 때 값을 안넣어주면 함수파라미터의 값을
    print(a + b)  # 기본값으로 사용


add(55, 12)
add()


# 정수 3개를 넣으면 그 합을 '출력'하는 함수
def add2(a=1, b=2, c=3):
    print(a + b + c)


print("=====")
add2(20, 50, 100)
add2()

# 정수 2개를 넣으면 그 합을 '구하는' 함수


def add3(a=1, b=1):
    return a + b


print(add3())


# 정수 2개를 넣으면 사친연산 결과를 '구하는' 함수
'''
    설명서 
    asdasd
    qweqwe
    !@#!@#
'''
def add4(a=1,b=2):
    '''
        설명서 
        asdasd
        qweqwe
        !@#!@#
    '''
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum,sub,mul,div
help(add4)

#q,w,e,r = add4(20,10)

q,w,_,r=add4(20,10) # _처리하면 곱하기결과 안가져올 수 있음