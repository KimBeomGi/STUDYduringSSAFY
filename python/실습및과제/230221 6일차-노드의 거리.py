# import sys
# sys.stdin = open('230221 6일차-노드의 거리.txt','r')

# V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
# 주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
# 예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
# 노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
# 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
# E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
# 두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.

# [문제풀이]
# 0. 노드의 갯수 V, 무방향 간선갯수 E와 함께, 각 노드출발-도착, 그리고 최종 출발 S와 도착G가 주어진다.
# 0-1. 이 때 간선을 출발지에서 도착지가지 갈때 지나는 간선의 갯수를 출력해야한다.
'''
def is_can_go(adj_matrix):
    Q = [0]*(E**2 +1)
    front = -1
    rear = -1
    visited = [[0]*(V+1) for _ in range(V+1)]               # 방문을 기록하면서 경로의 길이를 세는 visited 변수

    for i in range(1,V+1):
        if adj_matrix[S][i] == 1:                           # adj_matrix[S][i]가 1이면 간선이 있으므로
            rear += 1                                       # 데이터를 넣을 것이므로 rear +1 해주기
            Q[rear]=(S,i)                                   # Q[rear] = (S.i)로 받아주기
            visited[S][i] = 1                               # visited[S][i] =1로 만들어 방문했음을 나타내줌
    if Q[rear] == 0:
        return f'#{testcase} {0}'

    while front < rear:                                     # front가 rear를 넘어가는 것은 데이터를 쓸 게 없다는 뜻이므로 front < rear
        front += 1                                          # 프론트랑 rear랑 같을때 돌아버리는 것도 방지해주자. front에 +1 해주기
        for i in range(1,V+1):                              # 1~V까지 확인하기
            if visited[Q[front][1]][i] == 0 and adj_matrix[Q[front][1]][i] == 1:    # 방문하지 않았고 경로도 있다면
                rear += 1                                                           # Q에 등록하기 위해 rear를 한칸 뒤로 보내고
                Q[rear] = (Q[front][1], i)                                          # Q[rear]에 새 경로 등록
                visited[Q[front][1]][i] = visited[Q[front][0]][Q[front][1]] +1      # visited는 재 방문 예방을 위해 사용표시 및 경로시 몇회인지 작성
                if i == G:                                                          # i값이 G 도착지라면,
                    return f'#{testcase} {visited[Q[front][1]][i]}'                 # 출력값 출력
    return f'#{testcase} {0}'                               # while을 다 돌리며 확인했는데 없으므로 0 출력


T = int(input())
for testcase in range(1, T+1):
    # 입력값 받기
    V, E = map(int, input().split())                        # 노드갯수 V, 간선갯수 E 입력받음
    adj_matrix = [[0]*(V+1) for _ in range(V+1)]            # 인접행렬 만들기. 노드가 1부터 시작하므로 V+1로 만들어줌
    for _ in range(E):
        a, b = map(int, input().split())                    # 각 노드별 이어주는 간선을 입력받음
        adj_matrix[a][b] = 1                                # a에서 b로 가는 길이 있음을 표시
        adj_matrix[b][a] = 1                                # 무방향이므로 b에서 a로 가는 길이 있음을 표시
    S, G = map(int, input().split())                        # 출발 노드와 도착 노드를 입력받음
    print(is_can_go(adj_matrix))                            # 함수 실행 및 출력
'''

def is_can_go(adj_matrix):                                  # 출발지에서 도착지까지 이동가능여부 확인
    Q = [S]                                                 # 큐를 생성하고 S를 담아둠
    visited = [0]*(V+1)                                     # 각 노드별 도착 여부를 확인할 visited 변수
    time_num = 1                                            # 노드를 몇개나 들렸는지 확인하는 변수
    while Q:                                                # Q에 값이 있을 때
        for i in range(1, V+1):                             # 1~ V까지 반복하면서
            if visited[i] == 0 and adj_matrix[Q[0]][i] == 1:# 해당 노드에 방문하지 않았으면서, 간선이 있다면
                Q.append(i)                                 # 큐에 추가하기
                visited[i] = time_num                       # visited[i]에 노드 방문갯수를 입력
                if i == G:                                  # 만약 i가 도착 노드라면
                    return f'#{testcase} {time_num-1}'      # 출력값을 출력하되 time_num-1의 이유는 출발 노드는 경유 노드가 아니기 때문
        time_num += 1                                       # for문이 끝나면 time_num에 1을 더하기
        Q.pop(0)                                            # 제일 앞의 데이터를 빼냄
    return f'#{testcase} 0'

T = int(input())
for testcase in range(1, T+1):
    # 입력값 받기
    V, E = map(int, input().split())                        # 노드갯수 V, 간선갯수 E 입력받음
    adj_matrix = [[0]*(V+1) for _ in range(V+1)]            # 인접행렬 만들기. 노드가 1부터 시작하므로 V+1로 만들어줌
    for _ in range(E):                                      # 각 간선을 입력받기 위한 반복문
        a, b = map(int, input().split())                    # 각 노드별 이어주는 간선을 입력받음
        adj_matrix[a][b] = 1                                # a에서 b로 가는 길이 있음을 표시
        adj_matrix[b][a] = 1                                # 무방향이므로 b에서 a로 가는 길이 있음을 표시
    S, G = map(int, input().split())                        # 출발 노드와 도착 노드를 입력받음
    print(is_can_go(adj_matrix))                            # 함수 실행 및 출력


T= int(input())
for testcase in range(1, T+1):
    V, E = map(int,input().split())
    data = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())                            # 출발노드 S와 목적지 노드 G를 받음
    adj_matrix = [[0]*(V+1) for _ in range(V+1)]                # 인접행렬 작성
    visited = [0] * (V+1)                                       # 노드를 방문했느지 확인하는 변수

    for i in range(E):                                          # i를 인자로 간선의 갯수만큼 반복
        adj_matrix[data[i][0]][data[i][1]] = 1                  # 인접행렬에 1을 기입 (a,b) = 1 의 형태
        adj_matrix[data[i][1]][data[i][0]] = 1                  # 인접행렬에 1을 기입 (b,a) = 1 이 되는 형태

    Q =[S]                                                      # Q에 S기입
    visited[S] = 1                                              # start 노드는 방문을 했으니 1로 기입

    while Q:                                                    # Q가 있을때만 실시
        c = Q.pop(0)                                            # 현재 노드를 Q.pop(0)으로 선정

        for i in range(V+1):                                    # i를 인자로 반복
            if adj_matrix[c][i] and not visited[i]:             # 현재값이 i 값으로 가는 경로가 있는지 확인하고, 방문도 안했다면,
                Q.append(i)                                     # Q에 i값을 추가
                visited[i] = visited[c] + 1                     # 해당 노드에 거치는 노드 수 기입
    
    if not visited[G]:                                          # visited[G]가 0이면 답은 0
        ans = 0
    else:                                                       # 그게 아니면 출력값 출력
        ans = visited[G]-1

    print(f'#{testcase} {ans}')