# 문제
# 체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

import sys
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(8)]

count = 0
# 보드 행마다, 열마다 확인
for row in range(8):
    for column in range(8):
        if row%2 == 0:  # 0,2,4,6행
            # 0,2,4,6열이 흰색
            if column % 2 == 0 and board[row][column] == 'F':
                count +=1
            
        else:   # 1,3,5,7 행
            # 1,3,5,7 열이 흰색
            if column % 2 and board[row][column] == 'F':
                count += 1
print(count)

#######
# 이 방법도 있지롱
c = []
for _ in range(8):
    c.append(list(map(str, list(input()))))

n = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if c[i][j] == 'F': 
                n += 1
print(n)