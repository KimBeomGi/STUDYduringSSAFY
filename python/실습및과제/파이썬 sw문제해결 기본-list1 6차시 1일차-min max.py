# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

# [입력]
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('파이썬 sw문제해결 기본-list1 6차시 1일차-min max.txt', 'r')
'''
# 버블 정렬 방법 이용
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    problem = list(map(int, input().split()))

    # 정렬하기
    for i in range(N-1):
        for j in range(N-1):
            if problem[j] > problem[j+1]:
                problem[j], problem[j+1] = problem[j+1] , problem[j]
    
    # 최솟값, 최댓값 구하기
    min_solve = problem[0]
    max_solve = problem[N-1]

    print(f'#{testcase} {max_solve-min_solve}')
'''
# 선택 정렬 방법 이용
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    problem = list(map(int, input().split()))
    # 오름차순을 위해 진행하는 반복문
    for i in range(N-1):        # 0~ N-2까지 하는 이유는 [N-1] 인덱스는 진행할 필요가 없기 때문
        min_idx = i
        # 선택을 하기 위한 반복문
        for j in range(i,N):
            if problem[min_idx] > problem[j]:
                min_idx = j
        problem[min_idx], problem[i] = problem[i], problem[min_idx]
    
    # 최솟값, 최댓값 구하기
    min_solve = problem[0]
    max_solve = problem[N-1]
    print(f'#{testcase} {max_solve-min_solve}')