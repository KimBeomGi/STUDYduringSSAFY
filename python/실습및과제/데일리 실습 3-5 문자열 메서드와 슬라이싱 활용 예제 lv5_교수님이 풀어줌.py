# 목표
# 반복문(for, while)이 동작하는 핵심 원리에 대해 이해한다.
# 조건문(if)이 동작하는 핵심 원리에 대해 이해한다.
# 리스트 내부 딕셔너리가 있는 형태의 문제를 다루며, 각 자료형의 특징을 면밀히 살펴본다.

# 문제
# 1. 여러개의 소금물을 섞었을 때, 혼합된 소금물의 퍼센트 농도와 양을 계산하는 프로그램을 만드시오.
# 조건
#     1. 소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오.
#     2. 최대 5개의 소금물을 입력할 수 있다.
#     3. 출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오.

# [문제풀이]
# 소금물의 퍼센트 농도 = (소금의 양)/ (소금물의 양)*100 이다.
# 소금의 양 = (소금물의 퍼센트 농도)*(소금물의 양)/100 이므로 각 소금의 양을 구해주고, 각 소금의 양과 각 소금물의 양을 각각 더해줘야한다.
# 이렇게해서 ((총 소금의 양)/ (총 소금물의 양)*100, 소금물의 양) 이 출력되도록해야 한다.
# 최대 5개의 소금물을 입력할 수 있으므로 반복문으로 입력을 5번만 돌리도록 제한
# 조건3.에 따라 round(~,2)를 이용

all_saltwater = []  # 모든 (퍼센트 농도, 소금물의 양)을 리스트화
salt_quantity = 0
salt_water_quantity = 0

for i in range(1,6):
    input_str = input('소금물의 퍼센트 농도(%)와 소금물의 양(g)을 숫자로만 입력하세요:')    # 최초 소금물 퍼센트 농도와 소금물의 양을 입력하도록 함
    if str(input_str) != 'Done':   # 'Done' 입력시 출력이 되야하는데 Done이 아니라면 계속 입력하도록 만들기
        salt_water = list(map(float, input_str.split()))
        salt_water.append(salt_water[0]*salt_water[1]/100) # 소금의 양을 salt_water리스트 안에 추가해주었음.
        all_saltwater.append(salt_water)    #입력된 퍼센트 농도, 소금물의 양을 리스트 안의 리스트로서 입력
    else:   # 위에서 str(input_str) != 'Done': 으로 썼기에 여기선 Done일 때 어떻게 할거야! 임 그래서 마칠거다 라고 함
        break
for salt in range(len(all_saltwater)):
        salt_quantity = salt_quantity + all_saltwater[salt][2]  # 소금의 양 총합
        salt_water_quantity = salt_water_quantity + all_saltwater[salt][1]  # 소금물의 양 총합
        salt_percent = salt_quantity / salt_water_quantity * 100    #소금물의 농도
round_salt_percent = round(salt_percent)
round_salt_water_quantity = round(salt_water_quantity)
print(round_salt_percent, round_salt_water_quantity)
   
    

# for salt in range(len(all_saltwater)):
#     salt_quantity = salt_quantity + all_saltwater[salt][2]  # 소금의 양 총합
#     salt_water_quantity = salt_water_quantity + all_saltwater[salt][1]  # 소금물의 양 총합
#     salt_percent = salt_quantity / salt_water_quantity * 100    #소금물의 농도
# round_salt_percent = round(salt_percent)    # 소금물의 농도 결과 반올림
# round_salt_water_quantity = round(salt_water_quantity)  #소금물의 양 결과 반올림
# print(round_salt_percent, round_salt_water_quantity)