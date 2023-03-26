# [문제]
# 1 정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 출력하라.
# 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야한다.


# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

# [문제풀이]
# 1. list를 전달 받는다고 하지만 입력받을 때는 str 이므로 int와 리스트의 형태로 바꿔주도록 한다.
# 2. 연속적으로 나타나는 숫자는 하나만 남기고 제거해야하므로 for문으로 list를 돌려서 하나씩 제거해주며 리스트를 만들어보자.
# ※처음에는 문제를 잘 못 읽어 set으로 중복값을 제거하려 했었음. 문제 잘 읽을 것.
# 첫 시도에서 remove 하려 했는데 제거될 수록  리스트가 줄어들어서 반복문에서 꼬였음.
# 새 비어있는 리스트를 만들고 그곳에 추가하는 방식으로 제작

asker = input()[1:-1]                               # 처음 입력을 리스트처럼 생긴 문자열을 받기 때문에 []을 제거
asker_list = list(map(int, asker.split(',')))           # []을 제거한 문자열을 다시 int화, 리스트화 진행
# print(sosker)
ask = []                                            # 리스트로 출력하기 위해 ask 라는 빈 리스트를 새로 생성, 해당 방식은 elif를 먼저 읽어야 이해가 가능
for souce in range(len(asker_list)):                    # for 반복문을 통해 최초 asker리스트에서 중복 요소를 확인실시
    if souce == (len(asker_list)-1):                    # asker 리스트의 맨 마지막의 경우 진행하려는 중복검사에 있어 제한되기에 elif 보다 먼저 작성
        # if asker_list[-1] == asker_list[souce]:         
        #     ask.append(asker_list[souce])               
        ask.append(asker_list[souce])               # 중복 맨 마지막을 출력하는 것인데 맨 마지막값은 다음 값과 비교가 불가능하므로 바로 출력
        # else:
        #     break                                            # 필요한 것들이 다 출력 되었으니 break
    elif asker_list[souce] != asker_list[souce+1]:          # asker리스트 의 인덱스가 다음 인덱스와 같지 않다면, asker_list[souce]를 빈 ask리스트에 추가.
        ask.append(asker_list[souce])                       # 중복되는 값이 지속적으로 있다면 맨 뒤에것을 출력하겠다는 의미
        print(ask)
print(ask)