# 골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

# 각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

# 두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

# N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

# e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

# e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

#   1  2  3 도착
# 1 0 18 34
# 2 48 0 55
# 3 18 7 0
# 출발

# 이 경우 최소 소비량은 89가 된다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('230327 5189 전자카트.txt')

# [문제풀이]
# 0. 각 사무실을 돌아다니되 전기 카트의 최소 배터리 사용량을 구해야한다.
# 0-1. 모든 사무실을 들려야 하는데, 각 사무실로 가는데 드는 배터리 사용량이 다르다.
# 해설을 보니 행의 값이 출발지고, 열의 값이 도착지이므로 배터리 사용량 보는 법은 2번방에서 1번 방이면 [2][1]이다.
# 각 방은 연결되어야하므로 내가 2번 방이면 [2][?]의 경로가 내가 갈 수 있는 경로이다.

#####
# 이것도 되고
# def battery_quantity(count, start, sum_value):
#     global min_value
#     if count == N:                                                  # 
#         sum_value += matrix[start][0]
#         if sum_value < min_value:
#             min_value = sum_value
#             return
#     if sum_value > min_value:
#         return
#     for arrival in range(1,N):
#         if matrix[start][arrival] == 0:
#             continue
#         elif not used[arrival]:
#             used[arrival] = 1
#             battery_quantity(count+1, arrival, sum_value+matrix[start][arrival])
#             used[arrival] = 0

# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     used = [0]*N
#     min_value = 2**55
#     A = battery_quantity(1,0,0)
#     print(f'#{testcase} {min_value}')


###################################
# 이것도 되고
def battary(start, visited, battery):                               # 함수 생성
    global min_battery                                              # 글로벌로 min_battery를 생성
    
    if all(visited):                                                # 모든 구역을 방문한 경우
        battery += matrix[start][0]                                 # 사무실로 돌아가는 배터리 사용량 추가
        if battery < min_battery:                                   # battery 값이 min_battery값보다 작다면
            min_battery = battery                                   # 값 바꾸기
        return
    
    for arrival in range(1, N):                                     # 도착지점은 어딜까?
        if not visited[arrival]:                                    # 방문안해봤으면
            visited[arrival] = 1                                    # 방문표시하고
            battary(arrival, visited, battery + matrix[start][arrival])     # 방문하기
            visited[arrival] = 0                                    # 방문 끝. 다시 미방문 표시
            
T = int(input())
for test_case in range(1, T+1):                                     # 테스트케이스 만큼 반복
    N = int(input())                                                # N 입력받기
    matrix = [list(map(int, input().split())) for _ in range(N)]    # 행렬생성
    min_battery = 2**55                                             # 최소 배터리 사용량 초기화
    visited = [0] * N                                               # visited 생성
    visited[0] = 1                                                  # 출발하는 곳은 1로 만들어주기
    battary(0, visited, 0)                                          # 함수에 대입
    print(f"#{test_case} {min_battery}")                            # 출력!



####################
# def permutation(arr, depth, n, r, visited, result):
#     if depth == r:
#         result.append(list(arr))
#         return

#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             arr[depth] = i+1
#             permutation(arr, depth+1, n, r, visited, result)
#             visited[i] = False

# T = int(input())  # 테스트케이스 수 입력

# for t in range(1, T+1):
#     N = int(input())  # 구역 수 입력
#     e = [list(map(int, input().split())) for _ in range(N)]  # 배터리 사용량 입력

#     # 가능한 경로 순열 생성
#     path = []
#     permutation([0]*(N-1), 0, N-1, N-1, [False]*(N-1), path)
    
#     min_battery = float('inf')  # 최소 배터리 사용량 초기화
    
#     for p in path:
#         # 각 경로에서의 배터리 사용량 계산
#         battery = e[0][p[0]] + e[p[-1]][0]
#         for i in range(len(p)-1):
#             battery += e[p[i]][p[i+1]]
#         # 최소 배터리 사용량 갱신
#         min_battery = min(min_battery, battery)

#     # 결과 출력
#     print(f"#{t} {min_battery}")
#######################