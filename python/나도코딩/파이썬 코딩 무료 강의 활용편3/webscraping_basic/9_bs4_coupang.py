import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.15 Safari/537.36"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.15 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) 
# print(items[0].find("div",attrs={"class":"name"}).get_text())
for item in items:
    
    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()  # 제품명
    
    # 애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다> ")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    # 리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})   # 평점
    if rate:
        rate = rate.get_text()
    else:
        # rate = "평점 없음"
        print(" <평점 없는 상품 제외합니다.> ")
        continue
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})   # 평점수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()  # 예 : (26)
        rate_cnt = rate_cnt[1:-1]
        # print("리뷰 수", rate_cnt)
    else:
        # rate_cnt = "평점 수 없음"
        print(" <평점 수 없는 상품 제외합니다.> ")
        continue
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price+"원", rate+"점", rate_cnt+"명")
    
    


# # 아래는 gpt가 짜준거

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.15 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# items = soup.select("li.search-product")
# if len(items) > 0:
#     first_item = items[0]
#     item_name = first_item.find("div", class_="name").get_text()
#     print(item_name)
# else:
#     print("상품을 찾을 수 없습니다.")



# import requests
# import re
# from bs4 import BeautifulSoup

# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.15 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# print(res.text)

# items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) 
# print(items[0].find("div", attrs={"class":"name"}).get_text())








# # 아래를 해봤는데 
# import requests
# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.15 Safari/537.36"}
# # res = requests.get("http://google.com")
# res = requests.get(url, headers=headers)
# res.raise_for_status()  # 이것을 사용하게 되면 오류발생시 오류를 출력하고 끝내버림

# with open("iscan.html", "w", encoding="utf8") as f:
#     f.write(res.text)

# # # 아래처럼 오류가 발생했음
# # PS C:\Users\dyd13\Desktop\STUDYduringSSAFY\python\나도코딩\파이썬 코딩 무료 강의 활용편3\webscraping_basic> & "c:/Users/dyd13/Desktop/STUDYduringSSAFY/python/나도코딩/파이썬 코딩 무료 강의 활용편3/webscraping_basic/venv/Scripts/python.exe" "c:/Users/dyd13/Desktop/STUDYduringSSAFY/python/나도코딩/파이썬 코딩 무료 강의 활용편3/webscraping_basic/crawl.py"
# # Traceback (most recent call last):
# #   File "c:\Users\dyd13\Desktop\STUDYduringSSAFY\python\나도코딩\파이썬 코딩 무료 강의 활용편3\webscraping_basic\crawl.py", line 23, in <module>
# #     res.raise_for_status()  # 이것을 사용하게 되면 오류발생시 오류를 출력하고 끝내버림
# #     ^^^^^^^^^^^^^^^^^^^^^^
# #   File "C:\Users\dyd13\Desktop\STUDYduringSSAFY\python\나도코딩\파이썬 코딩 무료 강의 활용편3\webscraping_basic\venv\Lib\site-packages\requests\models.py", line 1021, in raise_for_status
# #     raise HTTPError(http_error_msg, response=self)
# # requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreD