# UP / DOWM 게임(함수)
# 유저의 이름을 입력받고 환영하는 인사를 출력
# (컴퓨터) 1~100사이의 랜덤함 숫자를 하나 뽑아서
# 유저에게 정답을 입력하게 했을 때,
# 범위안의 숫자가 아니면 다시입력하도록 함
# 입력한 숫자가 정답보다 작으면 'UP' 크면 'DOWN' 출력
# 정답을 맞췄을 때는 몇 번만에 맞췄는지 출력 + 종료
# 정답 기회는 총 10번
import random

user_name = input('이름: ')
print('환영합니다 {}님'.format(user_name))

rand_num = random.randint(1, 100)
cnt = 1

while True:
    user_num = int(input('숫자를 입력하세요: '))
    
    while user_num<1 or user_num>100:
        user_num = int(input('다시 입력하세요: '))
        
    if rand_num==user_num:
        print('{}번만에 정답!'.format(cnt))
        break
    elif cnt>= 10:
        print('기회 끝!')
        break
    elif rand_num>user_num:
        print('UP!')
        cnt+=1
    else:
        print('DOWN!')
        cnt+=1
    