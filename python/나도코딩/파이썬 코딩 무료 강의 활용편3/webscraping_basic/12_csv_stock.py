import csv
import requests
from bs4 import BeautifulSoup

filename = "시가총액1-200.csv"
# f = open(filename, "w", encoding="utf-8", newline="")
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# 리스트 형태로 csv파일에 제목을 입히기 위해 실시
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실"
# ["N","종목명","현재가"....]
title = list(map(str, title.split()))
print(type(title))
writer.writerow(title)

for page_num in range(1, 3):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={page_num}"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <=1:    # 의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)   # writer.writerow() 여기서 괄호에 들어갈 값은 리스트 형태여야함.