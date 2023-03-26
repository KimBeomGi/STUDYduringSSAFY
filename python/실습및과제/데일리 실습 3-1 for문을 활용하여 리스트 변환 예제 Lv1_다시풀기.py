# 목표
# 반복문(for, while)이 동작하는 핵심 원리에 대해 이해한다.조건문(if)이 동작하는 핵심 원리에 대해 이해한다.리스트를 for문을 통해 변환하며, 이에 대한 응용력을 키운다.

# 문제
# 과수원에 농부 한 명이 썩은 과일이 몇 개 들어있는 과일 봉지를 가지고 있다. 과일 봉지를 입력받아, 썩은 과일 조각들을 모두 신선한 것으로 교체하는 코드를 작성하고 리스트 형식으로 출력하시오.
# 	예를 들어, apple,rottenBanana,apple,RoTTenorange,Orange이라는 문자열이 주어진 경우, 대체된 리스트는 ['apple', 'banana', 'apple', 'orange', 'orange'] 이어야 한다.

fruits = input().lower().split(',')    #입력하는순가 소문자로 전환되고, 쉼표 기준으로 갈라서 리스트로 만들어줌
new_fruits=[]   # rotten이 없어진 fruit을 받을 리스트 작성
for fruit in fruits:    # fruits 리스트에 각 인덱스를 요소로한다.
    new_fruits.append(fruit.replace('rotten',''))   # fruits의 인덱스이자 인자인 fruit에서 rotten을 제거 후 new_fruits 리스트에 입력
print(new_fruits)