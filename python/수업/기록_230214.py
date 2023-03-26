'''
재귀 호출, 재귀 함수
def f(i, k):
    if i == k:      # 목표에 도달하면
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)


A = [i for i in range(1000)]
B = [0]*1000
f(0,1000)
'''

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
arr =  list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]       # 쌍에서 2개씩 가져올게 하면 이런 방법을 이용할 수도 있다.
    adjM[v1][v2] = 1
    adjM[v2][v1] = 1
    
    adjL[v1].append(v2)
    adjL[v2].append(v1)

print()