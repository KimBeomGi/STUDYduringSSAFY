# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

import sys

x = [0]*1001
y = [0]*1001
for i in range(3):
    x_tmp, y_tmp = map(int, sys.stdin.readline().strip().split())
    x[x_tmp] += 1
    y[y_tmp] += 1
for i in range(1001):
    if x[i] == 1:
        answer_x = i
        break
for i in range(1001):
    if y[i] == 1:
        answer_y = i
        break
print(answer_x, answer_y)