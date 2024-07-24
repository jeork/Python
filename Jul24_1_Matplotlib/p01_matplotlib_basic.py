import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
 
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

yData = np.array([12, 31, 1, 2])  # Numpy의 Array를 사용
xData = [1, 2, 3, 4]  # Numpy를 사용하지 않아도 내부적으로 변환

# 기본
# plt.plot(yData)
# plt.show()

# x, y
# plt.plot(xData, yData)
# plt.show()

# 축
# plt.plot(xData, yData)
# plt.xlabel("x축")
# plt.ylabel("y축")
# plt.axis([0, 10, 0, 50])    # [xmin, xmax, ymin, ymax]
# plt.show()

# title
# plt.plot(xData, yData)
# f = {"fontsize": 15, "fontweight": "light"}  # bold, light, ultralight,...
# plt.title("ㅋㅋ", loc="left")
# plt.title("ㅎㅎ", loc="center")
# plt.title("제목", loc="right",fontdict=f)
# plt.show()

# style
# plt.plot(xData,yData,"c-.h")
# plt.show()

# 색 / 선의 모양 / 마커의 모양
#    b : blue / g : green / r : red / y : yellow / k : black
#    w : white / c : cyan
#    plot함수의 color라는 옵션으로 RGB지정하는 것도 가능

# 선의 모양 
#    ' : ' : 점선 / ' - ' : 실선 / ' -- ' : dashed line / ' -. ' : 실선 + 점선
# plot 함수의 linestyle 이라는 옵션으로 지정하는 것이 가능!

# 마커의 모양 
# ' . ' : 점 / ' o ' : 동그라미 / ' v ' : 아래 삼각형 / ' ^ ' : 위 삼각형
# ' < ',' > ' : 삼각형을 외쪽, 오른쪽 / ' s ' : 사각형 / ' p ' : 오각형
# ' h ' : 육각형  / ' * ' : 별 / ' + '+ 모양 / ' x ' : x 모양
#    plot함수의 marker 라는 옵션으로 지정하는 것이 가능

# plt.plot(xData, yData, "k-x")
# plt.show()

# grid (격자)
# plt.plot(xData, yData)
# plt.grid(axis="both", color="#997700", linestyle="-.")
# plt.show()

# 눈금
# plt.plot(xData,yData)
# plt.xticks(xData, ["일", "이", "삼", "사"])
# plt.yticks(np.arange(0, 41, 10), ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"])
# plt.tick_params(axis="x",direction="inout", length=10, pad=15, 
                # color="r", labelsize=20,labelcolor="#F15F5F")
# #        x, y, both        in, out, inout
#
# plt.show()

# 선 
# plt.plot(xData,yData)
# # 실제 y값, xmin, xmax => 지정한 점을 따라서 수평선
# plt.hlines(31, 1, 2, color="r", linestyles="--")
# # 실제 x값, ymin, ymax => 지정한 점을 따라서 수직선
# plt.vlines(1, 31, 12, color="r", linestyles="--")
# plt.show()

# 선 여러개
xData = [1,2,3,4]
yData = np.array([12,31,1,2])
# yData2 = [5,66,1,10]
# plt.plot(xData, yData, "r-")
# plt.plot(xData, yData2, "g:")
# plt.legend(["빨강 데이터 ", "초록데이터"])
# plt.show()

# 선 여러개 2 ( y 축을 나눠서)
yData2 = [50,606,100,1000]
x1 = plt.subplot()  # 여러 그래프들을 동시에 시각화
p1 = x1.plot(xData, yData, "r-")
x1.set_xlabel("x축")
x1.set_ylabel("y축")

x2 = x1.twinx() # x축을 공유
p2 = x2.plot(xData, yData2, "g:")
x2.set_ylabel("y축2")
x1.legend(p1 + p2,["Red", "Green"])
plt.show()








