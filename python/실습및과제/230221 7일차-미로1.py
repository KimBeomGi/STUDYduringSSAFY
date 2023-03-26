import sys
sys.stdin = open('230221 7일차-미로1.txt', 'r')

# [문제]
# 아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
# 가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
# 아래의 예시에서는 도달 가능하다.

# 아래의 예시에서는 출발점이 (1, 1)이고, 도착점이 (11, 11)이며 도달이 불가능하다.

# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트케이스가 주어진다.
# 테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).

# [문제 풀이]




def find_start(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return (i,j)

def is_can_go(maze):
    # 델타 생성(상,하,좌,우)
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    Q = [0]*(N*N)                                       # 큐 생성
    rear = -1                                           # 큐에 이용할 rear
    front = -1                                          # 큐에 이용할 front
    visited = [[0]*N for _ in range(N)]                 # 방문 기록과 거리를 계산하는 visited 변수 생성
    rear += 1
    Q[rear] = (sp_i, sp_j)                              # Q[rear] 즉, 현재의 Q[0]에 (sp_i, sp_j) 시작 위치를 입력
    visited[sp_i][sp_j] = 1                             # 출발지에 대한 visited 변수 = 1

    while front < rear:                                 # front가 rear보다 작을때만 작동
        front +=1                                       # front에 +1
        now_i = Q[front][0]                             # Q[front]로 보는 현재 위치 값 i
        now_j = Q[front][1]                             # Q[front]로 보는 현재 위치 값 j
        for d in range(4):                              # 주변 델타 값을 확인하기 위해서
            next_i = now_i +dr[d]                       # 델타를 적용한 다음 i
            next_j = now_j +dc[d]                       # 델타를 적용한 다음 j
            if 0<= next_i < N and 0<= next_j < N:       # 델타를 적용시킨 값이 미로 행렬 안에 있을 때
                if maze[next_i][next_j] !=1 and visited[next_i][next_j] == 0:   # 해당 좌표 값이 벽이 아니고, 방문하지도 않았다면
                    rear += 1
                    Q[rear] = (next_i, next_j)
                    visited[next_i][next_j] = visited[now_i][now_j] + 1
                    if maze[next_i][next_j] == 3:
                        return f'#{testcase} 1'
    return f'#{testcase} 0'

T = 10
for testcase in range(1,T+1):
    testcase = int(input())
    N = 16                                              # 미로 크기가 16 by 16이니 N = 16
    maze = [list(map(int,input())) for _ in range(N)]   # 미로 생성
    start_point = find_start(maze)                      # 시작 위치 찾기
    sp_i, sp_j = start_point                            # 시작 위치의 행 위치
    print(is_can_go(maze))