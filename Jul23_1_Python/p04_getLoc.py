# dd77f7c6313f3f8d46ae3d3da9bfc473
# 37.5111158
# 127.098167
from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote
from cx_Oracle import connect

# https://dapi.kakao.com/v2/local/search/keyword.${FORMAT}    
# Authorization: KakaoAK dd77f7c6313f3f8d46ae3d3da9bfc473
# json

# 검색어를 입력
#    => 위도 / 경도 지정
#    => 반경 1km이내에 있는
#    => 검색어에 대한 위치정보

#    => 장소명(업체명), 전화번호, 경도, 위도
#    => DB에 저장
#    => 전화번호 : 없는 부분은 ' - '으로 대체
#    => 경도, 위도 : 소수점 6자리까지

q = quote(input('검색어 : '))
h = {"Authorization" : "KakaoAK dd77f7c6313f3f8d46ae3d3da9bfc473"}
hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", f"/v2/local/search/keyword.json?y=37.511115&x=127.098167&radius=1000&query={q}", headers=h)
resBody = hc.getresponse().read()
data = loads(resBody)

con = connect("oj2/1@localhost:1521/xe")
cur = con.cursor()
for d in data['documents']:
    d['x'] = round(float(d['x']),6)
    d['y'] = round(float(d['y']),6)
    place_name = d['place_name']
    phone = d['phone']
    x = d['x']
    y = d['y']
    sql = f"insert into jul23_map values('{place_name}','{phone}',{x},{y})"
    
    cur.execute(sql)
    if cur.rowcount==1:
        print("성공")
        con.commit()
        
con.    close()