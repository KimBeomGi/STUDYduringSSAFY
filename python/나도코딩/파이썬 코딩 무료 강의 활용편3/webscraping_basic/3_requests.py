import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocodingssssss.tistory.com")
res.raise_for_status()  # 이것을 사용하게 되면 오류발생시 오류를 출력하고 끝내버림

# print("응답코드 :", res.status_code)    # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code,"]")

# res.raise_for_status()
# print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)