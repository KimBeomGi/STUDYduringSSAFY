import sys
sys.stdin = open('230216 5일차-배열최소합.txt', 'r')

T = int(input())                                        # 반복횟수 입력
for testcase in range(1,T+1):
    N = int(input())                                    # 행렬의 각 행과 열의 길이N을 입력받음
    selected = [-1]*N                                   # selected 즉, 어떤 값을 사용하고 있는지에 대한 변수(위치를 표시)
    used = [0]*N                                        # 각 행에서 어떤 열을 사용했는지를 표시해주기 위한 used 변수
    matrix = [list(map(int,input().split())) for _ in range(N)] # 입력값을 입력받음
    min_sum = 10*N*N                                    # 주어진 행렬에서 만들어질 수 없는 값을 min_sum으로 할당

    def solve(idx, sum_v):                              # idx(행), sum_v(순열의 합)를 매개변수로 한 solve 함수 생성
        global min_sum                                  # min_sum을 global에서 불러와서 사용해야하므로.
        if sum_v > min_sum:                             # sum_v > min_sum이면 더 탐색할 필요가 없으니까 보냄
            return                                      # 안돼. 돌아가. 바꿔줄 맘 없어.
        
        if idx == N:                                    # idx 즉, 행이 맨 마지막이라면
            if min_sum > sum_v:                         # 지금까지 최소합값이랑 현재 구한합값을 비교해서 최소합값이 크다면
                min_sum = sum_v                         # 최소합값을 현재 구한합값으로 변경
            return                                      # 그리고 자신을 호출한 곳으로 다시 복귀
        
        for i in range(N):                              # for문의 i인자를 이용해 0~(N-1)만큼 각 행의 열을 확인한다.
            if used[i] == 0:                            # 해당 열이 사용되지 않았다면
                selected[idx] = i                       # selected에서 각 인덱스는 행을 의미하며 selected[idx]에 표시함으로서
                                                        # 그 행에 어느 열을 선택했는지를 표현해줌
                used[i] = 1                             # used[i] = 1로 바꿈으로서 열이 사용했음을 표시.
                solve(idx+1, sum_v + matrix[idx][i])    # 재귀함수로 solve함수를 호출하는데 이때 다음행을 호출하기 위해 (idx+1),
                                                        # sum_v를 구하기위해 sum_v + matrix[idx][i]를 매개변수로 넣은채로 진행한다.
                used[i] = 0                             # 해당 열은 해당행에서 사용했으므로 다른 행에서 재사용하기 위해서 used[i] = 0을 표시
                # used[i] = 1을 사용하고 used[i] = 0이 가능한 이유는 현재 i는 for문을 돌고 있기 때문에
                # 추가로 만약 다음행으로 더 갈 수 있다면 재귀호출로 solve함수를 진행해서 used[i] = 0으로 바로 가지 않는다.
                # 게다가 같은행이라도 다시 그 열을 갈 일이 없기 때문
    solve(0,0)                                          # solve함수에 idx=0,sum_v=0을 할당해서 시작해준다.
    print(f'#{testcase} {min_sum}')                     # 출력값 출력