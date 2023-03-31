def dfs(n, sm):
    global ans
    # 최솟값 구할 때 항상 성공하는 가지치기?!
    # if ans <= sm-B:       # 이 가지치기 말고 또 다른거?
    #     return
    if ans== 0: # 이미 만점!        # 이건 극단적 가지치기!
        return

    if n == N:
        if sm >= B:
            ans = min(ans, sm-B)
        return
    
    dfs(n+1, sm+lst[n])     # 포함
    dfs(n+1, sm)            # 미포함


T  = int(input())
for testcase in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    
    ans = N*10000
    dfs(0,0)

    print(f'#{testcase} {ans}')