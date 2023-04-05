T = int(input())
for testcase in range(1, T+1):
    R, P = map(str, input().split())
    R = int(R)
    for i in range(len(P)):
        print(P[i]*R, end = '')
    print()