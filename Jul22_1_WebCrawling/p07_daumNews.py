from urllib.parse import quote
from bs4 import BeautifulSoup
import requests
from urllib3.util import response

# https://search.daum.net/search?w=news&q=
# %ED%95%9C%EC%9D%BC%20%EC%95%BC%EA%B5%AC 
# &enc=utf8&cluster=y&cluster_page=1&DA=DNS
# 검색어 콘솔에 입력
# 요청했을 때 나오는 결과 1 ~ 5페이지까지의 뉴스 제목을 출력
# 페이지 : p
q = quote(input('검색어 : '))

for i in range(1, 6):
    print(f"----------- {i} 페이지 -----------")
    url = f"https://search.daum.net/search?w=news&q={q}"
    url += f"&enc=utf8&cluster=y&cluster_page=1&DA=DNS&p={i}"
    response = requests.get(url)
    if response.status_code == 200:
        # res = requests.get(url)
        # soup = BeautifulSoup(res.text, 'html.parser')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('strong > a')
        for title in titles:
            print(title.text)