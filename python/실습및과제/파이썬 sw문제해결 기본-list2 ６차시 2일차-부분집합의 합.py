# 얘 나중에 다시 풀어야함




# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


import sys
sys.stdin = open('파이썬 sw문제해결 기본-list2 ６차시 2일차-부분집합의 합.txt', 'r')

T = int(input())
for testcase in range(1, T+1):
    initial_set = []
    for i in range(1,13):                       # 1~12를 initial_set
        initial_set.append(i)
    N, K = map(int, input().split())            # 부분집합의 원소갯수 N, 부분집합의 합 K
    n_initial_set = len(initial_set)            # 원집합의 길이
    count_equal_K = 0                           # K와 값이 같은 부분집합의 갯수를 세아리는 변수
    for i in range(1 << n_initial_set):         # 원집합의 부분집합의 갯수, 즉 0 ~ (1*(2^n_initial_set)-1) 이 range임
        subset = []
        for j in range(n_initial_set):          # j인자를 0~ (n_initial_set-1) 만큼
            if i & (1<< j):                     # True 면 그러니까 0이상이면
                subset.append(initial_set[j])
            if len(subset) == N:
                sum_subset = 0
                for i in subset:
                    sum_subset = 0
                    for i in subset:
                        sum_subset += i
                    if sum_subset == K:
                        count_equal_K += 1
    if count_equal_K != 0:
        print(f'#{testcase} {count_equal_K}')
    elif count_equal_K == 0:
        print(f'#{testcase} {0}')
