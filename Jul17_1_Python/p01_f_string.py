# 좋아하는 음료이름, 마시는 횟수 = 입력받아서 그 내용을 출력
from datetime import datetime

# beverage = input('좋아하는 음료이름 : ')
beverage = "오트사이드"
# frequency = int(input('하루에 마시는 횟수 : '))
frequency = 1

print("저는 {}를 좋아하고요 하루에 {}번 마십니다".format(beverage, frequency))
print(f"저는 {beverage}를 좋아하고요 하루에 {frequency}번 마십니다")

# 소수점 반올림 표현
    
n = 1.125
# n=1.135

print(f"{n}")  # 1.125 / 1.135
print(f"{n:.1f}")  # 1.1 / 1.1
print(f"{n:.2f}")  # 1.12 / 1.14 

# 문자 정렬

s1 = "left"
result1 = f"|{s1:<10}|"
print(result1)

s2 = "mid"
result2 = f"|{s2:^10}|"
print(result2)

s3 = "right"
result3 = f"|{s3:>10}|"
print(result3)

num = 10
result4 = f"my age : {num},{{num}}, {{{num}}}"
print(result4)


# f-string과 dict
d = {
        "name" : "Beaver",
        "gender" : "남자",
        "age" : 100 
    }
result5 = f"name : {d['name']}, gender: {d['gender']}, age:{d['age']}"
print(result5)


# f-string과 list
n = [100, 200, 300]
# 각 요소를 출력
print(f"list : {n[0]},{n[1]},{n[2]}")

for v in n:
    print(f"리스트 요소 :{v}")

num2 = 1234567890
print(f"{num2:,}")

date1 = datetime.today()
print(date1)

# 연-월-일 => 요일
print(f"{date1:%Y-%m-%d}is in a {date1:%A}")

