'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
adj_list = [[] for _ in range(V+1)]
data = list(map(int, input().split()))
for i in range(0, E*2, 2):  # 2칸씩 띄워서
    adj_list[data[i]].append(data[i+1])
    adj_list[data[i+1]].append(data[i])

# 지금부터 bfs
# 현재 위치에서 방문할 수 있는 모든 경로를 일단 저장
# 저장한 순서대로 방문하기
visited = [0]*(V+1)
queue = [1]  #
visited[1] = 1
while queue:
    # dfs와는 다르게 다시 돌아올 일이 없음. 따라서 빼고 시작
    front = queue.pop(0)
    print(front, end = ' ')
    # 현재 노드에서 방문할 수 있는 경로 탐색하기
    for node in adj_list[front]:            # front랑 node랑 연결됨
        if not visited[node]:               # = if visited[node] == 0:, node에 방문하지 않았으면, 방문 목록에 저장
            queue.append(node)
            visited[node] = 1
print()
print('끝')