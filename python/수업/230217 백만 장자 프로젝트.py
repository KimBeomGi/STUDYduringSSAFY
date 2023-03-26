T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    i = ans = 0
    while i < N:
        # [1] i~ 끝까지 최대값의 index찾ㄱ기
        i_mx = i
        for j in range(i+1, N):
            if lst[i_mx] < lst[j]:
                i_mx = j
        
        # [2] i~i_m 까지의 최대값과 차이 누적
        for j in range(i, i_mx):
            ans += lst[i_mx]-lst[j]
        
        i = i_mx + 1

    print(f'#{testcase} {ans}')


# 개선 

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    ans = mx = 0
    for n in lst:
        if mx>n:
            ans += mx-n
        else:
            mx = n
    print(f'#{testcase} {ans}')
        



    i = ans = 0
    while i < N:
        # [1] i~ 끝까지 최대값의 index찾ㄱ기
        i_mx = i
        for j in range(i+1, N):
            if lst[i_mx] < lst[j]:
                i_mx = j
        
        # [2] i~i_m 까지의 최대값과 차이 누적
        for j in range(i, i_mx):
            ans += lst[i_mx]-lst[j]
        
        i = i_mx + 1

    print(f'#{testcase} {ans}')