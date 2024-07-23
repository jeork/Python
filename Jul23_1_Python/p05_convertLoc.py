# Table 데이터 => 번호값 제외한 모든 데이터 => csv파일 담는 작업
from cx_Oracle import connect

con = connect("oj2/1@localhost:1521/xe")
cur = con.cursor()
sql = "select * from jul23_map"

cur.execute(sql)

f = open("C:/Users/sdedu/Desktop/data/loc.csv","w",encoding="UTF-8")

for pn,p,x,y in cur:
    f.write(f"장소 이름 : {pn}\n전화번호 : {p}\n위도 : {x}\n경도 : {y}\n\n")
    
print('완료')

f.close()
con.close()
