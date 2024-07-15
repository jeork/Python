l = [123, 45, 6, 78, 910]

for ll in l:
    print(ll)
    
# ㅋ 을 10번 출력
for i in range(0, 10):
    print('ㅋ')

# 1~20까지의 정수 중에서 홀수만 출력
# for i in range(1, 21, 2):
    # print(i)
    #
# while True:
    # y = int(input("y : "))
    # if y % 2 == 0:
        # print("짝수")
        # break;

ll={"컴퓨터","모니터","키보드","마우스"}
for i,v in enumerate(ll):
    print(i+1) 
print("===============")


score = [10, 54, 56, 70, 70, 87, 65, 99, 91, 88]
max=0
index=0
# 1등 학생은 몇번째? / 점수는 몇점?/ 출력
for i,v in enumerate(score):
    if max < v:
        max=v 
        index=i
print(index,max)
    
