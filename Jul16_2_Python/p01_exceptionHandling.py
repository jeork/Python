# 정수 2개 입력받아서 앞의 숫자를 뒤에 숫자로 나눴을 때 그 몫을 출력

try:
    x = int(input('x : '))
    y = int(input('y : '))
    print(x//y)
    
    l = [1,23,456]
    print(l[y])

except Exception as asdf:       # 일괄적으로 처리
    print(asdf)                 # 무슨 내용인지 알고 싶을 때
    
# except ZeroDivisionError:     # 하나씩 처리
    # print('0?')
# except IndexError:
    # print('not in list')
    
# try문에서 else를 사용하는 이유는, 단순 성능적인 부분이 아니라
# 에러가 발생할 가능성이 있는 부분과 그렇지 않은 부분을 정확히 구분지어
# 작성자의 의도를 명확하게 하기 위함    
else:
    print("문제가 없으면 실행")

finally:
    print("문제가 있든 없든 무조건 실행(return보다 먼저 수행)")    
