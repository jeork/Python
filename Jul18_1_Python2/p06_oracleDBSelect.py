# input으로 숫자 2개를 입력 => 가격(오름차순)으로 정렬 => ?~? 번째까지의 평균 가격을 출력
from cx_Oracle import connect

con = connect("oj2/1@localhost:1521/xe")
start = int(input('시작 : '))
end = int(input('끝 : '))

sql = f"select avg(c_price) from (select rownum as rn, c_price from(select c_price from jul18_coffee order by c_price)) where rn between {start} and {end}"

cur = con.cursor()

cur.execute(sql)

for i in cur:   # cur 안에 tuple 형태로 결과가 담김 
    print(i)
    print(type(i))
    
con.close()