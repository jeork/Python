# 원두를 검색해서
# 그 원두를 사용하는 커피의 종류 갯수, 평균가를 출력
from cx_Oracle import connect

con = connect("oj2/1@localhost:1521/xe")
b = input('원두 : ')
sql = f"select COUNT(c_bean), AVG(c_price) from jul18_coffee where c_bean in '%s'"%b
cur = con.cursor()
cur.execute(sql)

for i, j in cur:
    print(f"커피의 종류 : {i}개\n평균가 : {j:.1f}원")
    
con.close()