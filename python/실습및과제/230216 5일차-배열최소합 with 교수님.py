# 배열최소합
# 순열 
import sys
sys.stdin = open('230216 5일차-배열최소합.txt', 'r')

T = int(input())
for testcase in range(1, T+1):


    N = int(input())
    # idx 행의 몇 번째 열을 선택할 건지 결정
    selected = [0]*N
    used = [0] * N

    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10*N*N

    def solve(idx, sum_v):
        global min_sum
        # 가능성이 없는 경우의 수는 수행하지 않음: 가지치기
        # 이미 구한 최솟갑 보다 중간 합이 더 크거나 같음.
        if sum_v >= min_sum:                        # 내가 구해논 min_sum보다 크거나 같아버리면
            return                                  # 안돼, 돌아가 바꿔줄 생각 없어!

        if idx == N:
            # # 모든 행을 다 결정한 거니까
            # # print(selected)
            # sum_v = 0
            # for i in range(N):
            #     # selected[i] # i 행에서 선택한 열
            #     sum_v += arr[i][selected[i]]
            if min_sum > sum_v:
                min_sum = sum_v
            # print(selected, sum_v)

            return                                  # 여기서 return은 solve(N)을 끝내는 것임
        # 내가 할 수 있는 모든 경우의 수 수행해보기
        for i in range(N):   # i가 열의 번호, 모든 열을 선택
            if not used[i]:                         # 사용 안했으면 사용가능, 사용하고 있으면 사용 ㄴㄴ
                selected[idx] = i
                used[i] = 1                         # used[i]를 볼거임
                solve(idx+1, sum_v + arr[idx][i])   # 다음행 보러 갈거임 재귀함수 시작
                used[i] = 0
    
    # 더한게 없으니 중간합 0
    solve(0, 0)
    print(f'#{testcase} {min_sum}')