# 목표
# 반복문(for, while)이 동작하는 핵심 원리에 대해 이해한다.
# 조건문(if)이 동작하는 핵심 원리에 대해 이해한다.
# 리스트 내부 딕셔너리가 있는 형태의 문제를 다루며, 각 자료형의 특징을 면밀히 살펴본다.

# 문제
# 1. 여러 사람의 혈액형(A,B,AB,O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 만드시오

# [문제풀이]
# 각 리스트에 있는 각 혈액형의 수를 세아려준다.
# 각 혈액형의 수를 value, 혈액형을 값을 만들어주는 dictionary를 넣어준다.


blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
blood_a = 0
blood_b = 0
blood_o = 0
blood_ab = 0

for blood in blood_types:   # blood_types가 리스트이기에 따로 range를 안하고 blood_types를 이용
    if blood == 'A':
        blood_a += 1
    elif blood == 'B':
        blood_b += 1
    elif blood == 'O':
        blood_o += 1
    elif blood == 'AB':
        blood_ab += 1

blood_dic = {}  # 혈액형 딕셔너리 생성
blood_dic['A'] = blood_a
blood_dic['B'] = blood_b
blood_dic['O'] = blood_o
blood_dic['AB'] = blood_ab
print(blood_dic)

