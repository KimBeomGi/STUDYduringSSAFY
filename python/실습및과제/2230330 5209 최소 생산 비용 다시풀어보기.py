import sys
sys.stdin = open('2230330 5209 최소 생산 비용.txt','r')


def find_mincost(product, cost):
    global min_cost

    if min_cost < cost:
        return
    if product == N:
        if min_cost > cost:
            min_cost = cost
        return
    
    for j in range(N):
        if used[j] == 0:
            used[j] = 1
            find_mincost(product+1, cost+factories[product][j])
            used[j] = 0

T = int(input())
for testcase in range(1, T+1):
    N = int(input())                # 행과 열의 각 갯수
    factories = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 99*N*N
    used = [0]*N
    find_mincost(0, 0)
    print(f'#{testcase} {min_cost}')