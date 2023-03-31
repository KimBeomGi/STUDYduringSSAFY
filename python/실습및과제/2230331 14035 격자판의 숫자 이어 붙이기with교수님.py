import sys
sys.stdin=open('2230331 14035 격자판의 숫자 이어 붙이기.txt','r')

# r,c : 현재 좌표
# cards: 움직이면서 만든 숫자카드 순서 모양
# cnt : 움직인 횟수
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def solve(r,c, cards, cnt):
    if cnt == 7:
        print(cards)
        numbers.add(cards)
        return

    # 현재 칸에서 움직일 수 있는 경우의 수: 상하좌우 네칸
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:     # 정상범위 안에 있으면
            solve(nr,nc, cards+data[nr][nc], cnt+1)

T = int(input())
for testcase in range(1, T+1):
    data = [list(input().split()) for _ in range(4)]
    # 모든 격자판의 모든 칸에서 시작해서 7번 움직이는 경우의 수를 모두 계산
    numbers = set()     # 숫자 카드의 모양이 중복되면 안되니까.. set으로 만듬
    for i in range(4):
        for j in range(4):
            solve(i,j,data[i][j], 1)
    print(f'{testcase} {len(numbers)}')