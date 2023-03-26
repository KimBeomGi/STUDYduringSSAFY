# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    # [1] N 번 반복하면서 노선입력, 빈도수 표기
    cnts = [0]*5001
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E+1):
            cnts[i] += 1
    
    P = int(input())
    alist = []
    for _ in range(P):
        p = int(input())
        alist.append(cnts[p])
    
    print(f'#{testcase}', *alist)