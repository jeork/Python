# 기상청 (주소값 구해서)
# 기상청 xml => DB에 적재
# 시간대  / 기온 / 최고기온 / 날씨(한글) / 바람의 방향(한글)

# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4136025600 
from cx_Oracle import connect
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4136025600")
res = hc.getresponse()
resBody = res.read()

con = connect("oj2/1@localhost:1521/xe")
cur = con.cursor()

for w in fromstring(resBody).getiterator("data"):
    w_hour = w.find("hour").text
    w_temp = w.find("temp").text
    w_tmx = w.find("tmx").text
    w_wfKor = w.find("wfKor").text
    w_wdKor = w.find("wdKor").text
    sql = f"insert into jul19_weather values(jul19_weather_seq.nextval,'{w_hour}','{w_temp}','{w_tmx}','{w_wfKor}','{w_wdKor}')"
    cur.execute(sql)
    if cur.rowcount==1:
        print("성공")

con.commit()
con.close()
print("END")    
