T = int(input())
 
for tc in range(1, T+1):
    V, E = map(int, input().split())    # 노드 개수, 간선 정보
    data = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())    # 출발 노드, 도착 노드
    arr = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
 
    for i in range(E):
        arr[data[i][0]][data[i][1]] = 1
        arr[data[i][1]][data[i][0]] = 1
 
 
    Q = [S]
    visited[S] = 1
 
    while Q:
        c = Q.pop(0)  # current. 현재값
 
        for i in range(V+1):
            if arr[c][i] and not visited[i]:
                Q.append(i)
                visited[i] = visited[c] + 1
 
    if not visited[G]:
        ans = 0
    else:
        ans = visited[G]-1
 
    print(f'#{tc} {ans}')