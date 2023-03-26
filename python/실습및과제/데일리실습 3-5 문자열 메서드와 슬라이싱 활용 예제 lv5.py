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

all_saltwater = []
salt_quantity = 0          # 총 소금의 양을 구하기 위함
saltwater_quantity = 0     # 총 소금물의 양을 구하기 위함

for i in range(1,6):
    plus_water_input = input('소금물의 퍼센트 농도(%)와 소금물의 양(g)을 숫자로만 입력하세요:')   # 소금물의 퍼센트 농도와 소금물의 양 입력
    if plus_water_input != 'Done':    #Done이 입력되면 내용을 출력해야하므로 Done이 아니면 소금물의 내용을 투입해야하니까!
        plus_water = list(map(float, plus_water_input.split()))
        plus_water.append(plus_water[0]*plus_water[1]/100)  # 소금의 양을 구해서 만들어진 plus_water리스트에 입력
        all_saltwater.append(plus_water)    # [소금농도, 소금물의 양, 소금의 양]리스트를 모두 all_saltwater 리스트한 곳에 넣어주기
    else:
        break

for salts in range(len(all_saltwater)):     # all_saltwater의 내용들을 각각 계산해서 출력하기 위함
    salt_quantity = salt_quantity + all_saltwater[salts][2]                 # 각 리스트별 소금의 양을 추출해서 더해주기
    saltwater_quantity = saltwater_quantity + all_saltwater[salts][1]       # 각 리스트별 소금물의 양을 추출해서 더해주기
salt_percent = salt_quantity/saltwater_quantity*100     # 혼합된 소금물의 퍼센트를 구하기 위함
pro_salt_percent = round(salt_percent)                  # 소수 2번째자리까지 반올림한 소금물 농도
pro_saltwater_quantity = round(saltwater_quantity)      # 소수 2번째자리까지 반올림한 소금물의 양
print(pro_salt_percent, pro_saltwater_quantity)