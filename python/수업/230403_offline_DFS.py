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

# 그래프 순회하기 : 그래프 시작 정점은 1로 가정
# DFS : 경로를 찾으면 이동했다가, 길이 막히면 갈림길로 다시 돌아와서
#       탐색 하지 않은 경로를 탐색시작
#       왔던 경로로 되돌아가기 위해서... 경로를 저장할건데
#       되돌아 가는 방법은, 방문했던 경로를 마지막 방문했던 위치부터 삭제하면서
#       되돌아 갈 수 있다.  >>  stack의 특성과 일치
#       스택에 방문 경로를 저장하기
# start: 시작정점
def dfs(start):
    stack = []      # 방문 경로를 저장하기 위한 stack
    # 방문했던 정점을 다시 방문하는 것을 막기 위해서 방문확인용 배열
    visited = [0] * (V+1)   # 정점의 인덱스를 이용할것이기 때문에 정점을 이용
    stack.append(start)
    visited[start] = 1

    # 현재 위치(스택에 마지막에 추가된 위치) 에서 갈 수 있는 경로를 모두 찾을 것
    # 완전탐색

###### 되돌아오는 경로까지 출력하겠다 하면 아래 코드임.
    while stack:            # stack에 노드가 있으면 게속 반복
        current = stack[-1]
        # 현재위치에서 연결되어 있는 노드들 모두 살펴보기
        # 갈 수 있으면 바로 이동하기
        # print(current,end=' ')
        
        for i in range(1, V+1):
            # 현재 위치에서 i번 노드로 갈 수 있는지 확인
            # i번 노드가 current노드와 연결되어 있고, 방문하지 않았으면, 방문
            if adjacency[current][i] and not visited[i]:
                stack.append(i)
                print(i,end=' ') # 스택에 들어갈 때, 방문 경로를 출력
                visited[i] = 1
                break   # 현재위치에서 다른 노드로 가는 경로를 찾는 일을 멈춤
        
        else:   # for문에서 break가 실행되지 않았으면: 경로를 찾지 못했으면
            stack.pop()
    
    # while문이 끝나면 dfs는 종료

dfs(1)
print('---------------------')


# 재귀를 활용한 dfs 작성
# v : 현재 정점
# visited = [0] * (V+1)
# ajd: 인접행렬
# visited : 중복방문 방지
def dfs2(v, adj, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in range(V+1):
        if adj[v][i] and not visited[i]:
            # 방문해라!
            dfs2(i, adj, visited)

dfs2(1, adjacency, [0]*(V+1))