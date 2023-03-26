import requests
import json


# finedust_json=requests.get('https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EA%B2%BD%EB%B6%81&pageNo=1&numOfRows=100&returnType=JSON&serviceKey=jxFZjVGuhp0SD8lBkTb1D5aGwcnnvkCiT%2FKvityy8qkQLQGdhh7pQJOQa0bpRY9zsouaF0QhBYD6p5vxXCSitA%3D%3D&ver=1.0').text
url= 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EA%B2%BD%EB%B6%81&pageNo=1&numOfRows=100&returnType=JSON&serviceKey=jxFZjVGuhp0SD8lBkTb1D5aGwcnnvkCiT%2FKvityy8qkQLQGdhh7pQJOQa0bpRY9zsouaF0QhBYD6p5vxXCSitA%3D%3D&ver=1.0'
response=requests.get(url).text
response_dict = json.loads(response)
items = response_dict['response']['body']['items'] #response와 body는 딕셔너리, items는 리스트 문이였음 그래서 못풀고 있었음.
# for item in items:
#     location = item['stationName']  # 또 stationName과 pm10Value 값 등은 딕셔너리로 되어있어서, 리스트내에서 딕셔너리를 추출해냄.
#     pm10Value = item['pm10Value']
#     pm25Value = item['pm25Value']
#     print(f'{location}지역 미세먼지 농도는 {pm10Value}, 초민세먼지 농도는{pm25Value}입니다.')

# print(type(items))


for item in items:
    location = item['stationName']  # 또 stationName과 pm10Value 값 등은 딕셔너리로 되어있어서, 리스트내에서 딕셔너리를 추출해냄.
    dataTime = item['dataTime']
    pm10Value = item['pm10Value']
    pm25Value = item['pm25Value']
    if location == '진미동':        # 위 location에서 stationName의 값을 정해주고 출력해주니 예시로 든 진미동 미세먼지 농도만 출력이 가능하다.
        print(f'{dataTime}기준, {location}지역 미세먼지 농도는 {pm10Value}, 초민세먼지 농도는{pm25Value}입니다.')
