# [문제]
# N x N 행렬이 주어질 때,
# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

# [제약 사항]
# N은 3 이상 7 이하이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
# 다음 N 줄에는 N x N 행렬이 주어진다.

# [출력]
# 출력의 첫 줄은 '#t'로 시작하고,
# 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
sys.stdin = open('230210 숫자배열회전.txt', 'r')

# [문제풀이]
# 0. 정사각형으로 이루어진 숫자행렬이 주어지면 그 숫자를 90도,180도 270도 돌린 순서대로 해당 행렬을 출력하는 문제이다.
# 1. 우선 테스트 케이스를 입력받는 것을 행렬입력받듯이 받고, 그것을 (0,0) (2,0)식으로 각 위치로 표현해보자.
# 1-1. (0,0) (2,0) 이 위치가 90도 돌렸을 때 180도 돌렸을때, 270도 돌렸을 때 어느 위치에 있는지 파악하고,
# 1-2. 그 위치로 가기 위해서 어떤 방법을 사용해야하는지만 확인하면 풀 수 있을 듯 하다.
# 2. 현재 위치의 요소가 다음 위치의 인자로 바뀔 수 있도록 하는 방법만 알면 빨리 풀릴 듯.

T= int(input())
for testcase in range(1,T+1):
    N = int(input())
    matrix = [list(map(str, input().split())) for _ in range(N)]        # 정사각형 행렬 생성
    
    # 90도 돌림
    def degree90(matrix):                                               # 90도 돌리는 함수 생성
        matrix_90 = [[0]*N for _ in range(N)]                           # 90도 돌린 행렬을 집어넣을 행렬
        for i in range(N):                                              # 현재 위치에 사용될 인자 i
            for j in range(N):                                          # 현재 위치에 사용될 인자 j
                matrix_90[i][j] = (matrix[N-1-j][i])                    # 90도 돌리니까 이렇게 됨
        return matrix_90
    
    # 180도 돌림
    def degree180(matrix):                                              # 180도 행렬을 돌리는 함수 생성
        matrix_180 = [[0]*N for _ in range(N)]                          # 180도 돌린 행렬을 집어넣을 행렬
        for i in range(N):                                              # 현재 위치에 사용될 인자 i
            for j in range(N):                                          # 현재 위치에 사용될 인자 j
                matrix_180[i][j] = degree90(matrix)[N-1-j][i]           # 180도 돌리니까 이렇게 됨(90도 돌리고 또 90도)
        return matrix_180
    
    # 270도 돌림
    def degree270(matrix):                                              # 270도 행렬을 돌리는 함수 생성
        matrix_270 = [[0]*N for _ in range(N)]                          # 270도 돌린 행렬을 집어넣을 행렬
        for i in range(N):                                              # 현재 위치에 사용될 인자 i
            for j in range(N):                                          # 현재 위치에 사용될 인자 j
                matrix_270[i][j] = degree180(matrix)[N-1-j][i]          # 270도 돌리니까 이렇게 됨(90도 돌리고 또 90도 또 90도)
        return matrix_270

    # print(matrix)
    # print(degree90(matrix))
    # print(degree180(matrix))
    # print(degree270(matrix))
    print(f'#{testcase}')
    for list_row in range(N):                                           # 행별로 출력하기 위해서
        print(f"{''.join(degree90(matrix)[list_row])}", end =' ')       # 90도 돌린 리스트 출력 띄어쓰기 후 다음을 이어서 출력해야 하므로 end=''
        print(f"{''.join(degree180(matrix)[list_row])}", end =' ')      # 180도 돌린 리스트 출력 띄어쓰기 후 다음을 이어서 출력해야 하므로 end=''
        print(f"{''.join(degree270(matrix)[list_row])}")                # 270도 돌린 리스트 출력