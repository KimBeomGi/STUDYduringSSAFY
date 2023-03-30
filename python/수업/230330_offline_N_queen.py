# N이 주어질 때 N*N 크기의 격자판에 N개의 퀸을 놓을 수 있는
# 경우의 수는 몇 개인가?
# 모든 행에 퀸 놓아보기. 단, 하나의 행에는 하나의 퀸만 놓아본다.
# 각 행에서는 모든 경우의 수에 대해서 모두 수행해보기
# (모든 열에 놓아보기)

# row: 퀸을 놓으려는 행의 번호
# 사실 N-queen은 순열과 거의 비슷하다 ㅎㅎ

def nqueen(row):
    global count
    if row == N:            # 모든 행에 퀸이 놓여진 상태
        count += 1
        # print(queen)
        return
    # 행 하나에 퀸 놓고나면
    # 다음행에 퀸 놓기
    # 퀸 놓기 : 모든 열에 퀸 놓기
    for col in range(N):
        # board[row][column] = 1
        if not check_col[col] and not dia1[row+col] and not dia2[row-col+N-1]:
            check_col[col] = 1
            dia1[row+col] = 1       # 이게 중요
            dia2[row-col+N-1] = 1   # 이게 중요
            queen[row] = col        # row행, col열에 퀸을 놓음
            nqueen(row+1)
            check_col[col] = 0
            dia1[row+col] = 0
            dia2[row-col+N-1] = 0
# 대각 1: r+c
# 대각 2: r-c + (N-1)


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    check_col = [0]*N
    board = [[0]*N for _ in range(N)]   
    queen = [0]*N           # 퀸이 어디에 놓여져 있는지 표시하는 배열
    count = 0
    dia1 = [0] *(2*N-1)    # 대각선1의 갯수
    dia2 = [0] *(2*N-1)    # 대각선2의 갯수
    nqueen(0)
    print(count)