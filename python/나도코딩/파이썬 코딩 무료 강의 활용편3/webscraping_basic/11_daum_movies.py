import requests
from bs4 import BeautifulSoup



for year in range(2015, 2020):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images, start=1):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):      # //로 시작하면
            image_url = "https:" + image_url
        print(image_url)
        image_res =  requests.get(image_url)
        image_res.raise_for_status()

        with open(f"movie_{year}_{idx}.jpg", "wb") as f:
            f.write(image_res.content)      # res가 가진 content 정보를 파일로 쓰는 것.
        
        if idx >= 5:    # 상위 5개 이미지까지만 받아옴
            break