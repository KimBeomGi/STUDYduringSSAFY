import sys

def prim(n, graph):
    # 임의의 시작점을 선택
    start_node = 0
    
    # 선택된 정점을 저장하는 리스트
    selected = [False] * n
    
    # 시작점을 선택하고, 해당 정점과 연결된 간선들을 저장하는 리스트
    selected[start_node] = True
    edges = []
    for i in range(n):
        if graph[start_node][i] != 0:
            edges.append((start_node, i, graph[start_node][i]))
    
    # 트리의 간선들과 가중치의 합을 저장하는 변수
    mst = 0
    
    # MST 구성
    while edges:
        # 가장 작은 가중치를 갖는 간선을 선택
        e = min(edges, key=lambda x: x[2])
        edges.remove(e)
        
        # 선택된 간선으로부터 연결된 정점
        u, v, w = e
        if not selected[v]:
            selected[v] = True
            mst += w
            for i in range(n):
                if graph[v][i] != 0:
                    edges.append((v, i, graph[v][i]))
    
    return mst

n = 5
graph = [
    [0, 2, 3, 4, 0],
    [2, 0, 0, 5, 6],
    [3, 0, 0, 0, 1],
    [4, 5, 0, 0, 7],
    [0, 6, 1, 7, 0]
]

mst = prim(n, graph)

print(mst)  # 10


# 위 코드는 입력으로 인접 행렬 graph와 정점의 개수 n을 받아서,
# Prim 알고리즘을 실행한 후 MST의 가중치의 합을 출력합니다. 
# 예제 그래프에서 Prim 알고리즘을 실행하면 MST의 가중치의 합이 10이 되어야 합니다.