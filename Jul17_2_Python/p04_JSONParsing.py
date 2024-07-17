from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads


# dd77f7c6313f3f8d46ae3d3da9bfc473
# https://dapi.kakao.com/v3/search/book

# 책 이름 검색해서 책제목 - 작가 / 할인가 / 도서 소개 출력

book = quote(input('책 이름 : '))
h = {"Authorization": "KakaoAK dd77f7c6313f3f8d46ae3d3da9bfc473"}
hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", "/v3/search/book?query="+book,headers=h)

resBody = hc.getresponse().read()

bookData = loads(resBody)   # JS => Python
print(type(bookData))       # class 'dict'

books = bookData['documents']

for b in books:
    print(b['title'], '-', ', '.join(b['authors'])) # 작가 이름 두명 다 나옴
                                # .join() : list를 하나의 문자열로 만듬
                                # ', ' => 구분자.join() : list의 요소들을 지정한 구분자로 나눠
                                #                     하나의 문자열로 합쳐줌
                                # ex) ', '.join(['a','b','c',]) => a, b, c => , 로 이어줌
    print(b['sale_price'])
    print(b['contents'])
    print('-----------------')

# title = bookData['documents'][0]['title']
# authors = bookData['documents'][0]['authors']
# sale_price = bookData['documents'][0]['sale_price']
# contents = bookData['documents'][0]['contents']
# contents = contents.replace('&lt;','<').replace('&gt;','>').replace('.','.\n')
#
# print(f'책 제목 : {title}')
# print(f'작가 : {authors}')
# print(f'할인가 : {sale_price}원')
# print(f'도서 소개 : {contents}')

