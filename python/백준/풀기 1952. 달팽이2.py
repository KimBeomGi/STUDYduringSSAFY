# M, N = map(int, input().split())

# matrix = [[0]*N for _ in range(M)]

# # 우 하 좌 상
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
# delta = 0
# count = 0

# visited = [[0]*N for _ in range(M)]
# cr = 0
# cc = 0


# while 0 <= cr < M and 0 <= cc < N:
#     visited[cr][cc] = 1
#     d = delta % 4
#     nr = cr + dr[d]
#     nc = cc + dc[d]
#     if not (0<= nr < M and 0<= nc <N and visited[nr][nc] == 0):
#         delta += 1
#         count += 1
#     d = delta % 4
#     cr = cr + dr[d]
#     cc = cc + dc[d]
#     if all(visited):
#         break
# print(delta)