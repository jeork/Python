from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

# https://openapi.naver.com/v1/search/shop.xml
# jUIQ8bS91lcUGh54_2Qx
# OIKJ365nFE
# 상품명 : 입력
# xml 파싱해서 
# 문서의 상품 이름 / 최저가 / 브랜드 / 대분류 카테고리 정보를 출력
# q = input('상품명 : ')
q = "apple"
# 한글 값 들어가면 안되기 때문에
# URLEncoding해서 주소로 넘겨줄 것

q = quote(q)  # (urllib.parse)
id = "jUIQ8bS91lcUGh54_2Qx"
secret = "OIKJ365nFE"

hc = HTTPSConnection("openapi.naver.com")
# request 함수의 body
 #    :요청할 때 데이터를 보내야 하는 경우에 body에 담아서 보냄

h = {
    "X-Naver-Client-Id" : "jUIQ8bS91lcUGh54_2Qx",
    "X-Naver-Client-Secret" : "OIKJ365nFE" 
    }
hc.request("GET", "/v1/search/shop.xml?query=" + q, headers=h)

# hc.request.add_header("X-Naver-Client-Id",id)
# hc.request.add_header("X-Naver-Client-Secret",secret)

res = hc.getresponse()
resBody = res.read()

for p in fromstring(resBody).iter("item"):
    print(p.find("title").text)
    print(p.find("lprice").text)
    print(p.find("brand").text)
    print(p.find("category1").text)
    