import sys
sys.stdin = open('20230224 탈주범 검거.txt','r')


# BFS를 이용해보자.
# 총 7개의 터널이 있다.
# 각 터널별로 상하, 좌우로 움직일 수 있는 것 2개
# 좌,상 또는 좌,하로 움직일 수 있는 것 2개
# 우,상 또는 우,하로 움직일 수 있는 것 2개
# 상하좌우가 연결되어있는 터널 1개가 있다.
# 구현은 어떻게 해볼까?

T= int(input())
for testcase in range(1, T+1):
    N, M, R, C, L = map(int, input().split())       # 터널 세로크기 N, 가로크기 M, 맨홀 뚜껑 세로R,가로C, 소요 시간 L
    tunnel = [list(map(int,input().split())) for _ in range(N)]
    # 1~7이 터널마다 표기. 이걸 이용해볼까?
    now_r = R
    now_c = C 
    if (R,C) == 1:
        for i in range(-1, 2, 2):
            (R+i, C) in (1, 2, 5, 6)
            pass
        for j in range(-1, 2, 2):
            (R+i, C) in (1, 2, 5, 6)