from pymongo.mongo_client import MongoClient
con = MongoClient("192.168.0.22")
db = con.jul29

s = db.jul29_lunch.find()

for l in s:
    print(l["_id"])
    print(l["price"])
    print('-----------')

con.close()
print("성공!")