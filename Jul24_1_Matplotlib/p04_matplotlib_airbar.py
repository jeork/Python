# http://openAPI.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/
# 4f626857416f6c6c3632586a416843
# 서북권, 도심권, 동북권, ... 의 미세먼지 / 초미세먼지
# MSRRGN_NM / PM10 / PM25
# 각각 평균값을 bar그래프로 표현 (누적합)
from http.client import HTTPConnection
from json import loads
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

k = "4f626857416f6c6c3632586a416843"
hc = HTTPConnection("openAPI.seoul.go.kr:8088")
hc.request("GET", f"/{k}/json/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
airData = loads(resBody)

yyData={'도심권' : 0, '서북권' : 0,'동북권' : 0, '서남권' : 0, '동남권' : 0}
yyData2={'도심권' : 0, '서북권' : 0,'동북권' : 0, '서남권' : 0, '동남권' : 0}
cnt={'도심권' : 0, '서북권' : 0,'동북권' : 0, '서남권' : 0, '동남권' : 0}
xData=[]
yData=[]
yData2=[]

for a in airData['RealtimeCityAir']['row']:
    xData.append(a['MSRRGN_NM'])
    yyData[f'{a["MSRRGN_NM"]}']+=a['PM10']
    yyData2[f'{a["MSRRGN_NM"]}']+=a['PM25']
    cnt[f'{a["MSRRGN_NM"]}']+=1

for k in yyData:
    yData.append(round(yyData[k] / cnt[k]))
    yData2.append(round(yyData2[k] / cnt[k]))
    
xData = set(xData)  
xData = list(xData) # 중복제거

print(xData)
print(yData)
print(yData2)

plt.bar(xData,yData,color="#FFC19E")
plt.bar(xData,yData2,color="#B5B2FF",bottom=yData)
plt.legend(["미세먼지","초미세먼지"])
plt.show()