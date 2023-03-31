import sys
sys.stdin = open('2230330 동철이의 일 분배.txt', 'r')

# idx : 업무를 수행할 직원의 번호
def solve(idx, rate):
    global max_v
    if rate <= max_v:
        return
    if idx == N:
        # print(rate)
        # 모든 직원이 업무를 결정했으면
        # 확률 계산하기...
        max_v = max(max_v, rate)
        return

    for i in range(N):  # 모든 업무를 수행해 보긴
        # i번째 업무 수행
        if not check[i]:        # 다른 직원이 i번째 업무를 수행하지 않았으면 수행
            check[i] = 1
            solve(idx+1, rate * data[idx][i])
            check[i] = 0


T =int(input())
for testcase in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            data[i][j] /= 100
    
    check = [0]*N       # 다른직원이 해당 업무를 이미 수행했는지 확인
    # for row in data:
    #     print(row)
    max_v = 0
    solve(0,1)          # 곱하기 연산에 영향을 주지 않는 값은 1이라서 초기값을 1로 준다.
    print(f'#{testcase} {max_v*100:.6f}')       # 실수 출력할건데 6자리까지 출력해라. :6f