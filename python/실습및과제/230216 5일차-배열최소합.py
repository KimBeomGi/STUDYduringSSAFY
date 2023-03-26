
# NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
# 조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
# 예를 들어 다음과 같이 배열이 주어진다.
# 이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

# 2  a1  2
# a5  8  5
# 7  2  a2


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.


# [문제풀이]
# 0. N by N 개의 행렬이 있고, N개의 숫자를 골라서 합이 최소가 되도록 한다.
# 0-1. 이때 한 행마다 1개의 숫자를 받을 수 있게 되는데,
# 0-2. 또한 한 열에서도 1개의 숫자만을 받을 수 있게 된다.
# 0-3. 따라서 이번에 배웠던 순열과 같은 것이라 보면 되겠다.
# 1. 완전 탐색을 실시하면서, [i][j]로 되어있을 때, i는 반복하며 돌아갈것이니 문제 없고, j는 이전의 것과 곂치지 않도록 만들어 보자.



# # DFS 및 순열 생성
# def min_sum_m(matrix):
    
#     for _ in range(N**N):
#         temp_j_list = []                                                # (i,j) 형식으로 들어감, 함수에서 열이 겹치는지를 확인하기 위해 사용할 임시 리스트
#         min_sum = 10*N*N                                                # 합의 최솟값으로 사용하기 위한 min_sum. 우선, 10보다 작은 자연수이므로 제일 최댓값인 녀석을 넣었다.
#         temp_cal_list = []                                              # 함수에서 계산에 사용할 임시 리스트
#         for i in range(N):                                              # 행에 사용될 i 인자
#             # if i == N-1: 
#             #     for j in range(N):                                    # j를 N만큼 반복(열을 순회)
#             #         if j in temp_cal_list:                            # 만약 j인자가 리스트에 있다면
#             #             continue                                      # 다음 j로 넘어감
#             #         else:                                             # j인자가 리스트에 없으면?
#             #             temp_j_list.append(j)                         # j인자를 temp_j_list
#             #             temp_cal_list.append(matrix[i][j])            # j값을 temp_cal_list에 추가
#             #             # return matrix[i][j]
#             # else:
#             for j in range(N):                                          # j를 N만큼 반복(열을 순회)
#                 if (i,j) in temp_j_list:                              # 만약 j인자가 리스트에 있다면
#                     continue                                            # 다음 j로 넘어감
#                 else:                                                   # j인자가 리스트에 없으면?
#                     temp_j_list.append((i,j))                           # j인자를 temp_j_list
#                     temp_cal_list.append(matrix[i][j])                  # j값을 temp_cal_list에 추가
#                     break

#         temp_sum = 0                                                    # 구한 숫자들의 합을 구하기위한 temp_sum변수
#         for temp_num in temp_cal_list:                                  # 합하기 위해 쓰이는 반복문
#             temp_sum += temp_num
#         if min_sum > temp_sum:                                          # 현재 합의 최솟값이, 구한 합보다 크다면
#             min_sum = temp_sum                                          # 합의 최솟값을 구합 합으로 변경
#     return min_sum


# # 값 입력받음
# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())                                                    # N by N이므로 행렬의 길이 N을 입력받음
#     matrix = [list(map(int, input().split())) for _ in range(N)]        # N만큼 행을 입력받으므로 그에 따라 NbyN 행렬 생성
#     print(f'#{testcase} {min_sum_m(matrix)}')






# def dfs(idx,sum_v):
#     if idx == N:
#         print(sum_v)
#         return
#     for i in range(N):
#         dfs(idx+1, sum_v + arr[idx][i])

# arr = [[2,1,2,1],[5,8,5,1],[7,2,2,1],[1,1,1,1]]
# N = 4
# dfs(0,0)

