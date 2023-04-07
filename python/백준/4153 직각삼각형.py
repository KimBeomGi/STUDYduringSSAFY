import sys

lines = list(map(int, sys.stdin.readline().strip().split()))

while sum(lines) != 0:
    lines.sort()
    if lines[0]**2 + lines[1]**2 == lines[2]**2:
        print('right')
    else:
        print('wrong')
    lines = list(map(int, sys.stdin.readline().strip().split()))