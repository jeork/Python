# http://openAPI.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/SearchParkInfoService/1/132/

# 전체 공원 데이터 중에
#    공원이름(PK), 공원 소개, 개원일, 주소
#    => mongodb에 넣고
# 다 넣었으면 => 출력(console)

# 연결
from pymongo.mongo_client import MongoClient
from http.client import HTTPConnection
from json import loads
hc = HTTPConnection("openAPI.seoul.go.kr:8088")
hc.request("GET", "/4f626857416f6c6c3632586a416843/json/SearchParkInfoService/1/132/")

resBody = hc.getresponse().read()
park = loads(resBody)
con = MongoClient("192.168.0.22")
db = con.jul29

# for p in park['SearchParkInfoService']['row']:
    # db.jul29_park.insert_one({"_id" : p['P_PARK'],
                              # "p_list_content" : p['P_LIST_CONTENT'],
                              # "open_dt" : p['OPEN_DT'],
                              # "p_addr" : p['P_ADDR']})

p = db.jul29_park.find()

for l in p:
    print(l["_id"])
    print(l["p_list_content"])
    if l['open_dt']=="":
        print(" - ")
    else:
        print(l['open_dt']
    )
    print(l["p_addr"])
    print("------")

con.close()