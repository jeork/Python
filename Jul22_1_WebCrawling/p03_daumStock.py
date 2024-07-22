from fake_useragent.fake import UserAgent
import urllib.request as req
from json import loads
ua = UserAgent 
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random) 
# 헤더 선언 : dict 형태로(key, value)
h = {
        "User-Agent" : ua.chrome,
        "referer" :  "https:/finance.daum.net/" # 이 경로를 통해 옴
    }
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청 
res = req.urlopen(req.Request(url,headers=h)).read().decode()
# 응답 데이터 확인 
# print('res : ', res)

# 응답 데이터 => python
ranking = loads(res)

for r in ranking["data"]:
    print(f"순위 : {r['rank']}, 이름 : {r['name']}, 거래가 : {r['tradePrice']}")


                  
# 순위, 주식명, 거래가를 콘솔에 출력