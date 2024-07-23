# sss = ["ㅋㅋㅋ","ㅁㅁㅁ","ㅂㅂㅂ","ㅎㅎㅎ","ㅜㅜ","ㄷㄷㄷ"]

# for s in sss:
    # # 찾는 문자열이 존재하는 경우 : 그 문자열이 있는 인덱스값을 리턴
    # # 찾는 문자열이 존재하징 않는 경우 : -1 리턴
    # print(s.find('ㅋㅋㅋ'))
    # print(s.find('ㅁㅁㅁ'))
    # print('-------------')
    #
# 조조(맹덕), 유비(현덕), 손권(중모)
# 책을 훑어보면서... => 위의 인물들이 몇 번 언급됐는지 카운팅 하기
# 인물, 언급횟수 의 형태로 => csv파일에 저장
# for i in range(1,11):
# for i in range(1,11):
    # f = open(f"C:/Users/sdedu/Desktop/ThreeKingdoms/ThreeKingdoms/ThreeKingdoms{i}.txt","r",encoding="UTF-8")
    # f2 = open("C:/Users/sdedu/Desktop/ThreeKingdoms/ThreeKingdoms/cnt.csv","a",encoding="UTF-8")
    # j_cnt=0
    # y_cnt=0
    # s_cnt=0
    # while True:
        # data = f.readline()
        # if data.find('조조')>=0:
            # j_cnt+=1
        # if data.find('유비')>=0:
            # y_cnt+=1   
        # if data.find('손권')>=0:
            # s_cnt+=1
        # if data=="":
            # break
    # f2.write(f'----------삼국지 {i}권----------\n')   
    # f2.write(f'조조 : {j_cnt}\n')   
    # f2.write(f'유비 : {y_cnt}\n')   
    # f2.write(f'손권 : {s_cnt}\n')   
# f.close()
# f2.close()

wc = {'조조' : 0, '유비' : 0, '손권' : 0}
for i in range(1,11):
    fileName="C:/Users/sdedu/Desktop/ThreeKingdoms/ThreeKingdoms/ThreeKingdoms%d.txt"%i
    with open(fileName, "r", encoding="UTF=8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.split(" ")
            for word in line:
                if word.find('조조') !=-1 or word.find('맹덕')!=-1:
                    wc["조조"] +=1
                elif word.find('유비') !=-1 or word.find('현덕')!=-1:
                    wc["유비"] +=1
                elif word.find('손권') !=-1 or word.find('중모')!=-1:
                    wc["손권"] +=1
for key in wc:
    print(key)
for val in wc.values():
    print(val)
    
with open("C:/Users/sdedu/Desktop/ThreeKingdoms/ThreeKingdoms/tk.csv","w",encoding="UTF-8") as f:
        for k, v in wc.items():
            f.write(f"{k},{v}\n")
print("end!")
    
    