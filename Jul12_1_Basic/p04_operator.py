# 정수 2개를 입력받아서, 사칙연산에 대한 결과와
# 앞의 수를 뒤의 수로 나눴을 때의 나머지값을 출력

x = 5
y = 6

print('{0} + {1} = {2}'.format(x, y, x + y))
print('{0} - {1} = {2}'.format(x, y, x - y))
print('{0} * {1} = {2}'.format(x, y, x * y))
print('{0} % {1} = {2}'.format(x, y, x % y))

f = x // y 
print(f)  # 몫

g = x ** y  # 거듭제곱
print(g)

z = "ㅋㅋㅋ"
# h=x+z  # error
h = str(x) + z  # 문자열 결합
print(h)

i = x * z  # 숫자 * 문자열 => 문자열 반복
print(i) 
# x = x+3
x += 3  # 줄이기 가능
print(x)

# x++    # ++, -- 안됨

j = x > 10
print(j)

# && : and
# || : or
# ! : not

k = (x > 10) and (y < 3)
l = not k

# m : x가 5이상, 10이하: True / 아니면 False 담아서 출력
# m = (x >= 5) and (x <= 10)
m = (5 <= x <= 10)
print(m)

#####################################################

# 3항 연산자
# [참일때의 값] if [조건식] else [거짓일때의 값]
# 정수를 하나 입력받아서 => 그게 짝수면 '짝수' , 홀수면 '홀수'출력

n = 5
print('짝수' if(n%2==0) else '홀수')

# 위의 버전이 너무 가독성이 안좋아서 python 3.8 버전 이후로...
# [조건식]and[참일때의 값]or[거짓일때의 값]
print(n%2 ==0 and "짝수" or "홀수")  
