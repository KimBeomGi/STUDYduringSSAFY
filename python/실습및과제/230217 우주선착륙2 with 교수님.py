import sys
sys.stdin = open('230217 우주선착륙2.txt', 'r')

T= int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 모든 칸에서 8방향 검사하기
    # 현재 칸보다 낮은 개수 구하기 4 이상이면 후보지 개수 1 증가
    result = 0              # 후보지 개수
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    
    for r in range(N):
        for c in range(M):
            # data[i][j]가 주변 8개 지역보다 높냐?
            cnt = 0 # 낮은곳이 몇 군데 인지 저장할 변수
            for d in range(8):
                nr, nc = r+dr[d], c+dc[d]
                # 정상범위 안에 있는지 확인
                if 0 <= nr < N and 0 <= nc < M:
                    # 높이 검사
                    if data[r][c] > data[nr][nc]:
                        cnt += 1
            # 8방향 다 돌았는데, 4보다 크면 후보지.
            if cnt >= 4:
                result += 1
    print(f'#{testcase} {result}')