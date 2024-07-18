
# select 번호순으로 조회 => 번호를 입력하면 => 그 데이터가 삭제
# 999를 입력하게 되면 프로그램이 종료 => 종료하기 전까지 반복

from cx_Oracle import connect
con = connect("oj2/1@localhost:1521/xe")
cur = con.cursor()

while True:
    sql = "select * from jul18_coffee order by c_no"
    cur.execute(sql)
    for a,b,c,d in cur:
        print(a, b, c, d)
    print('---------------')
    n = int(input('삭제할 번호 입력(999:프로그램종료) :'))
    sql = f"delete from jul18_coffee where c_no={n}"
    if n==999:
        print("프로그램 종료")
        break
    else:
        cur.execute(sql)
        if cur.rowcount==1:
            print("삭제 성공")

con.close()