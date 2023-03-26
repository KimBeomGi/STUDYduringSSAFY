import random
import json
import requests


# finedust_json=requests.get('https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EA%B2%BD%EB%B6%81&pageNo=1&numOfRows=100&returnType=JSON&serviceKey=jxFZjVGuhp0SD8lBkTb1D5aGwcnnvkCiT%2FKvityy8qkQLQGdhh7pQJOQa0bpRY9zsouaF0QhBYD6p5vxXCSitA%3D%3D&ver=1.0').text
finedust_json=requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EA%B2%BD%EB%B6%81&pageNo=1&numOfRows=100&returnType=JSON&serviceKey=jxFZjVGuhp0SD8lBkTb1D5aGwcnnvkCiT%2FKvityy8qkQLQGdhh7pQJOQa0bpRY9zsouaF0QhBYD6p5vxXCSitA%3D%3D&ver=1.0').text
finedust_dict = json.loads(finedust_json)
print(type(finedust_dict)) 
# print(finedust_dict['response']['body']['items']["stationName"])
# print(finedust_dict['response']['body']['items']["dataTime"])
# print(finedust_dict['response']['body']['items']["pm10Value"])
# print(finedust_dict['response']['body']['items']["pm25Value"])
# print(finedust_dict['response']['body']['items']["pm10Grade1h"])
# print(finedust_dict['response']['body']['items']["pm25Grade1h"])
for n in finedust_dict:
    print(n)

# a = float(finedust_dict['response']['body']['items']["dataTime"])
# b = float(finedust_dict['resp onse']['body']['items']["stationName"])
# c = float(finedust_dict['response']['body']['items']["pm10Value"])
# d = float(finedust_dict['response']['body']['items']["pm10Value"])
# e = float(finedust_dict['response']['body']['items']["pm10Grade1h"])
# f = float(finedust_dict['response']['body']['items']["pm25Grade1h"])
# print(f'name: {a}')
# print(f'name: {b}')
# print(f'name: {c}')
# print(f'name: {d}')
# print(f'name: {e}')
# print(f'name: {f}')


# print(finedust_number)



# json_dict = json.loads(get_str)
# print(json_dict)
# print(f'age: {json_dict["age"]}')
# print(f'count: {json_dict["count"]}')
# print(f'name: {json_dict["name"]}')
# print(type(json_dict)) 