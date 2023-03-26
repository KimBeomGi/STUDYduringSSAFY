import sys
sys.stdin = open('파이썬 sw문제해결 기본-stack2 7차시 5일차-배열 최소 합.txt', 'r')










def per_sum(idx, sum_value):
    global min_sum
    if sum_value >= min_sum:
        return
    
    if idx == N:
        if min_sum > sum_value:
            min_sum = sum_value
            return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            per_sum(idx+1, sum_value + matrix[idx][i])
            visited[i] = 0

T= int(input())
for testcase in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 10*N*N                                # 최소합을 넣을 min_sum 변수 생성
    visited = [0]*N                                 # 행마다 들어간 열이 무엇인지 확인하기 위함



    per_sum(0,0)
    print(f'#{testcase} {min_sum}')