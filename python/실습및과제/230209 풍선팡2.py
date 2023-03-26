# [문제]
# 종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다.
# 다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
# NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.
# (3<=N, M<=100)

# 입력
# 첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.

# 출력
# #과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.

import sys
sys.stdin = open('230209 풍선팡2.txt', 'r')


# [문제풀이]
# 0. N by M개의 행렬로 되어 있다. 하나를 터뜨리면 좌우상하의 풍선이 같이 터지면서 꽃가루가 날린다.
# 0-1. 풍선이 가장 적게 터지는 경우의 수는 제일 구석모퉁이에 있는 경우로 자기자신 포함 총 3개가 터지는 경우이다.
# 0-2. 각 풍선별로 들어있는 꽃가루 수는 다르기 때문에 꼭 같다고는 구석에 있는 것이 적다고 할 수는 없다.
# 1. 하나의 풍선만 터뜨리면 되고 기본적으로는 리스트[행][열] 리스트[행+1][열] 리스트[행-1][열] 리스트[행][열+1] 리스트[행][열-1]이 같이 터진다고 보면된다.
# 1-1. 이때 1.에서 각 인덱스가 가지는 숫자들을 모두 더해서 제일 큰 수를 출력하면 된다.
'''
T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())                                # 행 N과 열 M을 받음
    matrix = [list(map(int, input().split())) for _ in range(N)]    # 입력값으로 행렬을 만듬
    
    max_flower = 0                                                  # 최대 터지는 꽃 수
    now_flower = 0                                                  # 이번에 터진 꽃 수
    for row in range(N):                                            # 행의 수인 N만큼 반복
        for column in range(M):                                     # 열의 수인 M만큼 반복
            # 각 모퉁이에서 풍선을 터뜨리려고 하는 경우
            if row == 0 and column == 0:                            # 좌측 상단 모서리
                now_flower += matrix[row][column]
                now_flower += matrix[row][column+1]
                now_flower += matrix[row+1][column]
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0
            elif row == N-1 and column == 0:                        # 좌측 하단 모서리
                now_flower += matrix[row][column]
                now_flower += matrix[row-1][column]
                now_flower += matrix[row][column+1]
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0
            elif row == 0 and column == M-1:                        # 우측 상단 모서리
                now_flower += matrix[row][column]
                now_flower += matrix[row+1][column]
                now_flower += matrix[row][column-1]
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0
            elif row == N-1 and column == M-1:                      # 우측 하단 모서리
                now_flower += matrix[row][column]
                now_flower += matrix[row-1][column]
                now_flower += matrix[row][column-1]
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0
            
            # 각 라인 끝에 있는 경우
            elif row == 0:                                          # 제일 위 라인
                now_flower += matrix[row][column]
                now_flower += matrix[row+1][column]
                now_flower += matrix[row][column-1]
                now_flower += matrix[row][column+1]
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0
            elif row == N-1:                                        # 제일 아래 라인
                now_flower += matrix[row][column]
                now_flower += matrix[row-1][column]
                now_flower += matrix[row][column-1]
                now_flower += matrix[row][column+1]
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0
            elif column == 0:                                       # 제일 왼쪽 라인
                now_flower += matrix[row-1][column]
                now_flower += matrix[row+1][column]
                now_flower += matrix[row][column]
                now_flower += matrix[row][column+1]
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0
            elif column == M-1:                                     # 제일 오른쪽 라인
                now_flower += matrix[row-1][column]
                now_flower += matrix[row+1][column]
                now_flower += matrix[row][column-1]
                now_flower += matrix[row][column]
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0                

            # 5개가 다 터지는 경우
            else:
                now_flower += matrix[row][column]                       # 해당 풍선 꽃잎 더하기
                now_flower += matrix[row][column+1]                     # 해당 풍선 오른쪽 꽃잎 더하기
                now_flower += matrix[row][column-1]                     # 해당 풍선 왼쪽 꽃잎 더하기
                now_flower += matrix[row+1][column]                     # 해당 풍선 아래쪽 꽃잎 더하기
                now_flower += matrix[row-1][column]                     # 해당 풍선 위쪽 꽃잎 더하기
                if max_flower < now_flower:
                    max_flower = now_flower
                    now_flower = 0
                else:
                    now_flower = 0

    print(f'#{testcase} {max_flower}')
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
 
    max_v = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
 
    for i in range(N):
        for j in range(M):
            cnt = board[i][j]
            for k in range(4):
                di = i+dr[k]
                dj = j+dc[k]
                if 0 <= di < N and 0 <= dj < M:
                    cnt += board[di][dj]
            if cnt > max_v:
                max_v = cnt
    print(f'#{tc} {max_v}')