
# 이건 작은값부터 찾기
# [입력값]
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#[풀이]
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
data = list(map(int, input().split()))
# for i in range(E):
#     data[i*2] data[i*2+1]
# 또는
for i in range(0, E*2, 2):
    a, b = data[i], data[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
for row in adj:
    print(*row)

# dfs 시작!
# 갈 수 있는 경로를 발견하면 이동하고, 길이 없으면 왔던 길을 되돌아감
# 되돌아 가기 위해서 방문 경로를 저장할 것임

# 재방문을 막기위해서... visited 배열을 사용
def dfs(start):
    # stack을 이용해서 저장하면 편해요!
    stack = []  # 이름만 스택인 리스틀 만들것이고, 다순히 스택처럼 활용하겠다. 경로 저장용 stack
    visited = [0]*(V+1) #[0,1,0,0,0,0,0,0] 방문하자마자 표시하고 시작할 것임.
    stack.append(start)
    visited[start] = 1   #'인접행렬에서 1번노드로 갈 수 있는 녀석을 확인함'
    current = stack[-1] # 현재 위치는 start 즉, stack의 마지막 위치
    # 현재 노드에서 연결된 노드를 확인
    print(start, end=' ')
    while stack:        # 스택이 비어있지 않으면 계속 반복
        current = stack[-1]
        for i in range(1, V + 1):
            if adj[current][i] and not visited[i]:  # i번 노드가 current와 연겨로디어있는지 확인하는 것.
                stack.append(i)
                visited[i] = 1
                print(i, end=' ')
                break  # 연결된 노드 찾기 중단
        else:   # for문 수행중에 경로를 발견하지 못함!!!!!!
            stack.pop()

dfs(1)

'''
# 아래는 큰값부터 찾기
# [입력값]
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#[풀이]
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
data = list(map(int, input().split()))
# for i in range(E):
#     data[i*2] data[i*2+1]
# 또는
for i in range(0, E*2, 2):
    a, b = data[i], data[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
for row in adj:
    print(*row)

# dfs 시작!
# 갈 수 있는 경로를 발견하면 이동하고, 길이 없으면 왔던 길을 되돌아감
# 되돌아 가기 위해서 방문 경로를 저장할 것임

# 재방문을 막기위해서... visited 배열을 사용
def dfs(start):
    # stack을 이용해서 저장하면 편해요!
    stack = []  # 이름만 스택인 리스틀 만들것이고, 다순히 스택처럼 활용하겠다. 경로 저장용 stack
    visited = [0]*(V+1) #[0,1,0,0,0,0,0,0] 방문하자마자 표시하고 시작할 것임.
    stack.append(start)
    visited[start] = 1   #'인접행렬에서 1번노드로 갈 수 있는 녀석을 확인함'
    current = stack[-1] # 현재 위치는 start 즉, stack의 마지막 위치
    # 현재 노드에서 연결된 노드를 확인
    print(start, end=' ')
    while stack:        # 스택이 비어있지 않으면 계속 반복
        current = stack[-1]
        for i in range(V, 0, -1):
            if adj[current][i] and not visited[i]:  # i번 노드가 current와 연겨로디어있는지 확인하는 것.
                stack.append(i)
                visited[i] = 1
                print(i, end=' ')
                break  # 연결된 노드 찾기 중단
        else:   # for문 수행중에 경로를 발견하지 못함!!!!!!
            stack.pop() # 특정한 노드에서 길을 찾지 못하면 POP

dfs(1)
'''

'''
# 아래는 큰값부터 찾기  # 얘는 dfs라고 말하기엔 애매함.....
# [입력값]
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#[풀이]
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
data = list(map(int, input().split()))
# for i in range(E):
#     data[i*2] data[i*2+1]
# 또는
for i in range(0, E*2, 2):
    a, b = data[i], data[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
for row in adj:
    print(*row)

# dfs 시작!
# 갈 수 있는 경로를 발견하면 이동하고, 길이 없으면 왔던 길을 되돌아감
# 되돌아 가기 위해서 방문 경로를 저장할 것임

# 재방문을 막기위해서... visited 배열을 사용
def dfs(start):
    # stack을 이용해서 저장하면 편해요!
    stack = []  # 이름만 스택인 리스틀 만들것이고, 다순히 스택처럼 활용하겠다. 경로 저장용 stack
    visited = [0]*(V+1) #[0,1,0,0,0,0,0,0] 방문하자마자 표시하고 시작할 것임.
    stack.append(start)
    visited[start] = 1   #'인접행렬에서 1번노드로 갈 수 있는 녀석을 확인함'
    current = stack[-1] # 현재 위치는 start 즉, stack의 마지막 위치
    # 현재 노드에서 연결된 노드를 확인
    print(start, end=' ')
    while stack:        # 스택이 비어있지 않으면 계속 반복
        current = stack.pop()       # 이렇게 되면 내가 갈 수 있는 모든 경로 다 살핌!
        print(current, end=' ')
        visited[current] = 1
        for i in range(V, 0, -1):
            if adj[current][i] and not visited[i]:  # i번 노드가 current와 연겨로디어있는지 확인하는 것.
                stack.append(i)
                # break  # 연결된 노드 찾기 중단
        # else:   # for문 수행중에 경로를 발견하지 못함!!!!!!
        #     stack.pop() # 특정한 노드에서 길을 찾지 못하면 POP
dfs(1)
'''