'''
# DFS 및 순열 생성
def min_sum_m(matrix):
    min_sum = 10*N*N                                                # 합의 최솟값으로 사용하기 위한 min_sum. 우선, 10보다 작은 자연수이므로 제일 최댓값인 녀석을 넣었다.
    temp_cal_list = []                                              # 함수에서 계산에 사용할 임시 리스트
    temp_j_list = []                                                # (i,j) 형식으로 들어감, 함수에서 열이 겹치는지를 확인하기 위해 사용할 임시 리스트
    visited = [[0]*N for _ in range(N)]                             # 방문기록 생성 visited 생성
    i = 0                                                           # while반복문에 쓸 행 i인자
    while 0 <= i < N:                                               # 행 반복
        j = 0                                                       # while반복문에 쓸 행 j인자
        while 0 <= j < N:                                           # 열 반복
            if j == N-1:                                            # 맨 마지막 열이면


            elif visited[i][j] == 1:                                # 만약 j인자가 리스트에 있다면
                visited[i][j] = 0                                   # 다음번에도 이용해야되니까 visited[i][j] = 0으로 만듬
                j += 1                                              # j에 +1을 함으로써
                continue                                            # 다음 j로 넘어감
            else:                                                   # j인자가 리스트에 없으면?
                temp_j_list.append((i,j))                           # j인자를 temp_j_list
                temp_cal_list.append(matrix[i][j])                  # j값을 temp_cal_list에 추가
                visited[i][j] = 1                                   # 방문기록 남기기
                break
        j += 1
        i += 1

    temp_sum = 0                                                    # 구한 숫자들의 합을 구하기위한 temp_sum변수
    for temp_num in temp_cal_list:                                  # 합하기 위해 쓰이는 반복문
        temp_sum += temp_num
    if min_sum > temp_sum:                                          # 현재 합의 최솟값이, 구한 합보다 크다면
        min_sum = temp_sum                                          # 합의 최솟값을 구합 합으로 변경
    return min_sum


# 값 입력받음
T = int(input())
for testcase in range(1, T+1):
    N = int(input())                                                    # N by N이므로 행렬의 길이 N을 입력받음
    matrix = [list(map(int, input().split())) for _ in range(N)]        # N만큼 행을 입력받으므로 그에 따라 NbyN 행렬 생성
    print(f'#{testcase} {min_sum_m(matrix)}')
'''

import sys
sys.stdin = open('230216 5일차-배열최소합.txt', 'r')

def perm_summ(idx, perm_sum):                                            # 순열의 합을 구해내는 perm_sum 함수 생성, 행을 의미하는 idx와 순열의 합을 의미하는 perm_sum을 매개변수로 받음
    if idx == N:                                                        # 행을 의미하는 idx가 N이라면
        perm_sum_list.append(perm_sum)                                  # perm_sum_list에 perm_sum을 추가
        return                                                          # 마지막 행이므로 돌아감
    for i in range(N):                                                  # 열을 돌기 위해서 i를 인자로 N번돌림
        if not used[idx][i]:                                            # used의 요소로 들어있지 않으면
            permutation[idx] = matrix[idx][i]                           # 생성하는 순열의 요소로 집어넣는다.
            used[idx][i] = 1                                            # 사용한 거니까 1로 표현해주고
            perm_summ(idx+1, perm_sum + matrix[idx][i])                 # 재귀함수를 이용해서 행을 1개 더해주고, 값을 sum해준다.
            used[idx][i] = 0                                            # 사용했음은 다시 1로 지워준다.

T = int(input())
for testcase in range(1, T+1):
    N = int(input())                                                    # N by N이므로 행렬의 길이 N을 입력받음
    matrix = [list(map(int, input().split())) for _ in range(N)]        # N만큼 행을 입력받으므로 그에 따라 NbyN 행렬 생성
    permutation = [0]*N                                                 # N개의 숫자를 순열(permutation)로 만들어 합을 구할 것이기 때문
    used = [[0]*N for _ in range(N)]                                    # N by N개의 사용했음을 표시하는 행렬 만들기
    perm_sum_list = []
    perm_summ(0, 0)
    min_sum = 10*N*N
    for perm_sum_i in perm_sum_list:
        if min_sum > perm_sum_i:
            min_sum = perm_sum_i
    print(f'#{testcase} {min_sum}')

     



# # N = 3
# arr = [1,2,3]
# perm_arr = [0]*N
# used = [0]*N
# # idx 번째에 넣을 수 있는 수자 다 넣기
# def perm(idx):
#     if idx==N:
#         print(perm_arr)
#         return
#     for i in range(N):
#         if not used[i]:                 # used[i]가 0일때
#             perm_arr[idx] = arr[i]
#             used[i] = 1
#             perm(idx+1)
#             used[i] = 0                 # i번째 사용하고나서 사용완료했으니 이제 다른 값 찾아야해서 반납(?)
# perm(0)

# def dfs(idx,sum_v):
#     if idx == N:
#         print(sum_v)
#         return
#     for i in range(N):
#         dfs(idx+1, sum_v + arr[idx][i])

# arr = [[2,1,2,1],[5,8,5,1],[7,2,2,1]]
# N = 3
# dfs(0,0)