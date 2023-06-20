import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.15 Safari/537.36"}
# res = requests.get("http://google.com")
res = requests.get(url, headers=headers)
res.raise_for_status()  # 이것을 사용하게 되면 오류발생시 오류를 출력하고 끝내버림

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)