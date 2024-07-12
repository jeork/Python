print("파이썬^ㅡ^")

print('내', '일', '토', '요', '일', sep='ㅋ')

# 메일 주소 출력
# 전화번호 출력

print('asdasd031', 'naver.com', sep='@')
print('010', '4936', '3347', sep='-')

# end
print('파이썬이', end=' ')
print('본격적으로', end=' ')
print('시작', end=' ')
print();

# 출력 형식 (format)
print('{} and {}'.format('1번', '2번'));
print('{1} and {0} and {0}'.format('1번', '2번'));
print('{p1} and {p2}'.format(p1='Life', p2='Egg'));

# %d, %f, %s
print('%d' % 123)
print('%.2f' % 123.456)

# 10이라는 값을 0번째에, 11.11111이라는 값을 1번째에 소수점 둘째자리까지 출력
print('{0}, {1}'.format('%d' % 10, '%.2f' % 11.11111))
print('{0:d}, {1:.2f}'.format(10,11.11111))
