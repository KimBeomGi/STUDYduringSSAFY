import sys
sys.stdin = open('2230404 5250 최소 비용.txt')


# [문제풀이]
# 0. 출발은 맨 왼쪽 위, 도착은 맨 오른쪽 아래로 고정이다.
# 0-1. 상하 좌우로만 이동이 가능하며, 한칸 이동시마다 기본 1의 이동 비용이 들게 된다.
# 0-2. 높이가 같거나 아래로 이동할 경우는 추가 비용이 들지 않지만, 높아지면 해당 높이- 현재 높이 만큼 더 비용이 든다.


# # 이건 완전탐색으로 풀어봄
# def gotoend(row, column, cost):
#     global min_cost
#     if min_cost < cost:
#         return

#     if row == N-1 and column == N-1:
#         min_cost = min(min_cost, cost)
#         return

#     for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
#         if 0<= row+dr <N and 0<= column+dc <N:
#             if not visited[row+dr][column+dc]:
#                 visited[row+dr][column+dc] = 1
#                 if matrix[row][column] < matrix[row+dr][column+dc]:
#                     extra_cost = matrix[row+dr][column+dc]-matrix[row][column]
#                     gotoend(row+dr, column+dc, cost+1+extra_cost)    
#                 else:
#                     gotoend(row+dr, column+dc, cost+1)
#                 visited[row+dr][column+dc] = 0

#     pass
# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0]*N for _ in range(N)]
#     min_cost = 0xffffffffffff
#     gotoend(0,0,0)
#     print(f'#{testcase} {min_cost}')

### 그냥 풀어보기
#### 완전실패
# def gotoend(row, column, cost):      
#     global min_cost
#     # if min_cost < cost:
#     #     return
#     if row == N-1 and column == N-1:
#         min_cost = min(cost, min_cost)
#         return
#     tmp_cost = 101
#     tmp_d = 0
#     for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
#         if not visited[row+dr][column+dc] and 0<= row+dr < N and 0<= column + dc < N :
#             if matrix[row+dr][column+dc] > matrix[row][column]:
#                 if tmp_cost > matrix[row+dr][column+dc]-matrix[row][column]+1:
#                     tmp_cost = matrix[row+dr][column+dc]-matrix[row][column]+1
#                     tmp_d = [row+dr, column+dc]
#             else:
#                 if tmp_cost > 1:
#                     tmp_cost = 1
#                     tmp_d = [row+dr, column+dc]
#     visited[row+dr][column+dc] = 1
#     gotoend(row+tmp_d[0], column+tmp_d[1], cost+tmp_cost)

# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0]*N for _ in range(N)]
#     min_cost = 0xfffffffffffff
#     cost = 0
#     gotoend(0,0,0)
#     print(f'#{testcase} {min_cost}')


                

#### dijkstra로 풀어보기


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_cost = 0xffffffffffff
