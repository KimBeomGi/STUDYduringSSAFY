# [문제]
# 작물과 가격이 함께 있는 리스트가 존재할 때, 가장 높은 가격을 가지고 있는 작물의 이름을 출력하라.
# 단, 작물의 이름을 직접 입력하여 출력하지 않는다.

# grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]


# [문제풀이]
# 1.리스트 안의 튜플의 형식이다. 딕셔너릴 전환하는 방법도 있을 것이지만 인덱스를 활용하는 방법을 이용해보자.
# 2. for 문으로 grain_lst[~][1]을 돌려 리스트에 넣고 그 리스트 중 가장 높은 값의 grain_lst[~][0]을 출력하는 방식을 사용해보자.
# 3. 이 방법이 성공하면 다른 방법도 찾아서 해보자.
'''
for문 이용 풀기
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
expensive_grain =[]                                                 # 작물 가격만 넣어둘 리스트
for grain_chip in grain_lst:                                        # grain_chip인자를 grain_lst에서 추출해서 반복
    expensive_grain.append(grain_chip[1])                           # 추출한 가격을 expensive_grain에 입력

realexpensive_grain = sorted(expensive_grain, reverse= True)        # 추출된 가격들을 내림차순으로 정렬
for grain in grain_lst:                                             # grain 인자를 grain_lst에서 추출해서 반복
    if grain[1] == realexpensive_grain[0]:                          # 작물의 가격이 제일비싼 작물의 가격과 같다면
        print(grain[0])                                             # 해당 작물의 가격을 출력
'''
'''
# 함수로 만들어 풀어보기.
def most_expensive_grain(grain_lst):
    expensive_grain =[]                                                 # 작물 가격만 넣어둘 리스트
    for grain_chip in grain_lst:                                        # grain_chip인자를 grain_lst에서 추출해서 반복
        expensive_grain.append(grain_chip[1])                           # 추출한 가격을 expensive_grain에 입력

    realexpensive_grain = sorted(expensive_grain, reverse= True)        # 추출된 가격들을 내림차순으로 정렬
    for grain in grain_lst:                                             # grain 인자를 grain_lst에서 추출해서 반복
        if grain[1] == realexpensive_grain[0]:                          # 작물의 가격이 제일비싼 작물의 가격과 같다면
            return(grain[0])    

grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
print(most_expensive_grain(grain_lst))
'''
'''
# 딕셔너리로 풀어보기
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
grain_dict = dict(grain_lst)                                                    # 주어진 리스트가 딕셔너리로 바로 바꿀수 있는 리스트안 튜플 형태이므로 딕셔너리로 변환
expensive_grain = sorted(list(grain_dict.values()))                             # 주어진 리스트의 value만 추출해서 리스트로 만든뒤 오름차순 정렬
most_expensive_grain = expensive_grain[-1]                                      # 바로 위 리스트에서 제일 비싼 작물의 가격을 선정
reverse_grain_dict= dict(map(reversed, grain_dict.items()))                     # 기존 딕셔너리에서 가격은 value이므로, 딕셔너리의 키와 값을 서로 바꾸어주고, 가격을 집어 넣었을 시 작물명이 나오도록 함
# print(reverse_grain_dict)
print(reverse_grain_dict[most_expensive_grain])
'''
'''
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
grain_lst.sort(key= lambda x : -x[1])                                           # lambda 함수 이용, 리스트 내 튜플이므로 튜플의[1]번째를 키로 잡고, 양수를 음수로 변환시켜주고 sort먹여서 오름차순.
# 음수의 오름차순이므로 [0]값이 양수로 바꾸었을때는 제일 큰 수이므로 ('옥수수',4500)이 나오게 된다.
print(grain_lst[0][0])                                                          # 따라서 grain_lst의 첫번째 튜플의 첫번째 값을 출력
'''