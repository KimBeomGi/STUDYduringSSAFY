def kruskal(V, E, edges):
    # 서로소 집합 생성 및 초기화
    parent = [i for i in range(V)]
    rank = [0] * V

    # 가중치를 기준으로 간선 정렬
    edges.sort(key=lambda x: x[2])

    mst = []  # 최소 스패닝 트리에 포함되는 간선들의 리스트

    for edge in edges:
        u, v, weight = edge
        # u와 v가 서로 다른 집합에 속해 있으면 합집합 연산 수행
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append(edge)
            if len(mst) == V-1:  # MST를 완성한 경우 종료
                break

    return mst


def find(parent, x):
    if parent[x] == x:
        return x
    else:
        return find(parent, parent[x])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


V = 7
E = 11
edges = [
    (0, 1, 7),
    (0, 3, 5),
    (1, 2, 8),
    (1, 3, 9),
    (1, 4, 7),
    (2, 4, 5),
    (3, 4, 15),
    (3, 5, 6),
    (4, 5, 8),
    (4, 6, 9),
    (5, 6, 11),
]

mst = kruskal(V, E, edges)

print(mst)
