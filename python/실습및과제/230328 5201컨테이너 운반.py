# [문제]
# 화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
# 트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.
# 이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.
# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고, 다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.
# 1<=N, M<=100, 1<=wi, ti<=50
 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('230328 5201컨테이너 운반.txt','r')

# [문제풀이]
# 0. N개의 컨테이너, M 대의 트럭, A도시, B도시
# 0-1. 1트럭 1컨테이너, 적재용량 초과면 컨테이너 운반X
# 0-2. A to B로 최대 M대의 트럭 편도 1번 운행
# 0-3. 싣지 못한 트럭이 있을수도 있지만 상관 ㄴㄴ 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력
# 1. 탐욕으로 풀자.

# def sum_weight(truck,container):                    # truck 번호, container 번호
#     global overall_weight                           # global 변수 사용
#     if truck == M or container == N:                # truck의 갯수가 다차거나 container번호가 다 차면
#         return                                      # 돌아가
#     for i in range(truck, M):                       # 트럭의 댓수만큼 반복
#         for j in range(container, N):               # 컨테이너의 갯수만큼 반복
#             if truck_load[i] >= box_weight[j]:      # 트럭의 적재용량이 컨테이너 무게보다 크다면
#                 overall_weight += box_weight[j]     # overall_weight에 추가
#                 truck = (i+1)                       # truck 다음번호 확인
#                 container = (j+1)                   # container 다음번호 확인
#                 sum_weight(truck,container)         # 다시 함수 사용
#                 return                              # 돌아가

# T = int(input())
# for testcase in range(1, T+1):
#     N, M = map(int, input().split())                                        # 컨테이너 갯수N, 트럭 댓수M
#     box_weight = sorted(list(map(int, input().split())), reverse=True)      # 각 컨테이너의 무게, 내림차순
#     truck_load = sorted(list(map(int, input().split())), reverse=True)      # 각 트럭 적재 가능 무게, 내림차순
#     overall_weight = 0                              # 답을 내기 위한 overall_weight
#     sum_weight(0, 0)                                # 함수사용
#     print(f'#{testcase} {overall_weight}')          # 출력값 출력


######
# 이거 왜 안됨?
def sum_weight(truck,container, overall_weight):    # truck 번호, container 번호
    # global overall_weight                         # global 변수 사용
    if truck == M or container == N:                # truck의 갯수가 다차거나 container번호가 다 차면
        k= overall_weight
        return k                                    # 돌아가
    for i in range(truck, M):                       # 트럭의 댓수만큼 반복
        for j in range(container, N):               # 컨테이너의 갯수만큼 반복
            if truck_load[i] >= box_weight[j]:      # 트럭의 적재용량이 컨테이너 무게보다 크다면
                overall_weight += box_weight[j]     # overall_weight에 추가
                truck = (i+1)                       # truck 다음번호 확인
                container = (j+1)                   # container 다음번호 확인
                k = sum_weight(truck,container, overall_weight)         # 다시 함수 사용
                return k                            # 돌아가
            elif i==(M-1) and j==(N-1):
                if truck_load[i] < box_weight[j]:
                    return k
    return 0
T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())                                        # 컨테이너 갯수N, 트럭 댓수M
    box_weight = sorted(list(map(int, input().split())), reverse=True)      # 각 컨테이너의 무게, 내림차순
    truck_load = sorted(list(map(int, input().split())), reverse=True)      # 각 트럭 적재 가능 무게, 내림차순
    # overall_weight = 0                            # 답을 내기 위한 overall_weight
    answer = sum_weight(0, 0, 0)                    # 함수사용
    print(f'#{testcase} {answer}')                  # 출력값 출력

# 아래게 안되는거여
# 1
# 3 5
# 20 20 15
# 20 10 10 5 1

# 출력값은 20

# 5
# 3 2
# 1 5 3
# 8 3
# 5 10
# 2 12 13 11 18
# 17 4 7 20 3 9 7 9 20 5
# 10 12
# 10 13 14 6 19 11 5 20 11 14
# 5 18 17 8 9 17 18 4 1 16 15 13
# 3 5
# 20 20 15
# 20 10 10 5 1
# 2 2
# 30 27
# 1 2


# #1 8
# #2 45
# #3 84
# #4 20
# #5 0