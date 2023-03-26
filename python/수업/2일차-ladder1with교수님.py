import sys
sys.stdin = open('ladder1_input.txt', "r")
T = 10
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 시작 점 찾기 : 0번 행에서 1인 인덱스를 찾기
    # 0번: 하, 1번: 좌, 2번: 우
    dr = [1,0,0]
    dc = [0,-1,1]
    result = 0
    for i in range(100):        # 100번열 까지 다 봐야지.
        if ladder[0][i] == 1:
        # 시작점 마다 사다리 타기 시작
            dir = 0             # 아래 방향 시작
            r , c = 0, i        # r은 첫번째 행, c는 시작위치
            # 한칸씩 이동하기를 반복 >>> 목적지 도착하기 전까지 반복
            # r이 99행이 될 때 까지 반복
            while r < 99:
                # 특정한 상황에서 방향을 바꿔주어야 합니다.
                #1. 아래쪽으로 내려오는 경우
                if dir == 0:
                    # 좌, 우에 1이 있으면 방향 전환
                    if c >0 and ladder[r][c-1] == 1:            # 맨 왼쪽이면 [0] 인데 [-1]을 보게 되는 거 방지
                        dir = 1
                    elif c < 99 and ladder[r][c+1] ==1:         # 맨 오른쪽이면 [99] 인데 터지는 거 방지
                        dir = 2
                #2. 좌, 우 방향으로 움직일 경우
                    # 아래 방향에 1이 있으면 방향 전환
                else:
                    # 도착지가 1, 2인 경우가 있으니 0이 아니면으로 검사
                    if ladder[r+1][c] != 0:                     # 아래 방향이 1이면 또는 2이면(그러니까 사다리라인이 있으면)
                        dir = 0
                # 한 칸씩 이동하기 현재 방향으로
                r += dr[dir]
                c += dc[dir]
            # r = 99, c = x
            if ladder[r][c] == 2:       # 목적지 찾음
                # 저 위의 i 가 정답
                result = i
                break                   # 더 이상 출발할 필요가 없음
    
    print(f'#{tc} {result}')