# 완전탐색: 현 상황에서 내가 할 수 있는 모든 경우의 수를 다 고려해보기
# 현재위치를 저장하는 변수
# sum_v : 이동하는 중에 계산한 경로합
# 오른쪽, 아래쪽 이동하는 경우의 수 모두 수행해보기
# 더이상 수행하지 않아도 되는 경우의 수
# 1. 영역을 벗어나거나, 여태까지 이동하면서 그머고 계산한 경로의 합이
# 2. 여태까지 이동하면서 계산한 경로의 합이 내가 알고 있는 정답보다 클 때
# 마지막 위치에 도착했을 때 최솟값이면 저장
import sys
sys.stdin = open('230327 5188 최소합.txt','r')

# #############################
# def solve(r,c, sum_v):
#     global min_v
#     if sum_v >= min_v:
#         return
#     if r < 0 or r >=N or c < 0 or c >=N:
#         return
#     sum_v += data[r][c]
#     if (r,c) == (N-1, N-1):
#         # 목적지 도착 : 결과 계산
#         if sum_v < min_v:
#             min_v = sum_v
#         return
    
#     # 목적지에 도착하지 못했으니..할 수 있는 거 다해보기
#     # 오른쪽으로 가거나 아래쪽으로 가기
#     solve(r, c+1, sum_v)     # 오른쪽으로 가기
#     solve(r+1, c, sum_v)     # 아래쪽으로 가기

# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     min_v = 1000
#     solve(0,0,0)
#     print(f'#{testcase} {min_v}')

# #############################
# 이건 global 안쓰고 하는 방법

def solve(r,c, sum_v):
    # global min_v
    # if sum_v >= min_v:
    #     return
    if r < 0 or r >=N or c < 0 or c >=N:
        return 0xffffffff
    sum_v += data[r][c]
    if (r,c) == (N-1, N-1):
        # 목적지 도착 : 결과 계산
        # if sum_v < min_v:
        #     min_v = sum_v
        return sum_v
    
    # 목적지에 도착하지 못했으니..할 수 있는 거 다해보기
    # 오른쪽으로 가거나 아래쪽으로 가기
    result1 = solve(r, c+1, sum_v)     # 오른쪽으로 가기
    result2 = solve(r+1, c, sum_v)     # 아래쪽으로 가기
    return min(result1, result2)

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # min_v = 1000
    # solve(0,0,0)
    # 경로 합의 최솟값을 반환하는 함수
    result = solve(0,0,0)
    print(f'#{testcase} {result}')
###########################################