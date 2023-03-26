# [문제]
# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# [입력]
# 3
# 3 6
# 5 15
# 5 10

# [출력]
# #1 1
# #2 1
# #3 0

# [문제풀이]
# 0. N개의 원소를 가지면서 그 N개의 원소의 합이 K인 부분집합의 갯수를 구하는 문제이다.
# 0-1. 이 때 집합은 1~12이므로 부분집합에서 제일 작은 숫자도 제일 큰 숫자도 1, 12가 된다.
# 1. 부분 집합을 구해야 문제가 해결되기 때문에 부분집합을 구해보자.
# 2. 반복문을 쓸 수 도 있지만, 반복문을 쓰게되면 1~12 까지 for 문을 써야되기때문에 이는 제한되므로
# 2-1. 비트연산자를 이용하여 부분집합을 구하자.
# 2-2. 이때 구해지는 부분집합의 길이가 주어지는 N과 같을 때, 그 부분집합의 합이 K와 같은지 확인하고
# 2-3. K와 같다면 해당 부분집합이 있으므로 구하려는 값에 +1을 하는 식으로 문제를 해결하자.

T = int(input())
initial_set = [x for x in range(1, 13)]                         # 1~12가 들어있는 원 집합 initial_set
n_initial_set=len(initial_set)                                  # 원 집합의 길이

for testcase in range(1, T+1):                                  # 테스트케이스 출력을 위함
    N, K = map(int, input().split())                            # 입력되는 부분집합의 원소 갯수, 부분집합의 합
    count_equal_k = 0                                           # K와 갑이 같은 부분집합의 갯수를 더함
    for i in range(1 << n_initial_set):                         # 원집합의 부분집합의 갯수
        subset = []                                             # 부분집합이 들어갈 리스트
        for j in range(n_initial_set):                          # 원집합의 길이를 통해 비트연산자를 이용한 부분집합을 구할 것임.
            if i & (1 << j):                                    # j번째 비트가 i 와 비교해서 1&1 이어서 True 이면
                subset.append(initial_set[j])                   # 원집합의 j번째 인덱스를 부분집합에 추가해라.
        if len(subset) == N:                                    # 부분집합의 길이가 입력되는 부분집합의 길이라면
            sum_subset = 0                                      # subset의 합이 입력되는 K와 같은지 확인하기 위함
            for i in subset:                                    # 부분집합(subset)의 인자를 반복문을 돌려서 총합을 구하기 위함
                sum_subset += i                                 # 각 부분집합의 원소를 더한다.
            if sum_subset == K:                                 # 각 부분집합의 합이 K와 같다면
                count_equal_k += 1                              # count_equal_k에 1을 더한다
    if count_equal_k != 0:                                      # K와 값도 같고 N과 길이도 같은 부분집합의 갯수가 0이 아니면 출력
        print(f'#{testcase} {count_equal_k}')
    elif count_equal_k == 0:                                    # K와 값도 같고 N과 길이도 같은 부분집합의 갯수가 0이면 0 출력
        print(f'#{testcase} {0}')


'''
T = int(input())
for testcase in range(1, T+1):                                  # 테스트케이스 출력을 위함
    initial_set = []                                            # 1~12가 들어있는 원 집합
    for i in range(1,13):
        initial_set.append(i)
    N, K = map(int, input().split())                            # 입력되는 부분집합의 원소 갯수, 부분집합의 합
    n_initial_set=len(initial_set)                              # 원 집합의 길이
    count_equal_k = 0                                           # K와 갑이 같은 부분집합의 갯수를 더함
    for i in range(1 << n_initial_set):                         # 원집합의 부분집합의 갯수
        subset = []                                             # 부분집합이 들어갈 리스트
        for j in range(n_initial_set):                          # 원집합의 길이를 통해 비트연산자를 이용한 부분집합을 구할 것임.
            if i & (1 << j):                                    # j번째 비트가 i 와 비교해서 1&1 이어서 True 이면
                subset.append(initial_set[j])                   # 원집합의 j번째 인덱스를 부분집합에 추가해라.
        if len(subset) == N:                                    # 부분집합의 길이가 입력되는 부분집합의 길이라면
            sum_subset = 0                                      # subset의 합이 입력되는 K와 같은지 확인하기 위함
            for i in subset:                                    # 부분집합(subset)의 인자를 반복문을 돌려서 총합을 구하기 위함
                sum_subset += i                                 # 각 부분집합의 원소를 더한다.
            if sum_subset == K:                                 # 각 부분집합의 합이 K와 같다면
                count_equal_k += 1                              # count_equal_k에 1을 더한다
    if count_equal_k != 0:                                      # K와 값도 같고 N과 길이도 같은 부분집합의 갯수가 0이 아니면 출력
        print(f'#{testcase} {count_equal_k}')
    elif count_equal_k == 0:                                    # K와 값도 같고 N과 길이도 같은 부분집합의 갯수가 0이면 0 출력
        print(f'#{testcase} {0}')
'''