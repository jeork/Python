from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.22")
db = con.jul29

# 음식 메뉴와 가격을 입력받아서 mongodb에 저장하기
m = input("메뉴 이름 : ")
p = int(input("가격  : "))

db.jul29_lunch.insert_one({"_id" : m, "price" : p})

con.close()
print('Success !')