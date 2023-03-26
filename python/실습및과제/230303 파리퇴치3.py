import sys
sys.stdin = open('230303 파리퇴치3.txt','r')

# [문제]
# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다.
# 아래는 N=5 의 예이다.
# 파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
# 다음은 M=3 세기로 스프레이르 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.
# 한 번에 잡을 수 있는 최대 파리수를 출력하라.

# [제약 사항]
# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 다음 N 줄에 걸쳐 N x N 배열이 주어진다.

# [문제풀이]
# 0. 뿌린 위치에서 상하좌우 또는 모든 대각선 방향으로 분사가 되는데 이 때 가장 많이 죽인 파리의수를 구하는 것.
# 0-1. 잡을 때마다 리스트에 추가하거나, max값보다 크면 바꾸거나 하는 식으로 하면 될 듯 하다.
# 1. 판의 크기 N은 5~15이다.
# 1-1. 스프레이의 세기 M은 2~ N으로 주어진다.
# 2. 각 영영별 파리갯수는 30 이하이다.는 그리 중요하진 않다.

T = int(input())
for testcase in range(1, T+1):
    N, M =  map(int, input().split())                               # 판 크기 N, 스프레이 세기M을 입력받음 
    fly_mt = [list(map(int, input().split())) for _ in range(N)]    # 파리가 있는 것을 N만큼 입력받으면서 파리 판을 만들어냄
    # 델타값을 2가지로 둬볼까? 하나는 상하좌우, 하나는 대각선들
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    # 대각선들(좌상,우상,우하,좌하)
    ddr = [-1,-1,1,1]
    ddc = [-1,1,1,-1]

    max_fly = 0                                                     # 최대 사망파리 수
    for row in range(N):                                            # 스프레이 분사할 행
        for column in range(N):                                     # 스프레이 분사할 열
            # 상하좌우 4방향
            kill_count = fly_mt[row][column]                        # 현재 죽이고 있는 파리
            for i in range(4):                                      # 4방향 돌아가면서 실행
                for j in range(1,M):                                # 현재 위치말고 스프레이가 미치는 영역
                    spray_r = row + dr[i]*j                         # spray로 영향을 미치는 행(상하좌우)
                    spray_c = column + dc[i]*j                      # spray로 영향을 미치는 열(상하좌우)
                    if 0 <= spray_r < N and 0 <= spray_c < N:       # 영향을 미치는 곳이 범위 내라면
                        kill_count += fly_mt[spray_r][spray_c]      # spray로 영향을 미치는 곳의 파리를 킬 카운트에 넣기
            if max_fly< kill_count:                                 # 최대 사망파리 수가 이번 사망파리 수보다 작으면
                max_fly = kill_count                                # 이번이 최대 사망파리 수

            # 대각선 4방향
            kill_count = fly_mt[row][column]                        # 현재 죽이고 있는 파리 수
            for i in range(4):                                      # 4방향 돌아가면서 실행
                for j in range(1,M):                                # 현재 위치말고 스프레이가 미치는 영역
                    spray_r = row + ddr[i]*j                        # spray로 영향을 미치는 행(대각선)
                    spray_c = column + ddc[i]*j                     # spray로 영향을 미치는 열(대각선)
                    if 0 <= spray_r < N and 0 <= spray_c < N:       # 영향을 미치는 곳이 범위 내라면
                        kill_count += fly_mt[spray_r][spray_c]      # spray로 영향을 미치는 곳의 파리를 킬 카운트에 넣기
            if max_fly< kill_count:                                 # 최대 사망파리 수가 이번 사망파리 수보다 작으면
                max_fly = kill_count                                # 이번이 최대 사망파리
    print(f'#{testcase} {max_fly}')