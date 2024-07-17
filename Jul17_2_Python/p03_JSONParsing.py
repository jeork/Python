# 42008a8c8e7402a3fc9d3b1a7df8fee9
from xml.etree.ElementTree import fromstring
from http.client import HTTPSConnection
from json import loads


# https://api.openweathermap.org
# /data/2.5/weather?q={city name}&appid={API key}
# 도시 이름 : 입력 (영어)
# 요청파라미터 추가 O
# 응답 내용 출력까지
city = input('도시 이름 : ')
apiKey = "42008a8c8e7402a3fc9d3b1a7df8fee9"
hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?q="+city+"&appid="+apiKey+"&units=metric&lang=kr" )

res = hc.getresponse()

resBody = res.read()
print(resBody.decode()) # 여기까지가 HTTP통신

weatherData = loads(resBody) #JS => Python
print(weatherData)

# dict : {"key" : "value"}
# list : [1, 2, 3] => 인덱스 값으로 

l1 = [1,2,3]                    # python : list / JS : array
d={"name" : "홍길동", "age" : 30} # python : dict / JS : object
# 날씨, 기온, 체감기온, 습도, 바람속도
# 데이터를 콘솔창에 출력
# dict / list 잘 확인하면서!

# 단 하나의 데이터 O => 반복문이 필요없음!  

temp = weatherData['main']['temp']
weather = weatherData['weather'][0]['description']
feels_like = weatherData['main']['feels_like']
humidity = weatherData['main']['humidity']
windSpeed = weatherData['wind']['speed']
print("--------------")
print(f"기온 :{temp}도")
print(f"날씨 :{weather}")
print(f"체감기온 :{feels_like}도")
print(f"습도 :{humidity}")
print(f"바람속도 :{windSpeed}")

