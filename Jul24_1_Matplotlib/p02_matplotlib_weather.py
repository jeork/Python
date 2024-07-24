# 기상청 데이터
#    => 각 3시간별 기온(temp)와 습도(reh)를 선 그래프로 표현
# http://www.kma.go.kr
# /wid/queryDFSRSS.jsp?zone=4136025600
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

plt.rcParams['axes.unicode_minus'] = False  # 음수부호 제대로 안나올 때 처리
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

hc = HTTPConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4136025600")
resBody = hc.getresponse().read()

xData = ["1)12", "1)15", "1)18", "1)21", "1)24", "2)3", "2)6", "2)9",
         "2)12", "2)15", "2)18", "2)21", "2)24", "3)3", "3)6", "3)9",
         "3)12", "3)15", "3)18", "3)21"]
yData1 = []
yData2 = []
for w in fromstring(resBody).getiterator("data"):
    yData1.append(w.find("temp").text)
    
    yData2.append(w.find("reh").text)

x1 = plt.subplot()
x1.set_xlabel("시간")
x1.set_ylabel("기온")
p1 = x1.plot(xData, yData1, "r-o")

x2 = x1.twinx()
x2.set_ylabel("습도")
p2 = x2.plot(xData, yData2, "b-o")
x1.legend(p1 + p2, ["기온", "습도"])
plt.show()
