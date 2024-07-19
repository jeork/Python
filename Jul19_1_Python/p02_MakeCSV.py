# csv파일로 만들기(번호, 시간, 온도, 최고기온, 날씨, 바람속도 의 형태)
from cx_Oracle import connect
from xml.etree.ElementTree import fromstring
from http.client import HTTPConnection

con = connect("oj2/1@localhost:1521/xe")

    
f = open("C:/Users/sdedu/Desktop/data/jul19_weather.csv","a",encoding="UTF-8")
sql = "select * from jul19_weather"
cur = con.cursor()
cur.execute(sql)

for no,hour, temp, tmx, wfkor, wdkor in cur:
    f.write(f"{no},{hour},{temp},{tmx},{wfkor},{wdkor}\n")
    

f.close()
con.close()
print("성공")