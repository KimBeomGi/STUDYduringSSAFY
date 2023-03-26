# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
# 다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
 


# 이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
 

# 이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
# 답은 12와 6의 차인 6을 출력한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
# 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('파이썬 sw문제해결 기본-list1 9차시 1일차-구간합.txt', 'r')



T =int(input())
for testcase in range(1,T+1):
    N, M = map(int, input().split())                # N은 정수가 들어있는 배열의 길이, M은 합을 할 갯수
    nums_list =  list(map(int, input().split()))    # 들어갈 숫자들을 받음
    
    # 구간 M길이로 인한 첫 위치와, 끝 위치는 [i] [i+(M-1)]
    # 구간합 구하기.
    interval_sums = []
    for i in range(N-M+1):                          # 0~(N-M)까지 해야하니까
        sum_value = 0                               # sums_value 값을 만들어서 차후 구간합의 최댓값과, 최솟값을 구하기 위함
        for j in range(i, i+M):                     # 구간에서 첫 위치는 i, 끝위치는 i+(M-1)이므로
            sum_value += nums_list[j]               # sum_value에 구간내 수를 더하기
            pass
        interval_sums.append(sum_value)             # 한 구간이 끝나면 interval_sums에 sum_value 추가

    # 구간합의 최솟값, 최댓값 구하기
    min_sum = interval_sums[0]                      # interval_sums[0]값을 우선 구간합의 최솟값으로 변수 할당
    max_sum = 0                                     # max_sum = 0으로 변수 할당
    for interval_sum in interval_sums:              # interval_sums의 요소를 인자로 반복
        if min_sum > interval_sum:                  # min_sum이 요소보다 크면 대체
            min_sum = interval_sum
        if max_sum < interval_sum:                  # max_sum이 요소보다 작으면 대체
            max_sum = interval_sum

    # 출력
    print(f'#{testcase} {max_sum - min_sum}')