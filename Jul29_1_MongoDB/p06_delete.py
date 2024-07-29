from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.22")
db = con.jul29

# remove() / delete_one + delet_many
# db.jul29_lunch.remove({"_id" : "test"})
# db.jul29_lunch.remove({}) => mongoDB cmd 내에서 전체 데이터 삭제 시 == delete_many()

# 해당 데이터 하나만 삭제
db.jul29_lunch.delete_one({"price" : 8000})

# 해당 데이터 전체 삭제
db.jul29_lunch.delete_many({"price" : 8000})

con.close()
print('Success !')
