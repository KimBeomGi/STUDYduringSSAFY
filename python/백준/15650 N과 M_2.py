# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 입력값
# 3 1

# 출력값
# 1
# 2
# 3

# 입력값 
# 4 2

# 출력값
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4

# 입력값
# 4 4

# 출력값
# 1 2 3 4

# def find(N,M,result):
#     if len(result) == M:
#         temp = ' '.join(map(str, result))
#         if sorted(temp) not in val:
#             val.append(temp)
#         return
    
#     for i in range(1,N+1):
#         if not visited[i]:
#             visited[i]=True
#             result.append(i)
#             find(N,M,result)
#             visited[i]=False
#             result.pop()
#     return

# N,M = map(int,input().split())
# result = []
# visited = [False]*(N+1)
# val = []
# find(N,M,result)
# for a in val:
#     print(a)



N, M = map(int, input().split()) # N과 M을 입력받음
arr = []                        # 수열을 저장할 리스트

def dfs(k):                     # 깊이 우선 탐색 함수
    if len(arr) == M:           # 수열의 길이가 M이면
        print(*arr)             # 수열 출력
        return                  # 함수 종료
    for i in range(k, N+1):     # k부터 N까지 반복
        if i not in arr:        # i가 수열에 없으면
            arr.append(i)       # 수열에 i 추가
            dfs(i+1)            # 다음 탐색을 위해 재귀 호출
            arr.pop()           # 수열에서 i 제거

dfs(1)                          # 처음 탐색 시작
