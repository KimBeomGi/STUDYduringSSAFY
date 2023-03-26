import random
# 점심 메뉴 추천 프로그램 작성
# 메뉴는 한식, 중식, 양식, 일식 중 하나를  추천해줌 
# 위 목록 중 아무거나 하나 추천
# 모든 메뉴를 리스트에 넣어주기
# 변수이름 = []
menu = ['떡볶이','치킨','양념치킨','고기']    #비어있는 리스트를 menu라는 변수에 할당

# print(menu[2])
# menu에서 아무거나 하나 뽑기

# 파이썬에서 리스트 안에 있는 것 중에 아무거나 하나 뽑는 기능: random이라는 모듈
# 다른 사람이 만들어 놓은 모듈을 쓰려면 가져와서 써야하는데,(import)가 그 역할을 한다.
# lunch=random.sample(menu,2)   #외울 것.메뉴 리스트에서 임의의 값, n개를 선정한 값을 lunch 변수에 대입
# lunch=random.choice(menu)
# print(lunch)

print(menu[-1]) #파이썬에서만 되는 것인데 리스트에서 -1은 리스트의 맨 오른쪽 값을 의미. -2는 맨 오른쪽에서 2번째.

#리스트의 전체 길이: len이라는 함수를 이용. 사용 시 len() 의 형태.
# print(len(menu))
length = len(menu) # 왼쪽은 변수, 오른쪽은 값.
print(length)

print(menu[length-1])
print(menu[len(menu)-1])