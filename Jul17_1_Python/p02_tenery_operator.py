# 3항 연산자


def getWeight():
    weight = float(input("몸무게 : "))
    
    # 1. [참일때의 값] if [조건식] else [거짓일때의 값]
    return weight if weight >= 0 else weight * -1

    # 2. [조건식] and [참일때의 값] or [거짓일때의 값]
    return weight >= 0 and weight or weight * -1

# 3항 연산자 중첩    
    # [참1] if [조건1] else [참2] if [조건2] else ... [거짓일때의 값]
    
# 15, 16, 17을 list에 담고
# 리스트 각각의 요소가 2의 배수인지 3의 배수인지, 아니면 둘다 아닌지를 출력

n = [15, 16, 17]
for val in n:
    print(f'{val} : 2의 배수') if (val % 2 == 0) else print(f'{val} : 3의 배수') if (val % 3 == 0) else print(f'{val} : 둘다 아님')
    
# 길어진다면 if - elif - else 가 좀 더 보기 편함
for val in n:
    if(val%2==0):
        print(f'{val}은 2의 배수')
    elif(val%3==0):
        print(f'{val}은 3의배수')
    else:
        print(f'{val}은 2, 3의 배수 둘다 아님')
