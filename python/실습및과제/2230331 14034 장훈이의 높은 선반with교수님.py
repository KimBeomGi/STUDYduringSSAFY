import sys
sys.stdin=open('2230331 14034 장훈이의 높은 선반.txt','r')


# idx 번째 점원을 탑의 부품으로 쓰냐? 결정하기
def solve(idx, sum_v):
    global min_v
    if sum_v >= min_v:
        return
    if idx == N:
        if sum_v >= B:
            # print(sum_v)
            min_v = min(min_v, sum_v)
        return
    solve(idx+1, sum_v + data[idx])
    solve(idx+1, sum_v)

T= int(input())
for testcase in range(1, T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    min_v = 10000*N
    solve(0,0)
    print(f'#{testcase} {min_v-B}')