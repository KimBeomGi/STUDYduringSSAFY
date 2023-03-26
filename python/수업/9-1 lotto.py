# 1이상 45이하 자연수 중에서 임의의 중복되지 않는 숫자 6개를 뽑는 것.

# 5,9,11,17,24,36

# print(list(range(1,46)))

import random

selected_numbers=random.sample(range(1,46),6)
# # [5,7,3,4,1] >>> [1,3,4,5,7]
# selected_numbers.sort() # 이러면 오름차순으로 정렬 가능함 # 리스트 자체가 정렬이 됩니다. #.sort는 리스트에 포함되어있는 함수
# print(selected_numbers)

# print(sorted(selected_numbers)) #sorted(~~)는 파이썬 내장함수, 인자로 주어진 리스트를 이용해서 정렬된 리스트 반환

# #리스트는 .sort라는 함수를 포함함.

a = sorted(selected_numbers)    #얘를 정렬하는 거임 sorted()와 .sort는 다르다.
print(selected_numbers)
print(a)