import sys

a, b, c = map(int, sys.stdin.readline().strip().split())
while a != 0 or b != 0 or c != 0:
    tmp = [0]*1001
    tmp[a] += 1
    tmp[b] += 1
    tmp[c] += 1
    sum_value = a+b+c
    max_value = max(tmp)
    if sum_value - max(a,b,c) <= max(a,b,c):
        print('Invalid')
    elif max_value == 3:
        print('Equilateral')
    elif max_value == 2:
        print('Isosceles')
    elif max_value == 1:
        print('Scalene')
    a, b, c = map(int, sys.stdin.readline().strip().split())