import sys
sys.stdin= open('2230404 5251 최소이동거리.txt')

# 문제풀이
T = int(input())
for testcase in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0xffffff] * (V+1) for _ in range(V+1)]
    for i in range(E):
        a, b, w =map(int, input().split())
        graph[a][b] = w
        
    def dijkstra(graph, start,V):
        weight = [0xffffff]*(V+1)
        U = set()
        weight[start] = 0
        while len(U) < (V+1):
            min_v = 0xffffff
            min_idx = 0
            for i in range(V+1):
                if i not in U and weight[i] < min_v:
                    min_v = weight[i]
                    min_idx = i
            U.add(min_idx)
            for i in range(V+1):
                if weight[i] > weight[min_idx]+graph[min_idx][i]:
                    weight[i] = weight[min_idx]+graph[min_idx][i]
                weight[i] = min(weight[i], weight[min_idx]+graph[min_idx][i])

        return weight

    result = dijkstra(graph,0,V)
    print(f'#{testcase} {result[V]}')