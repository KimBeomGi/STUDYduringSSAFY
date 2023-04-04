'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
V, E = map(int, input().split())
graph = [[0xffffff] * (V+1) for _ in range(V+1)]
for i in range(E):
    a, b, w =map(int, input().split())
    graph[a][b] = w
# print(graph)
# start로부터 각 정점으로 가는 비용을 가지는 배열 반환
def dijkstra(graph, start,V):
    weight = [0xffffff]*(V+1)
    # 시작 정점 설정하기
    U = set()               # 경로비용이 확정된 정점의 집합
    weight[start] = 0       # 시작정점에서 시작정점까지 가는 비용은 0

    # U.add(start)
    # 각 정점까지 가는 비용중에 가장 작은 비용이 드는 정점을 선택 >>> 반복
    # 모든 정점이 선택될 대 가지
    while len(U) < (V+1):
        min_v = 0xffffff
        min_idx = 0
        for i in range(V+1):
            # i번 노드까지 가는 비용이 확정되지 않은 정점들 중에서..
            # weight[i]       # 얘네들 중에 최솟값 찾기
            if i not in U and weight[i] < min_v:
                min_v = weight[i]
                min_idx = i
        # weight가 최소인 i를 선택 >> min_idx
        U.add(min_idx)
        # min_idx를 거쳐서 갈 수 있는 정점들의 비용을 재계산
        for i in range(V+1):
            # 원래 알고 있던 i번 정점까지 가는 비용이랑
            # min_idx를 거쳐서 i번 정점까지 가는 비용이랑 비교
            if weight[i] > weight[min_idx]+graph[min_idx][i]:
                weight[i] = weight[min_idx]+graph[min_idx][i]
            weight[i] = min(weight[i], weight[min_idx]+graph[min_idx][i])

    return weight

result = dijkstra(graph,0,V)
print(result)