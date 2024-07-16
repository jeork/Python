from datetime import datetime
# 현재시간 날짜
now = datetime.today()  # 자동완성 주의 ( _datetime X )
print(now)

# 특정 시간 날짜
yesterday = datetime(2024, 7, 15)
print(yesterday)
print(type(yesterday))
print(yesterday.year)
print(yesterday.month)
print(yesterday.day)

# 생년월일을 입력받아서 나이를 계산해주는 프로그램

birth = input('생년월일 : ')
curYear = now.year
year = int(birth[:4])
age = curYear-year
print(age)

# strptime : str => datetime
bd = datetime.strptime(birth,"%Y/%m/%d")
print(type(bd))
# strftime : datetime => str
bd = datetime.strftime(bd,"%A")
print(bd) 