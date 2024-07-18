from cx_Oracle import connect
try:
    c = connect("oj2/1@localhost/xe")
    print("성공")
except Exception as e:
    print(e)
c.close()