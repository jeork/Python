
#조건문 : 흐름 제어
#
# if True: 
    # print("와 조건문")
# if False:
    # print("no")
    #
# print(10+2>8+3)
# print(10+2*2>8+3*2)
# print(((10+2)>3)and(6+4==10))

# 놀이동산 >> A: 성인, 150이상(값은 입력받아서)
# 입력시에 => 탑승 가능 or 탑승 불가 출력

# age = int(input('나이 입력 : '))
# height = int(input('키 입력 : '))
#
# if age>=20 and height>=150:
    # print('탑승 가능')
# else:
    # print('탑승 불가')
# print("탑승가능" if (age>=20)and(height>=150) else "탑승 불가")
# print((age >=20 and height>=150)and "탑승가능" or "탑승 불가")

# 점수 입력 => 
# 80점 이상은 'A'
# 70점 이상은 'B'
# 60점 이상은 'C'
# 나머지는 'D'를 출력

# score = int(input('점수 입력: '))
#
#
# if score>=80:
    # print('A')
# elif score>=70:
    # print('B')
# elif score>=60:
    # print('C')
# else:
    # print('D')

#in, not in
abc ={"name" : "비버", "age" : 19, "phone" : "010-1111-2222"}

print("name" in abc)
print(20 in abc.values())
print("height" not in abc)

