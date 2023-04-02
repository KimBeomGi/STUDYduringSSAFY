import sys
sys.stdin = open('2230331 14035 격자판의 숫자 이어 붙이기.txt')

def find7(value, row, column, count):
    global answer_set
    if count == 7:
        answer_set.add(value)
        return
    
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:       # 상하좌우
        if 0 <= row+dr < 4 and 0 <= column+dc < 4:
            find7(value+board[row+dr][column+dc], row+dr, column+dc, count+1)

T = int(input())
for testcase in range(1, T+1):
    board = [list(map(str, input().split())) for _ in range(4)]     # 보드판 만들기
    count = 1
    answer_set = set()
    # 보드 판의 모든 위치에서 확인 필요
    for i in range(4):
        for j in range(4):
            find7(board[i][j], i, j, count)
    print(f'#{testcase} {len(answer_set)}')