def kruskal(n, edges):
    # 부모 노드를 저장하는 리스트, 초기값은 자기 자신
    parent = [i for i in range(n)]
    
    # 두 노드를 연결하는 간선들을 저장하는 리스트
    mst = []
    
    # 각 노드의 루트 노드를 찾는 함수
    def find(node):
        if node == parent[node]:
            return node
        parent[node] = find(parent[node])
        return parent[node]
    
    # 두 노드를 합치는 함수
    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        parent[root2] = root1
    
    # 가중치를 기준으로 간선들을 오름차순으로 정렬
    edges.sort(key=lambda x: x[2])
    
    # 모든 간선에 대해 순회하며 MST 구성
    for u, v, w in edges:
        # 두 노드의 루트 노드가 다른 경우 (사이클을 생성하지 않는 경우)
        if find(u) != find(v):
            # 두 노드를 연결하고 mst 리스트에 추가
            union(u, v)
            mst.append((u, v, w))
    
    return mst
n = 5
graph = [
    [0, 2, 3, 4, 0],
    [2, 0, 0, 5, 6],
    [3, 0, 0, 0, 1],
    [4, 5, 0, 0, 7],
    [0, 6, 1, 7, 0]
]

# 간선 리스트 생성
edges = []
for i in range(n):
    for j in range(i+1, n):
        if graph[i][j] != 0:
            edges.append((i, j, graph[i][j]))

# MST 구하기
mst = kruskal(n, edges)

# 결과 출력
for u, v, w in mst:
    print(f"({u}, {v}) : {w}")
