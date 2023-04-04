# 서로소 집합을 이용한 find_set, union 구현
def find_set(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        p[py] = px

# 크루스칼 알고리즘 구현
def kruskal(graph):
    edges = []
    mst = []
    total_weight = 0
    
    # 그래프의 모든 간선을 edges 리스트에 추가
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))
    
    # 간선들을 가중치 오름차순으로 정렬
    edges.sort()

    # 각 정점을 집합으로 만들어서 초기화
    global p
    p = [i for i in range(len(graph))]

    # 모든 간선에 대해 최소 신장 트리를 구성하기 위한 과정
    for edge in edges:
        weight, u, v = edge
        # 사이클이 생기지 않는 경우 해당 간선 선택
        if find_set(u) != find_set(v):
            union(u, v)
            mst.append(edge)
            total_weight += weight
    
    return mst, total_weight

graph = [
    [0, 2, 3, 0],
    [2, 0, 0, 4],
    [3, 0, 0, 1],
    [0, 4, 1, 0]
]
mst, total_weight = kruskal(graph)
print(mst)
print(total_weight)