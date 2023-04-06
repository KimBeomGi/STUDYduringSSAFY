import sys

matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]

max_value = 0
max_index = 0
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max_value:
            max_value = matrix[i][j]
            max_index = (i, j)

print(max_value)
print(max_index[0]+1, max_index[1]+1)