# ? 어떻게 문제 해?
# 쟤네들 끼리 어떻게 비교함?
# 딕셔너리 쓰면 비교되니까 비교해서 교환하는 형식으로 
# count 써서 한 사람들 잡아 낼거임

# [문제]
# 숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
# 예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

# [입력]
# 입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
# 그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.
# 그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다

import sys
sys.stdin = open('GNS_test_input.txt', "r")

#[문제풀이]
# 0."ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" 의 외계어로 0~9까지 적힌 수가 있다.
# 0-1. 이 단어(수) 들을 0~9에 대입하는 수로 생각해서 문자를 정렬해보자.
# 1. zro 등의 단어(수) 들을 딕셔너리에 값을 +1로 받아내고,
# 1-1. 딕셔너리에서 해당 단어를 해당 단어의 value인 수량만큼 출력하고 이어서 다음 수를 출력하는 방식으로 해보자.

T = int(input())
for testcase in range(1,T+1):
    tc, N = map(str, input().split())
    N = int(N)
    ailen_nums_list = list(map(str, input().split()))                # 외계문자 입력받음
    ailen_nums_dict = {}                                            # 외계문자를 딕셔너리에 입력받을 것임.
    for ailen_num in ailen_nums_list:                               # ailen_nums_dict에 각 문자에 따른 수량을 입력하기 위함
        try: ailen_nums_dict[ailen_num] += 1
        except: ailen_nums_dict[ailen_num] = 1
    print(f'#{testcase}')
    ailen_how_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for ailen_num in ailen_how_num:                                 # 'ZRO'~''NIN'의 숫자만큼 출력하기 위함
        if ailen_nums_dict[ailen_num] == 0:
            continue
        else: 
            for i in range(ailen_nums_dict[ailen_num]):
                print(ailen_num, end=' ')
    print()