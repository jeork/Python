# http://openAPI.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/

# 구 이름, 미세먼지, 초미세먼지의 정보를 DB에 담기
#    (여러 기간에 걸쳐 이 데이터를 모은다고 가정)
from http.client import HTTPConnection
from json import loads
from xml.etree.ElementTree import fromstring

from cx_Oracle import connect


hc = HTTPConnection("openAPI.seoul.go.kr:8088")
hc.request("GET","/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()

con = connect("oj2/1@localhost:1521/xe")
cur = con.cursor()

seoulAir = loads(resBody)
seoulAir2 = seoulAir['RealtimeCityAir']['row']
for s in seoulAir2:
    msrste_nm = s['MSRSTE_NM']
    pm10 = s['PM10']
    pm25 = s['PM25']
    
    sql = "insert into jul19_seoulair values("
    sql +="jul19_seoulair_seq.nextval, "
    sql +=f"'{msrste_nm}', "
    sql +=f"'{pm10}', "
    sql +=f"'{pm25}')"
    cur.execute(sql)

con.commit()
con.close()
print("성공")