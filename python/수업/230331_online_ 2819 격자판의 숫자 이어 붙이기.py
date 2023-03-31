def dfs(n, tst, ci, cj):
    if n==7:
        sset.add(tst)       # 중복제건
        return
    
    for di, dj in((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = ci+di, cj+dj
        if 0<=ni<4 and 0<= nj <4:
            dfs(n+1, tst*10+arr[ni][nj], ni, nj)


T = int(input())
for testcase in range(1, T+1):
    # 문자열보다는 정수로 만드는 것이 빠르게 처리
    arr = [list(map(int, input().split())) for _ in range(4)]
    sset = set()
    
    for i in range(4):
        for j in range(4):
            dfs(1, arr[i][j], i, j)


    ans = len(sset)
    print(f'#{testcase} {ans}')