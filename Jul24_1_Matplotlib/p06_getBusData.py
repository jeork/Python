# http://openapi.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/1/5/20151101/
from http.client import HTTPConnection
from json import loads

# 2021 ~ 2023년 3년치 데이터를
# 연, 월, 일, 노선번호, 정류장명(역명), 승차 총승객수, 하차 총승객수
# 연도별로 csv파일에 저장

# 정류장명(역명) => 혹시 ,가 들어있을 수 있으니
#     => ,를 .로 바꿔서 저장
# 인원수 관련 => 정수형태로 저장
date=""
k = "4f626857416f6c6c3632586a416843"
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for i in range(2021,2024):
    f = open(f"C:/Users/sdedu/Desktop/data/bus/bus{i}.csv","w",encoding="UTF-8")
    for j in range(1,13):
        for j2 in range(1,32):
            date=str(i) + '%02d'%(j) + '%02d'%(j2)
            print(date)
            
            hc.request("GET",f"/{k}/json/CardBusStatisticsServiceNew/1/1/{date}")
            resBody = hc.getresponse().read()
            bus = loads(resBody)
            
            if 'RESULT'in bus.keys():
                    break
            else:
                list_total_count = bus['CardBusStatisticsServiceNew']['list_total_count']
                for j3 in range(1000, list_total_count,1000):
                    start = j3-999
                    hc.request("GET",f"/{k}/json/CardBusStatisticsServiceNew/{start}/{j3}/{date}")
                    resBody = hc.getresponse().read()
                    bus = loads(resBody)
                    for b in bus['CardBusStatisticsServiceNew']['row']:
                        f.write(str(b['USE_YMD'])+" ")
                        f.write(str(b['RTE_NO'])+" ")
                        f.write(b['SBWY_STNS_NM']+" ")
                        f.write(str(b['GTON_TNOPE'])+" ")
                        f.write(str(b['GTOFF_TNOPE'])+" ")
                        f.write("\n")
f.close()            
