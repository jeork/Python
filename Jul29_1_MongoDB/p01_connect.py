# 연결
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.22")
db = con.jul29

con.close()

print('Success !')
