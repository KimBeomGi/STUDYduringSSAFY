import sys
sys.stdin = open('230216 5일차-배열최소합.txt', 'r')

T = int(input())
for testcase in range(1, T+1):
    N = int(input())                                    # 행렬의 각 길이 N을 입력받음
    selected = [0]*N                                    # 순열을 만들기 위해 어떤 값이 선택되었는지를 표시하기 위해, selected 변수 생성
    used = [0]*N                                        # 순열 생성 함수에서, 어떠한 열이 사용되었는지 확인할 수 있게 하기 위한 변수 생성

    arr = [list(map(int,input().split())) for _ in range(N)]        # 입력값을 입력받으며, 행렬을 받음
    min_sum = 10*N*N

    def solve(idx, sum_v):                              # solve함수를 만들어서 순열의 합 중 최솟값을 받아냄. idx는 행렬의 행을, sum_v는 현재 구하고 있는 합
        global min_sum                                  # local로 사용되지 않고 global로 사용되는 min_sum이기 때문에 global을 사용
        if sum_v >= min_sum:                            # 현재 구하고 있는 순열의 합이 현재의 min_sum보다 크면
            return                                      # 더 할 필요없으니 반환.(탐색 종료)
        
        if idx == N:                                    # idx가 즉, 행이 마지막 행이면
            if min_sum > sum_v:                         # min_sum(지금까지 구했던 합 중 가장 작은합)보이 현재 구한 순열 합 보다 클 때
                min_sum = sum_v                         # min_sum에 sum_v를 대입한다.
            return                                      # return해서 이전의 행에서 다시 출발해 이번 행에서 
        
        for i in range(N):                              # i를 인자로해서 각 행의 열을 확인하는 반복문
            if not used[i]:                             # 사용된 열이 아니라면
                selected[idx] = i                       # selected의 idx 부분에 i값을 넣어라. 그러니까 0행에 1번열이 들어가면 [1,0,0,0]으로 바꿔라.
                used[i] = 1                             # used[i]값에 1을 기입함으로 i번째 열이 이전에 사용되었음을 표시한다.
                solve(idx+1, sum_v + arr[idx][i])       # 재귀함수로서 solve 함수로 들어가는데 다음행으로 넘어가면서, sum_v도 이번 [행][열]의 값을 더해준채 들어간다.
                used[i] = 0                             # 함수를 한번 진행했으니 used[i]를 0으로 만들어줘야 다음행에서 사용이 가능하기 때문
    
    solve(0, 0)
    print(f'#{testcase} {min_sum}')
    
