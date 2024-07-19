# DB에 있는 미세먼지 데이터 => csv에 저장 (데이터 콤마로 구분)
from cx_Oracle import connect

con = connect("oj2/1@localhost:1521/xe")

f = open("C:/Users/sdedu/Desktop/data/jul19_seoulair.csv","a",encoding="UTF-8")

sql = "select * from jul19_seoulair"
cur = con.cursor()
cur.execute(sql)

for no, nm, pm10, pm25 in cur:
    f.write(f"{no}, '{nm}', '{pm10}', '{pm25}'\n")
    
f.close()
con.close()
print("성공")