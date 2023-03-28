import sys
sys.stdin = open('230327 5189 전자카트.txt')

# 가능한 경로를 만들어 나가는 함수를 작성
# N-1개 노드에 대한 순서를 만들어주면 됩니다.
# path 경로를 저장하는 변수
# 경로를 구하고, 경로를 보면서 비용계산
# 경로 구하기
# 0번에서 시작해서 0번으로 돌아와야 한다.
def solve(idx, path):
    global min_v
    if idx == N-1: #모든 노드에 대한 순서를 정의한 상태
        # 마지막에 1번 노드 붙여서 경로 완성하면 됩니다.
        path.append(0)              # 마지막 관리소로 돌아오는 노드 추가
        # print(path)                 # 경로가 제대로 만들어졌는지 확인
        # 각 경로마다 비용 계산
        sum_v = 0
        for i in range(len(path)-1):
            sum_v += data[path[i]][path[i+1]]
        # 최소 비용확인
        if min_v > sum_v:
            min_v = sum_v
        path.pop()
        return
    # 경로로 넣을 수 있는 모든 노드를 path에 추가해보기
    for i in range(1, N):           # 0번은 시작점이니까
        if not check[i]:
            path.append(i)
            check[i] = 1
            solve(idx+1, path)
            check[i] = 0
            path.pop()              # 경로에 i번 노드 추가했다가 제거해주기

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    path = [0] #+ 모든 경로를 다 넣을 것이고 마지막에 # +[0]
    check = [0]*N  # 각 노드가 경로에 추가되었는지 표시하는 리스트
    min_v = 0xffffffff
    A = solve(0,path)
    print(f'#{testcase} {min_v}')


#################################
# 그냥 함 해보는 것
# N =4
# arr = [1,2,3,4]
# perm_arr = [0]*N
# used = [0]*N

# # idx번째 들어갈 요소 선택하기
# def perm(idx):
#     if idx == N:
#         print(perm_arr)
#         return
#     for i in range(N):
#         if not used[i]:
#             used[i] = 1
#             perm_arr[idx] = arr[i]
#             perm(idx+1)
#             used[i] = 0

# # idx 번째 요소랑 idx보다 뒤에 있는 요소랑 자리 바꾸기
# # 를 이용해서 순열 구하기
# def perm2(idx):
#     if idx == N:
#         print(perm_arr)
#         return
#     for i in range(idx, N):
#         arr[i], arr[idx] = arr[idx], arr[i]
#         perm2(idx+1)
#         arr[i], arr[idx] = arr[idx], arr[i]

# perm2(0)