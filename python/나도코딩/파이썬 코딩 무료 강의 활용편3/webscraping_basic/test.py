# 여기서 가져옴
# https://m.blog.naver.com/ytlee64/222240488478

from selenium import webdriver
from bs4 import BeautifulSoup
import time

def init():
    global driver
    # driver = webdriver.Chrome(r'C:/path/to/chromedriver.exe') # 이 부분은 알맞게 바꿔야함
    driver = webdriver.Chrome(r'C:/path/to/chromedriver.exe')
    driver.implicitly_wait(3)
    baseurl = 'https://www.coupang.com/vp/products/36647347?itemId=135209860&vendorItemId=73624129122&sourceType=CATEGORY&categoryId=178451&isAddedCart='
    driver.get(baseurl)
    time.sleep(2)

def run0():
    button_review = driver.find_elements_by_xpath('//*[@id="btfTab"]/ul[1]/li[2]') #상담평
    print(button_review[0].text)
    button_review[0].click()
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser', from_encoding='utf-8')
    articles = soup.findAll('article', class_='sdp-review__article__list js_reviewArticleReviewList')
    
    for a in articles:
        nametag = a.find('div', class_='sdp-review__article__list__info__user') 
        headlinetag = a.find('div', class_='sdp-review__article__list__headline') 
        contenttag = a.find('div', class_='sdp-review__article__list__review__content js_reviewArticleContent')
        name = ''
        headline = ''
        content = ''
        if nametag is not None:
            name = nametag.text
        if headlinetag is not None:
            headline = headlinetag.text
        if contenttag is not None:
            content = contenttag.text
        print('-----------------------------------------', name)
        print(headline, content)

init()
run0()
