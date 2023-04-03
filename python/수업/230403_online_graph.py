'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split())
arr = list(map(int, input().split()))   # arr
adjM =[[0]*(V+1) for _ in range(V+1)]   # 인접행렬 adjM
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1        # 방향이 없는 경우
    adjL[n1].append(n2)
    adjL[n2].append(n1)     # 방향이 없는 경우

print()