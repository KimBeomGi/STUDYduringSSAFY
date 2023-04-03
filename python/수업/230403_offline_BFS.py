# BFS : 방문경로(예정)를 저장하는 것은 DFS와 동일
# 현재 노드에서 경로를 발견하면... 일단 방문경로에 추가하고
# 추가한 순서대로 방문하기..
# 먼저 추가된 정점을 먼저 방문 (FIFO) : Queue와 동일한 특징

'''
(정점의 갯수 7개 간선의 갯수 8개가 주어진다.)
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# 인접행렬 이용하기
# adjacency = [][]    # 각 노드들이 연결된 정보를 표현
V, E  = map(int, input().split())
data = list(map(int, input().split()))
adjacency = [[0]*(V+1) for _ in range(V+1)]
for i in range(0, E*2, 2):
    adjacency[data[i]][data[i+1]] = 1
    adjacency[data[i+1]][data[i]] = 1
    
    
# start : 시작정점
# 
def bfs(start):
    queue = [start]
    visited = [0] * (V+1)
    visited[start] = 1 
    while queue:
        current = queue.pop(0)     # 다시 현재 위치로 올 필요가 없음.
        print(current, end=' ')
        for i in range(1, V+1):
            if adjacency[current][i] and not visited[i]:
                # 갈 수 있는 곳이니까.. 방문 예정경로에 추가
                queue.append(i)
                visited[i] = 1 
    pass

bfs(1)