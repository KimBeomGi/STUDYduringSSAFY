import sys
sys.stdin = open('2230330 5208 전기버스2.txt','r')


# [문제]
# 충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
# 충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
# 정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.
# 다음은 1번에서 출발 5번이 종점인 경우의 예이다.

# 정류장 1 2 3 4 5
# 충전지 2 3 1 1

# 1번에서 장착한 충전지 용량이 2이므로, 3번 정류장까지 운행할 수 있다. 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.
# 마지막 정류장에는 배터리가 없다.

# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다

# [문제풀이]
# 0. 배터리를 교환하면서 운행하는 전기버스이다.정류장에는 각 배터리가 있지만 꼭 교체할 필요는 없음.
# 0-1. 우리는 최소한의 교체 횟수로 목적지에 도착하도록 해야한다.
# 1. 입력은 한 줄에 다 받아지면
# 1-1. 정류장 수 N이 먼저 입력된 후 그 이후로 1번부터 N-1번 정류장까지 N-1개의 정류장 별 배터리 용량이 주어진다.
# 2. 음... 한번 재귀로 풀어볼까. 함수 안에서 교체하는 경우와 교체안하는 경우로 나눠서 다시 함수로 들어가도록 하게.


def iscan(stop, battery, change):
    global min_change                           # global로 가져오기
    if stop == N-1 and battery >= 0:            # 종점에 도착했으면
        # print('#',went)
        if min_change > change:                 # min_change가 change보다 크다면
            min_change = change                 # min_change값 교체
        return                                  # 돌아가

    elif battery >= 0 and not went[stop]:       # battery도 0보다 큰 상태고 방문하지도 않았다면
        went[stop] = 1                          # went[stop]을 방문했음으로 표시
        if battery > 0:                         # 배터리가 0이상일 때만
            iscan(stop+1, battery-1, change)    # 배터리 교체 안하기
        if min_change >= change+1:              # 현재 배터리 교체 최솟값이 현재 배터리 교체값보다 크거나 같을 때만
            iscan(stop+1, each_batteries[stop]-1, change+1)   # 배터리 교체 하기
        went[stop] = 0                          # went[stop]을 방문했음 표시 지우기
    else: 
        return


T = int(input())
for testcase in range(1, T+1):
    N, *each_batteries = map(int, input().split())           # N과 버스정류장별 배터리를 각각 숫자, 리스트로 입력받음
    went = [0]*N                                # 각 정류장별 거쳤는지 확인하는 리스트
    min_change = N+1                            # min_change를 N+1로 우선 초기화
    init_battery = each_batteries[0]            # 최초 배터리 기입
    iscan(0, init_battery, 0)                   # 함수에 넣기
    print(f'#{testcase} {min_change}')