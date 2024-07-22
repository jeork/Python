from bs4 import BeautifulSoup
import requests
from urllib3 import request
from urllib.parse import quote


# 검색어를 입력했을 때,
# 관련 뉴스 내용 중 뉴스 제목들을 콘솔에 출력
# url 주소 뒤에 요청파라미터로 start=숫자를 넣으면
# 관련 뉴스 내용 5페이지 까지의 뉴스 제목들을 콘솔에 출력
q = quote(input("검색어  : "))
s = int(input("start = "))
url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&ssc=tab.news.all&query={q}&start={s}"
response = requests.get(url)

# def getTitle(address, q):
    # for i in range(0,5):
        # # 1페이지 : 1~10 / 2페이지 : 11~20 / 3페이지 : 21~30 / ...
        # print(f"============= {i+1} 페이지 =============")
        # start = 10 * i + 1 # 1/ 11/ 21/ 31/ 41
        # addr = address + q
        # addr +=""+str(start) 
        #


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html,'html.parser')

    # #sp_nws1 > div.news_wrap.api_ani_send > div > div.news_contents > a.news_tit
    ul = soup.select_one('ul.list_news')
    titles = ul.select('li>div>div>div.news_contents>a')
    
    for title in titles:
        print(title.text)
else:
    print(response.status_code)