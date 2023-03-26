import sys
sys.stdin = open('230221 6일차-미로의 거리.txt','r')

# NxN 크기의 미로에서 출발지 목적지가 주어진다.
# 이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
# 경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
# 다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

# 13101
# 10101
# 10101
# 10101
# 10021

# 마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
# 0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# [문제풀이]
# 0. n by n 의 미로이다.
# 0-1. 벽은 1, 통로는 0, 출발지는 2, 도착지는 3으로 나타낸다.
# 0-2. 출력값은 출발지에서 도착지까지 도착하는데 있어 거쳐야하는 칸수 (1,0) ~ (5,0)이라면 (2,0)~(4,0)이 지나는 칸이니 총 3칸이다.
# 0-3. 만약 도착할 수가 없다면 0 을 출력하면 된다.
# 1. BFS로 풀어야지롱~
# 1-2. visited와 front, rear 등을 아주 잘 활용해보자 흑흑흑....
# 2. 난 Q를 이용해서 가야할 좌표를 찍을 것이고, visited에 내가 거기까지 몇칸 소요되는지 확인할 것이다.


# 출발지점을 찾는 함수
def find_sp(N, matrix):
    for i in range(N):              # 출발지점의 행
        for j in range(N):          # 출발지점의 열
            if matrix[i][j] == 2:   # 해당 좌표가 출발지점이 확인되면
                return (i,j)        # 해당 좌표를 반환

# Q와 델타를 이용하면서 미로탈출하는 함수
def maze_exit():
    global front
    global rear

    # 출발지 확인 및 출발지에 위치
    start_point = find_sp(N, maze)                              # 이번 테스트케이스에서의 출발 위치 확인(튜플로 확인)
    cp_i = start_point[0]                                       # 출발 행 좌표 확인해서 현재 위치에 입력
    cp_j = start_point[1]                                       # 출발 열 좌표 확인해서 현재 위치에 입력
    visited[cp_i][cp_j] = 1                                     # 내가 현재 출발위치에 있으므로, 방문했음의 1로 표기
    # Q에 출발하는 현재 위치 등록
    rear += 1                                                   # 데이터의 마지막 위치를 의미하는 rear에 +1 해주기
    Q[rear] = (cp_i, cp_j)                                      # Q[rear] 즉, Q[0]에 좌표값을 입력

    # 델타 값 생성(상, 하, 좌, 우)
    dr = [-1,1,0,0]                                             # 행의 델타값 생성
    dc = [0,0,-1,1]                                             # 열의 델타값 생성

    while front <= rear:
        # 델타를 이용해서 현재위치에서 주변 둘러보기        
        for d in range(4):                                                  # 4방향 델타를 사용하기 위한 반복문
            next_i = cp_i + dr[d]                                           # 델타 방향으로 나아갈 다음 행
            next_j = cp_j + dc[d]                                           # 델타 방향으로 나아갈 다음 열
            if 0 <= next_i < N and 0 <= next_j < N:                         # 델타방향으로 나아가려는 위치가 행렬안에 있고, 
                if maze[next_i][next_j] != 1 and visited[next_i][next_j] == 0:              # 델타방향으로 나아가는 미로의 위치가 통로이면서, 미방문 상태라면
                    rear += 1                                               # rear를 한 칸 뒤로 보내고,
                    Q[rear] = (next_i, next_j)                              # Q[rear]에 (next_i, next_j)좌표를 입력
                    visited[next_i][next_j] = visited[cp_i][cp_j] + 1       # visited[next_i][next_j]값을 출발지에서 몇 칸 가야하는지를 기록해주기
                    if maze[next_i][next_j] == 3:                           # 만약 도착지가 발견되면
                        return f'#{testcase} {visited[next_i][next_j]-2}'   # 중간에 찾았으니 해당 구역까지 걸리는 칸 수를 확인하기
        front +=1                                                           # front를 한칸 앞 당겨주고
        if front > rear:                                                    # front가 rear를 넘어서면 더 찾을 값이 없으므로
            return f'#{testcase} 0'                                         # while문을 끝냈는데도 못 찾은 것이니 0을 출력
        cp_i, cp_j = Q[front]                                               # 현재 위치를 조정
    
T = int(input())
for testcase in range(1, T+1):
    N = int(input())                                            # 미로의 크기를 나타내는 N
    maze = [list(map(int, input())) for _ in range(N)]          # 미로의 값을 입력받아 미로 생성하기

    # Q를 이용하기 위해 관련 변수 생성
    visited = [[0]*N for _ in range(N)]                         # 미로의 해당 칸을 방문했는지를 기입하는 visited 변수(출발지에서 도착지까지의 칸을 세아릴 것임)
    Q = [0]*(N**2+1)
    front = rear = -1                                           # Q를 사용할 것이기 때문에 front와 rear를 이용하기 위함.

    print(maze_exit())