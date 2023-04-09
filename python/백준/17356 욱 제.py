import sys

A, B = map(int, sys.stdin.readline().strip().split())
M = (B-A)/400
answer = 1/(1+(10**M))
print(round(answer,10))