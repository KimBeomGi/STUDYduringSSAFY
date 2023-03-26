# json 문자열을 python dictionary로 변환하기

# json_dict = {}
# json_dict['test'] = '안녕하세요'
# print(json_dict)
# print(json_dict['test'])

import json
import requests

# json_str = '{"age":62,"count":298219,"name":"michael"}'
# # json 모듈 활용하기
# json_dict = json.loads(json_str)     # .~~는 메서드
# print(json_dict)
# print(f'age: {json_dict["age"]}')
# print(f'count: {json_dict["count"]}')
# print(f'name: {json_dict["name"]}')
# print(type(json_dict))      # type()는 데이터의 타입을 알려주는 함수임

# 파이썬에서 http 요청한 다음에 json 얻어오기
# 누군가가 http 요청하는 기능을 만들어 뒀다. requests라는 모듈에 포함되어 있음.(파이썬 내장 모듈이 아니므로 별도 설치해야하는 모듈임)
# pip install requests
# pip란? 패키지 인 파이썬
# pip list # pip에 의해 설치된 목록을 보여줌
get_str=requests.get('https://api.agify.io/?name=michael').text
json_dict = json.loads(get_str)
print(json_dict)
print(f'age: {json_dict["age"]}')
print(f'count: {json_dict["count"]}')
print(f'name: {json_dict["name"]}')
print(type(json_dict)) 

# 몇살?
# '나이는 XX살 입니다.'

import json
import requests

get_str=requests.get('https://api.agify.io/?name=michael').text
print(input('몇 살?'))
json_dict = json.loads(get_str)
print(json_dict)
print(f'나이는 {json_dict["age"]} 살 입니다.')
print(type(json_dict)) 


