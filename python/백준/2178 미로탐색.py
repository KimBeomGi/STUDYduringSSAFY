# # 문제
# # N×M크기의 배열로 표현되는 미로가 있다.

# # 1	0	1	1	1	1
# # 1	0	1	0	1	0
# # 1	0	1	0	1	1
# # 1	1	1	0	1	1
# # 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# # 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# # 입력
# # 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# # 출력
# # 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 입력값
# 4 6
# 101111
# 101010
# 101011
# 111011

# 출력값
# 15

# 입력값
# 4 6
# 110110
# 110110
# 111111
# 111101
# 출력값
# 9

# 입력값
# 2 25
# 1011101110111011101110111
# 1110111011101110111011101
# 출력값
# 38

# 입력값
# 7 7
# 1011111
# 1110001
# 1000001
# 1000001
# 1000001
# 1000001
# 1111111
# 출력값
# 13
from collections import deque

def bfs(start1, start2):
    queue = deque()
    queue.append((start1, start2))  

    while queue:
        start1, start2 = queue.popleft()

        for i in range(4):
            nx = start1 + dx[i]
            ny = start2 + dy[i]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == '1':
                queue.append((nx,ny))
                matrix[nx][ny] = int(matrix[start1][start2]) + 1
    
    return matrix[N-1][M-1]


N, M = map(int, input().split())

matrix = [ list(input()) for _ in range(N)]
# print(matrix)

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False]*M for _ in range(N)]

print(bfs(0,0))