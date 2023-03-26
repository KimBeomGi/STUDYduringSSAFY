# 목표
# 반복문(for, while)이 동작하는 핵심 원리에 대해 이해한다.
# 조건문(if)이 동작하는 핵심 원리에 대해 이해한다.
# 리스트 내부 딕셔너리가 있는 형태의 문제를 다루며, 각 자료형의 특징을 면밀히 살펴본다.

# 문제
#  1. Dictionary로 이루어진 list를 전달받아 모든 dictionary의 'age'key에 해당하는 value들의 합을 구하시오.

# [문제풀이]
# 리스트로 이루어져있으므로 리스트 내의 인덱스를 이용한 후
# 리스트에서 꺼내온 딕셔너리에서 age의 value를 출력한다.
# 해당 value를 새 리스트에 집어넣고 sum()을 이용해 합한다.

infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
sum_age = []
for info in range(len(infos)):
    sum_age.append(infos[info]['age'])
print(sum(sum_age))