# [문제풀이]
# 0. 입력값을 16진수로 입력받아 2진수로 변환해준 후
# 0-1. 연속한 1의 최대 개수를 출력하는 프로그램을 작성해야한다.

# 테스트 케이스 입력받기
T = int(input())
for testcase in range(1, T + 1):
    N = int(input())            # 16진수의 길이 입력받기
    hexa_int= input()               # 16진수 입력받기
    dec_int = int(hexa_int, 16)         # 10진수로 먼저 바꿔주기
    # print(dec_int)
    bin_int_tmp = bin(dec_int)      # 2진수지만 출력에 0b가 있으므로 임시 2진수
    # print(bin_int)
    bin_int = bin_int_tmp[2:]       # 실제로 2진수로 만들기
    M = len(bin_int)                # bin_int의 길이
    # print(bin_int)
    # bin_int= int(bin_int)         # str로 존재하는 bin_int를 int로 바꿔줌
    # 최대로 연속한 1의 갯수 파악
    max_count = 0                   # 출력을 위한 max_count 변수
    count = 0                       # max_count를 찾기 위한 count변수
    # print(bin_int)

    for i in range(M):
        # 0이면 현재 값확인 하고 max_count에 기입 또는 넘어가기
        if bin_int[i] == '0':
            if max_count < count:
                max_count = count
            count = 0
        # 1이면 count +1, 연속되면 계속 +1하겠지?!
        elif bin_int[i] == '1':
            count += 1
        # if 문으로 max_count 보다 count가 크면 일단 기입
        if i == M-1:
            if max_count < count:
                max_count = count
    print(f'#{testcase} {max_count}')