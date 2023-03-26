import sys
sys.stdin = open('파이썬 sw문제해결 기본-stack2 5차시 5일차-미로.txt', 'r')
# NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
# 주어진 미로 밖으로는 나갈 수 없다.
# 다음은 5x5 미로의 예이다. 

# 13101

# 10101

# 10101

# 10101

# 10021

# 마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
 
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

# [문제풀이]
# 0. N by N 크기의 미로를 탈출해야한다.
# 1. 0이 움직일 수 있는 곳이며, 1은 벽이다.
# 1-1. 2는 출발지이고, 3은 도착지이다.
# 2. 상하좌우 움직여야 하므로 델타 값을 이용해서 풀어보자.
# 3. 출력값으로 'error'를 출력해라 해놓고는 0을 출력하게 한다. 주의

def can_exit(N, maze):
    # 상하좌우 델타 생성
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    stack = [0]*(N*N)                                           # stack 생성 
    top = -1                                                    # stack에 이용될 top생성
    visited = [[0]*N for _ in range(N)]                         # visited 행렬 생성
    # 출발지의 위치를 찾기 위함
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:                                 # 미로의 출발지를 찾았다면
                start_r = i                                     # 출발 행위치 변수 생성
                start_c = j                                     # 출발 열위치 변수 생성
    
    # 미로 찾기
    top += 1                                                    # top을 한 칸 올려줌
    stack[top] = (start_r, start_c)                             # stack[top]에 미로 출발 지점 좌표를 넣기
    while top > -1:
        now_r = stack[top][0]
        now_c = stack[top][1]
        if maze[now_r][now_c] == 3:
            return 1 
        
        for i in range(4):                                      # 델타 값을 확인하기
            now_r = now_r + dr[i]
            now_c = now_c + dc[i]
            if 0 <= now_r < N and 0 <= now_c < N and maze[now_r][now_c] != 1 and visited[now_r][now_c] == 0:
                top += 1
                stack[top] = (now_r, now_c)
                visited[now_r][now_c] = 1
                break
        else:
            top -= 1
    return 0

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]          # 미로 생성
    answer = can_exit(N, maze)
    print(f'#{testcase} {answer}')


#     while top > -1:                                             # 활용가능한 stact 값이 있다면
#         for i in range(4):                                      # 델타 4방향을 확인함
#             if 0 <= stack[top][0]+dr[i] < N and 0 <= stack[top][1]+dc[i] < N and maze[stack[top][0]+dr[i]][stack[top][1]+dc[i]] == 3:
#                 return f'{testcase} 1'
#             while 0 <= stack[top][0]+dr[i] < N and 0 <= stack[top][1]+dc[i] < N and visited[stack[top][0]+dr[i]][stack[top][1]+dc[i]] != 1  and maze[stack[top][0]+dr[i]][stack[top][1]+dc[i]] != 1:
#                 stack[top+1] = (stack[top][0]+dr[i], stack[top][1]+dc[i])
#                 top += 1
#                 visited[stack[top][0]][stack[top][1]] = 1
#                 break
#         top -= 1                                                # while 문이 끝나고 델타값도 끝났다면 더 갈 수 있는 곳이 없는 곳이므로 top에서 -1을 해준다.
#     return f'{testcase} 0'


# T = int(input())
# for testcase in range(1,T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]          # 미로 생성
#     print(can_exit(N, maze))

# top = -1
# stack = [0]*10
# top+=1
# start_r = 1
# start_c = 2
# stack[top] = (start_r, start_c) 
# print(stack)
# now_r, now_c = stack[top]
# print(now_r, now_c)