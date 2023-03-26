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

import sys
sys.stdin = open('230215 5일차-미로.txt', 'r')

# [문제풀이]
# 0. 갈 수 있는 길은 0으로 표시 되어있고, 벽은 1로 표시 되어있다.
# 0-1. 출발점은 2이고, 도착점은 3으로 표시되어있으며, 이는 행렬로서 표현 되어 있음을 확인할 수 있다.
# 1. DFS를 이용하되, 조건을 걸어서 3에 도착하면 바로 출력되도록 한다. 따라서 함수로 이용해보자.
# 1-1. 미로에서 이동할 수 있는 것은 인접한 상하좌우가 되겠다.
# 2. 델타변수를 이용해서 하나씩 움직여보도록하자.

# 출발 위치 확인하기
def start_position(matrix):
    for i in range(N):                                                  # 행 찾기
        for j in range(N):                                              # 열 찾기
            if matrix[i][j] == '2':
                return (i, j)                                           # 출발 위치를 (행,열)로 반환

# 미로 탈출 가능 여부 확인하기
def can_exit(row, column, matrix):                                      # 출발 위치와 미로를 입력받아 함수 실행
    # 델타 (상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]                                                  # 행에 대한 델타변수
    dc = [0, 0, -1, 1]                                                  # 열에 대한 델타변수
    stack = [(row, column)]                                             # 미로 탈출 가능 여부 함수에서 사용 할 stack 변수
    is_went = [[0]*N for _ in range(N)]                                 # 해당 위치를 방문했는지를 확인 가능한 is_went 행렬 생성
    is_went[row][column] = 1                                            # 우선 현재위치는 방문한 곳이 되니 is_went 행렬에서 시작 위치를 1로 표현해줌

    # 미로 찾기 작동
    while stack :                                                       # 스택에 값이 있다면 while문을 작동
        current_row, current_column = stack[-1]
        if matrix[current_row][current_column] == '3':                    # 만약 현재 위치가 3 이면
            return 1                                                    # 함수를 종료시키고 미로 탈출 완료!
        for i in range(4):                                              # 0~3을 요소로하는 i를 반복문을 돌리면서 델타값으로 이동이 가능한지 확인하기 위함
            now_row = current_row + dr[i]
            now_column = current_column + dc[i]
            # 미로에서 나아가려는 방향이 벽에 안막혀 있고, 들리지도 않았다면
            if 0<= now_row <N and 0<= now_column <N and matrix[now_row][now_column] != '1' and is_went[now_row][now_column] == 0:
                stack.append((now_row, now_column))                     # 나아가려는 방향으로 나아가서 현재위치를 stack에 추가 바꿔라
                is_went[now_row][now_column] = 1                        # 나아가려는 방향으로 나아간 현재위치를 방문했음으로 표시
                break
        else:                                                           # 4방향모두 갈 길이 없다면 stack.pop()으로 이전으로 되돌아가기
            stack.pop()
    return 0                                                      # while문을 돌렸음에도 탈출이 불가능했기 때문에 0을 반환
            

T= int(input())
for testcase in range(1, T+1):
    N = int(input())                                                    # 미로 행렬에 사용될 가로 세로 크기
    maze_matrix = [list(map(str,input())) for _ in range(N)]            # 미로 행렬 제작(입력받음)

    # 출발 위치를 기점으로 미로 탈출 가능한지 여부 확인하기
    row, column = start_position(maze_matrix)
    print(f'#{testcase} {can_exit(row, column , maze_matrix)}')