from urllib3.util import response
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# 가수, 노래 제목을 직접 입력해서 요청
# 노래 가사에 대한 내용을 출력

a = quote(input('가수 : '))
m = quote(input('노래 제목 : '))
# https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=
# NewJeans+Supernatural+%EA%B0%80%EC%82%AC
# &oquery=
# NewJeans+Supernatural

url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query={a}+{m}"
url += f"%EA%B0%80%EC%82%AC&oquery={a}+{m}"

response = requests.get(url)
res = response.text
soup = BeautifulSoup(res,'html.parser')
s = soup.select_one('div.intro_box')
r = s.select('p')
for rr in r:
    print(rr.text)
