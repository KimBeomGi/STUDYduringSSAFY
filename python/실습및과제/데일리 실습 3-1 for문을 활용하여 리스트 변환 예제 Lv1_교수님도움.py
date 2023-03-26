# 목표
# 반복문(for, while)이 동작하는 핵심 원리에 대해 이해한다.조건문(if)이 동작하는 핵심 원리에 대해 이해한다.리스트를 for문을 통해 변환하며, 이에 대한 응용력을 키운다.

# 문제
# 과수원에 농부 한 명이 썩은 과일이 몇 개 들어있는 과일 봉지를 가지고 있다. 과일 봉지를 입력받아, 썩은 과일 조각들을 모두 신선한 것으로 교체하는 코드를 작성하고 리스트 형식으로 출력하시오.
# 	예를 들어, apple,rottenBanana,apple,RoTTenorange,Orange이라는 문자열이 주어진 경우, 대체된 리스트는 ['apple', 'banana', 'apple', 'orange', 'orange'] 이어야 한다.

# 유의 사항
# n 만약 리스트가 비어 있는 경우 빈 리스트를 반환한다.
# n 반환된 리스트의 요소는 모두 소문자여야 한다.
# 요구사항

# [문제풀이]
#1
# 우선 각 apple rottenBanana를 입력해주도록 input()을 이용
# 각 input값을 소문자로 변환시켜준 후 리스트에 포함시킨다.
# for i in range(len(list))를 이용해 각 문자에 rotten이라는 글자가 있는 경우 제거해준다.
# 마지막 이상유무 출력

# fruit_case=[]
# rotten = 'rotten'
# fruit = input()
# fruit.lower()
# fruit_case.append(fruit)

# for i in range(len(fruit_case)+1):     # 과일 수만큼 반복해주기
#     fruit_plus = input()
#     fruit_plus.lower()
#     fruit_case.append(fruit_plus)
#     if rotten in fruit_case:        # 얜 좀 검색해봐야겠다. # 'rotten'을 대체
#         rotten = ''
# print(fruit_case)


#2
# fruit_case = ''
# # fruit_case = []
# fruit = input()
# fruit_l = fruit.lower()
# if 'rotten' in fruit_l:
#     # fruit_case.append(fruit_l.replace('rotten', ''))
#     fruit_case += fruit_l.replace('rotten', '')
# else:
#     # fruit_case.append(fruit_l)
#     fruit_case += fruit_l
# print(fruit_case.split(','))

# 교수님이 풀어주신 방법1
fruits = input().lower().split(',')
new_fruits = []
for fruit in fruits:
    new_fruits.append(fruit.replace('rotten', ''))

print(new_fruits)

# 교수님이 풀어주신 방법2
fruit_case = ''
fruit = input()
fruit_l = fruit.lower()
if 'rotten' in fruit_l:
    fruit_case += fruit_l.replace('rotten', '')
else:
    fruit_case += fruit_l
print(fruit_case.split(','))

#===========================================================

# fruit_case = ''
fruit_case = []
fruit = input()
fruit_l = fruit.lower()
if 'rotten' in fruit_l:
    fruit_case.append(fruit_l.replace('rotten', ''))
    # fruit_case += fruit_l.replace('rotten', '')
else:
    fruit_case.append(fruit_l)
    # fruit_case += fruit_l
print(fruit_case.split(','))