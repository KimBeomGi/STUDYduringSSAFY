
T= int(input())
for testcase in range(1,T+1):
    N =int(input())
    cnts = [0]*200
    for _ in range(N):
        s, e = map(int, input().split())
        for i in range((s-1)//2, (e-1)//2+1):
            cnts[i] +=1
    ans = max(cnts)
    print(f'#{testcase} {ans}')


T= int(input())
for testcase in range(1,T+1):
    N =int(input())
    cnts = [0]*200
    for _ in range(N):
        s, e = map(int, input().split())
        if s>e:                                 # start가 end보다 크다면?!
            s, e = e, s                         # 자리바꾸고 실시
        for i in range((s-1)//2, (e-1)//2+1):
            cnts[i] +=1
    ans = max(cnts)
    print(f'#{testcase} {ans}')