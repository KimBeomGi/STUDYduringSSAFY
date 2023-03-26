arr= [
[0, 0, 1, 0, 0],
[0, 1, 1, 1, 1],
[0, 0, 1, 1, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0],
]
N = 5
# 연결된(상하좌우로) 1의 갯수 찾기
# 횡 우선 탐색하다가 1 발견하면 1 연결된거 보고 보고, 하면서 쭉 갈것임.
queue = []          # 리스트지만... 맨 뒤에 넣고 앞에서 뺄꺼니까.. queue라고 합시다.
# 2차원 배열에서 각 요소가 노드 이므로... 모든 정점에 대해서 방문표시
visited= [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            # 여기에서 bfs 시작
            queue.append((i,j))
            # 또는 한개씩 2개 넣기
            # queue.append(i)
            # queue.append(j)
            visited[i][j] = 1       # 방문했음 표시
            # 현재위치에서 갈 수 있는 모든 경로를 탐색
            # 경로를 발견하면 저장
            # 이후에 경로를 발견한 순서대로 방문(deQueue)
            cnt = 0         # 방문할 때 마다 cnt를 증가시키려고
            while queue:    #큐에 저장된 노드를 방문하는 작업을 반복(큐에 저장값이 있다면 계속 반복)
                # 현재 위치
                ci, cj = queue.pop(0)  # 먼저 발견한 순서대로 방문(현재 i, 현재 j를 받음)
                cnt += 1    # 방문할 때 마다 cnt를 증가시킴
                for di, dj in ([(-1,0),(1,0),(0,-1),(0,1)]):
                    ni, nj = ci + di, cj + dj           # next (i, j)
                    # 정상 범위 안에 있으면서,
                    if 0<= ni < N and 0<= nj < N:
                        # 1이고, 방문하지도 않았으면, 방문할 노드에 추가
                        if arr[ni][nj] == 1 and not visited[ni][nj]:
                            queue.append((ni, nj))
                            visited[ni][nj] = visited[ci][cj] + 1   # 현재 위치에서 갈 수 있는 경로
            print(cnt)
            print('여러번 실행될걸요?ㅋㅋㅋㅋㅋㅋ')