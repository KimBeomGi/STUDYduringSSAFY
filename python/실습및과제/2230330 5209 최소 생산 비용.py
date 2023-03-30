import sys
sys.stdin = open('2230330 5209 최소 생산 비용.txt','r')

# [문제]
# A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.
# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

#     A   B   C
# 1  73  21  21
# 2  11  59  40
# 3  24  31  83

# 예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다..
# 이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.

# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 제품 수 N이 주어지고, 이후 제품당 한 줄 씩 N개의 줄에 걸쳐 공장별 생산비용 Vij가 주어진다. 3<=N<=15,   1<=Vij<=99
 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# [문제풀이]
# 0. A사에서 N종의 제품을 N곳의 공장에서 공장당 1가지씩 생산한다.
# 0-1. 공장별 생산비용을 보고 최소 생산 비용을 계산해야한다.
# 1. 순열을 이용해볼까?

########################
# 우선 기본 틀 만들어놓음
# def min_cost_production(row):
#     if all(actived):                    # 공장이 모두 가동중이라면
#         print(cost)
#         return
#     for column in range(N):
#         if not actived[column]:         # 현재 미가동된 공장이라면
#             actived[column] = 1         # 가동 시켜주고,
#             cost[column] = factories[row][column]
#             min_cost_production(row+1)  # 다음 제품을 생산할 공장을 물색해보자.
#             actived[column] = 0         # 이제 다른 공장에서 가동시키기 위해 공장 가동 중단하기.
        
# T = int(input())
# for testcase in range(1,T+1):
#     N = int(input())
#     factories = [list(map(int, input().split())) for _ in range(N)]     # 공장별 생산단가 행렬
#     actived = [0]*N                     # 공장 가동여부를 확인하는 리스트
#     cost = [0]*N
#     min_cost_production(0)

##########################

def min_cost_production(row, cost):
    global min_cost
    if all(actived):                    # 공장이 모두 가동중이라면
        if min_cost > cost:             # 최소 생산비용과 현 생산비용을 비교해서 최소 생산비용이 더크면
            min_cost = cost             # 최소 생산비용을 현 생산비용으로 교체
        return
    for column in range(N):
        # 현재 미가동된 공장이고, 이번 공장에서 생산비용을 추가한게 현재 최소 생산비용보다 크지 않을때만 진행
        if not actived[column] and min_cost >= cost+factories[row][column]:
            actived[column] = 1         # 가동 시켜주고,
            # 다음 제품을 생산할 공장을 물색해보자. 이 때 비용은 추가하고 찾으러 가야지
            min_cost_production(row+1, cost+factories[row][column])
            actived[column] = 0         # 이제 다른 공장에서 가동시키기 위해 공장 가동 중단하기.
        
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    factories = [list(map(int, input().split())) for _ in range(N)]     # 공장별 생산단가 행렬
    actived = [0]*N                     # 공장 가동여부를 확인하는 리스트
    min_cost = 99*N*N                   # 가장 큰 비용을 우선 min_cost로 기입
    min_cost_production(0, 0)           # 함수진행
    print(f'#{testcase} {min_cost}')