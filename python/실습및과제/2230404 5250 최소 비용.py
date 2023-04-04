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


                

#### BFS로 풀어보기


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0xfffffffffff]*N for _ in range(N)]
    min_cost = 0xffffffffffff
    Q = []
    Q.append((0,0))
    row = 0
    column = 0
    visited[0][0] = 0
    while Q:
        row = Q[0][0]
        column = Q[0][1]
        Q.pop(0)
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            if 0 <= row + dr < N and 0 <= column + dc < N :
                # 다음으로 넘어가는 곳이 더 높으면?
                if  matrix[row + dr][column + dc] >  matrix[row][column]:
                    a = matrix[row + dr][column + dc] - matrix[row][column] +1
                else: a = 1

                value = visited[row][column] + a     # 넣게 될 값은 현재 위치 + a
                if visited[row+dr][column+dc] > value:
                    visited[row+dr][column+dc] = value
                    Q.append((row+dr,column+dc))    


    answer = visited[N-1][N-1]
    print(f'#{testcase} {answer}')


# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[float('inf')]*N for _ in range(N)]
#     Q = [(0,0)]
#     visited[0][0] = 0
#     dr = [-1,1,0,0]
#     dc = [0,0,-1,1]
    
#     while Q:
#         row, column = Q.pop(0)
#         for d in range(4):
#             nr = row+dr[d]
#             nc = column +dc[d]
#             if 0 <= nr < N and 0 <= nc < N :
#                 # 다음으로 넘어가는 곳이 더 높으면?
#                 if  matrix[nr][nc] >  matrix[row][column]:
#                     a = matrix[nr][nc] - matrix[row][column] +1
#                 else: a = 1
#                 value = visited[row][column] + a     # 넣게 될 값은 현재 위치 + a

#                 if value < visited[nr][nc]:
#                     visited[nr][nc] = value
#                     Q.append((nr, nc))

#     answer = visited[N-1][N-1]
#     print(f'#{testcase} {answer}')