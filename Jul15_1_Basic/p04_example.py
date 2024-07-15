import random


# 로또 번호뽑기(1~45 정수 중 6개) => 중복 x => 출력
num_list = [] # 랜덤으로 뽑은 숫자를 담을 list
cnt= 0

while cnt < 6:
    ran_num = random.randint(1,45)
    if ran_num not in num_list : # 뽑은 숫자가 list안에 없다면(중복처리)
        num_list.append(ran_num) # list에 뽑은 숫자 추가
        cnt+=1

for n in num_list:
    print(n, end=' ')
    
    