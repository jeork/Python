# Python의 시각화를 위한 Library - matplotlib

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

name = []
count = []

with open ("C:/Users/sdedu/Desktop/ThreeKingdoms/ThreeKingdoms/tk.csv","r",encoding="UTF-8")as f:
    for line in f.readlines():
        line = line.replace("\n", "").split(",")
        name.append(line[0])
        count.append(int(line[1]))
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font",family = fontName)

c = ['yellow', '#B2CCFF', '#FFA7A7']
# 막대그래프 - 절대적인 값 비교 
# plt.bar(name, count, width=0.4, color=c)
# plt.title('Three Kingdoms')
# plt.xlabel('name')
# plt.ylabel('count')
# plt.xticks(range(len(name)),name)    # 눈금 설정
# plt.show()

# 파이 차트 (pie)
plt.pie(count, labels=name, colors=c, shadow=True, explode=(0.1, 0.1, 0.1))
# explode = 각 항목이 원점에서 튀어나오는 정도
plt.title('Three Kingdoms')
plt.show()