# Java (NULL) = python (None)
import random
import time
# 가위바위보 (함수) => 한번 질 때까지 => 총 몇번 이겼는 지 출력
def ask():
    a = int(input('1.가위 2.바위 3.보 : '))
    return (1<=a and 3>=a) and a or ask() 

def rand_num():
    return random.randint(1, 3)

    
def result(user, com):
    if user - com == 0:
       return 'draw'
    elif user - com == -1 or user - com == 2:
        return 'lose'
    else:
        return 'win'


cnt = 0
while True:
    user = ask()
    com = rand_num()
    if result(user, com) == 'lose':
        print('졌습니다')
        print('{}번 이겼습니다'.format(cnt))
        break 
    elif result(user, com) == 'draw':
        print('비겼습니다')
    else:
        print('이겼습니다')    
        cnt += 1
        
        
        
        
