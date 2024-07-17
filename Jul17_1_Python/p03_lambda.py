# 변수를 할당하는 일반적인 함수
def hab(num):
    x = num + 100
    return x

print(hab(100))

# 람다 함수
(lambda num: print(num + 100))(100)

# 숫자 두개 넣으면 그 곱을 출력하는 함수
(lambda x, y: print(x * y))(5, 6)

# 숫자 두개 넣으면 그 합을 구하는 함수
sum = (lambda x, y: x + y)(7, 8)

print(sum)
