# 목표
# 학습주제파이썬 개발 환경에 대한 이해파이썬 예외처리 기본 방식에 대한 이해
# 학습목표모듈 동작 방식에 대해 이해한다.파이썬 자료 구조의 구조 및 동작 방식에 대해 이해한다.예외처리 방식 및 활용 방식에 대해 이해한다.

# 문제
# n개의 소금물을 섞었을 때, 혼합된 소금물의 농도와 양을 계산하는 프로그램 mass_percent.py를 만드시오. 조건    
# - 소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오.        
# 최대 5개의 소금물을 입력할 수 있다. 
# 출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오.

# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

# ======================================================================================================

# [문제풀이]

all_saltwater = []  # 모든 (퍼센트 농도, 소금물의 양)을 리스트화
salt_quantity = 0
salt_water_quantity = 0
for i in range(1,6):
    input_str = input('소금물의 퍼센트 농도(%)와 소금물의 양(g)을 숫자로만 입력하세요:')    # 최초 소금물 퍼센트 농도와 소금물의 양을 입력하도록 함
    if str(input_str) != 'Done':   # 'Done' 입력시 출력이 되야하는데 Done이 아니라면 계속 입력하도록 만들기
        salt_water = list(map(str, input_str.split()))
        salt_water[0] = salt_water[0][0:-1] #단위 삭제
        salt_water[1] = salt_water[1][0:-1]
        salt_water[0] = float(salt_water[0])  #str을 int로 교체
        salt_water[1] = float(salt_water[1])
        # print(salt_water) # 단위 삭제여부와 str에서 int로 바뀌었는지 확인
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
print(f'{round_salt_percent}% {round_salt_water_quantity}g')    # f스트링을 이용해 단위 붙여주기