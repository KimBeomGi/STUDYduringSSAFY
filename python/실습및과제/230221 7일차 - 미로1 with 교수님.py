# 목적지에 도착가능하면 1, 아니면 0을 반환
def solve():
    #시작점 찾고 bfs 수행
    si, sj = 0,0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si, sj = i, j
    # bfs 수행
    # 현재노드에서 갈 수 있는 모든 노드를 순서대로 저장하고, 저장한 순서대로 방문하는 방법. 먼저 발견한 곳으로 방문
    queue = []  # 방문할 노드를 저장하는 queue
    # 방문표시를 위한 배열
    visited = [[0]*16 for _ in range(16)]
    visited[si][sj] = 1
    # 큐에 방문할 노드가 남아있으면, 방문해서 갈 수 있는 경로가 있는지 확ㅇ니하고
    # 있으면 큐에 추가하기
    
    #델타 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    while queue:
        # 가장 먼저 발견한 노드를 빼서 경로 확인
        ci, cj = queue.pop(0)
        # 인접한 네 방향 검사, 갈 수 있는 길이 있는가
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            # 통로이면서 방문하지 않은 노드라면... 방문하겠소이다!!!
            if maze[ni][nj] == 0 and not visited[ni][nj]:
                queue.append((ni,nj))
                visited[ni][nj] = 1
            # 위에서 통로만 검사했으니 목적지는 무시하니까 따로 검사
            elif maze[ni][nj] == 3:
                return 1
            
    # 내가 갈 수 있는 경로를 모조리 queue에 넣었는데 목적지를 못찾음.
    return 0

T = 10
for testcase in range(1,T+1):
    testcase = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]     # .strip()은 공백 없애는 작업. 리눅스와 윈도우 환경에서의 차이로 인해.
    result = solve()
    print(f'#{testcase} {result}')