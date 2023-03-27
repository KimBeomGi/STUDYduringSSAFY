import sys
sys.stdin = open('5188 최소합.txt', 'r')
# NxN 배열 에서 목적지까지 가야한다
# 방향은 오른쪽 또는 아래로만 이동 가능
# 이동하면서 지나가는 칸의 숫자를 더해가면서 목적지에 도착했을 때 합계가 최소인 값을 출력해라
# 이동 횟수는 N-1번씩 오른쪽과 아래로 움직인다 ex) N = 3 -> 오:2, 아:2
def perm(x, y, sumv):
    global ans
    sumv += board[x][y]
    if y == N-1 and x == N-1: # 목적지에 도착했을 때
        if ans > sumv: # 최소값이 이번 루트의 합계보다 크면은 
            ans = sumv # 값 반환
        return
    elif ans < sumv: # 이미 최소값을 넘겼다면 끝
        return
 
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N: 
            perm(nx, ny, sumv) # 이동한 방향 탐색
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1]
    dy = [1, 0]
    used = [[0]*N for _ in range(N)]
    ans = 1e9 # 출력값
    perm(0, 0, 0)
    print(f'#{tc} {ans}')