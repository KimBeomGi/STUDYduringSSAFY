import sys
sys.stdin = open('230327 5189 전자카트.txt')
# 중간 경로 만들기 : 순열만들기

def perm(idx):
    global min_v
    if idx == N-1:
        # print(arr)
        path = [0] + arr + [0]
        sum_v = 0
        for i in range(len(path)-1):
            sum_v += data[path[i]][path[i+1]]
        if sum_v < min_v:
            min_v = sum_v
        return
    for i in range(idx, N-1):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    min_v = 0xffffffff
    # print(f'#{testcase} {min_v}')
    arr = [x for x in range(1,N)]
    perm(0)
    print(f'#{testcase} {min_v}')