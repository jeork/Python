# str
from audioop import reverse
from itertools import repeat


s = "0123456789"
print(s)

print(s[0])
print(s[0:6])       # (0번째부터 (6-1)번째 까지의 문자열
print(s[2:10:2])    # (2번째부터 (10-1)번째 까지의 문자열을 2칸씩 건너서 출력

# list : 리스트 (순서 O, 중복 O, 수정 O, 삭제 O)
a = [123,4,56,789,1011]
print(a[0])
print(a[0:3])
print(a[0:5:2])
print(a[-1])        # 뒤에서 첫번째

print(len(a))       # 요소의 갯수
a.append(s)         # 끝에 요소 추가
a.insert(2,1415)    # 중간 요소 추가
a[2]= 55            # 수정
del a[2]            #삭제
 
##a.sort()           # 오름차순 정렬
#a.sort(reverse=True) #내림차순
print(a)

# Tuple : 순서 

tuple1=('1','2','3')
# del tuple1[0]     # 삭제 불가
# tuple[0] = 'c'    # 수정 불가

t=(1,2,3,4,5,4,4)
print(t.index(5))   # index 해당 위치에 있는 값을 반환
print(t.count(3))   # index안의 요소가 튜플안에서 몇개가 있는지 그 갯수를 반환

# a1 = 20
# b1 = 10
(a1, b1)= (10, 20)  # 값을 줄 때 튜플로 묶어서 O / 소괄호 없어도 됨
print(a1, b1)       # 10, 20
(a1, b1) = (b1, a1) # swap
print(a1, b1)       # 20, 10


# Set(집합) : 중복 제거, 순서는 랜덤
s = {"ㅋ","ㅋ","ㄹ","ㅃ","ㅃ"}
print(len(s))
print(s)
s=list(s)
print(s)

# Dict(=map)
d = {"name" : "곽두팔", "age":100}
print(type(d))

print(d["name"])    # 곽두팔
print(d["age"])     # 100

# Range
r = range(10)       # 0 ~ (10-1)까지의 범위
print(r, type(r))

r2 = range(2,10)    # 2 ~ (10-1)까지의 범위
r3 = range(2,10,3)  # 2 ~ (10-1)까지의 범위를 3씩 건너서

# 0~9까지 있는 list 출력
r2=range(0,10)
r2=list(r2)
print(r2)

# 1~20 중 홀수만 있는 list 출력
r3=list(range(1,21,2))
print(r3)
