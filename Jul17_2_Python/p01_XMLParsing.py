from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http 통신

# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4136025600
hc = HTTPConnection("www.kma.go.kr")    # 서버 주소
hc.request("GET","/wid/queryDFSRSS.jsp?zone=4136025600")    # 요청

res = hc.getresponse()  # 응답 가져옴
resBody = res.read()    # 응답 내용
# print(resBody)


print(resBody.decode()) # 출력(한글처리)
################################################
# XML Parsing

# kmaWeather = fromstring(resBody)
# print(kmaWeather)
# weathers = kmaWeather.iter("data") # data태그 접근
# print(weathers)
# for w in weathers:
    # print(w)
    #
################################################
print("--------------")

for w in fromstring(resBody).getiterator("data"):
    print(w.find("hour").text)
    print(w.find("temp").text)
    print(w.find("wfKor").text)
    print("--------------")

