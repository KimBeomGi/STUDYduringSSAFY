# 네이버 증권 페이지에서 현재 KOSPI 지수 얻어오기
# 요청을 보내서 html 문자열 얻어오기
# 얻어온 결과를 beautifulsoup를 이용해서 KOSPI 지수 얻어오기
# 출력

import requests
from bs4 import BeautifulSoup
# 네이버 증권 페이지에서 현재 KOSPI 지수 얻어오기
response = requests.get('https://finance.naver.com/sise/sise_index.naver?code=KOSPI').text
# now_value = BeautifulSoup(response)
# 요청을 보내서 html 문자열 얻어오기
# print(response)
# 얻어온 결과를 beautifulsoup를 이용해서 KOSPI 지수 얻어오기
    #now_value
soup = BeautifulSoup(response, 'html.parser')
#출력
kospi_value=soup.select_one('#now_value').get_text()
print(f'현재 코스피 지수는 {kospi_value}입니다.')