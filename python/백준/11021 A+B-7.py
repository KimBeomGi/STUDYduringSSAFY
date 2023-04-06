import sys

T = int(sys.stdin.readline().strip())
for testcase in range(1,T+1):
    A, B = map(int, sys.stdin.readline().strip().split())
    print(f'Case #{testcase}: {A+B}')