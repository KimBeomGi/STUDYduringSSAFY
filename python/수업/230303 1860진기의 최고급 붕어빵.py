T = int(input())
for testcase in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = 'Possible'
    for t in sorted(lst):
        cnt += 1
        if cnt > (t//M)*K:      # 도착한 사람수 > 만들어 놓은 수
            ans = 'Impossible'
            break
    print(f'#{testcase} {ans}')