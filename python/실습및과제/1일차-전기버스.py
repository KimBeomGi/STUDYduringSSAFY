# [문제]
# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
# [예시]
# ↓ 표로 충전기와 충전회수에 관련한 내용이 적혀있음 파이썬 문서로는 안보임
# 정류장
# 충전기
# 충전회수

# 다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

# [입력]
# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

# [출력]

# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

# [입력]
# 3
# 3 10 5
# 1 3 5 7 9
# 3 10 5
# 1 3 7 8 9
# 5 20 5
# 4 7 9 14 17

# [출력]
#1 3
#2 0
#3 4

# [문제풀이]
# 1. 0번에서 출발해서 종점인 N번 정류장이라 했으므로 총 N+1개의 정류장이 있다.
# 1-1. 최대 이동가능 정류장이 K이므로 충전소 정류장 + K까지만 도착가능하다.
# 2. 충전기가 설치된 정류장 개수 M개. 몇 번 정류장에 설치되어있는지를 입력해줌.
# 2-1. 충전기 위치를 숫자로 표기해 리스트에 [1,3,7,8]과 같은 형식으로 만들어 저장해주자.
# 2-2. 그러면 M은 해당 리스트의 len(충전기위치)가 된다.
# 3. 충전기 설치가 잘못되어 종점에 도착할 수 없으면 0을 했으므로
# 3-1  충전소 위치 > 출발지점+k 또는 다음 충전소 위치 > 현 충전소 위치 + k 이면 0을 출력하면 된다.
# 4. 충전횟수를 출력해야하므로 충전횟수 변수(charge_nums)를 새로할당 한다.
# 5. 충전은 버스+k 안에 있으면 충전 해야함. 그런데 만약 버스+k 안에 2개가 있다면 뒤의 것을 충전하도록 한다.


'''
# K = 최대 이동가능정류장
# M = 충전기가 설치된 정류장 개수
# N = 버스 정류장 갯수
T = int(input())                                                    # testcase 횟수 T
for testcase in range(1, T+1):                                      # testcase를 인자로하는 1~T회 반복 실행
    K, N, M = map(int, input().split())                             # K,N,M을 따로 받아야 하므로 map(int, input().split())으로 받아줌
    charge_stops = list(map(int, input().split()))                   # 충전소의 위치를 리스트로 받아 넣어준다.

    pullcharge = K
    bus_battery = K
    bus = 0                                                         # bus의 위치
    charge_nums = 0                                                 # 충전횟수를 계산하기 위한 charge_nums 변수 할당

    for stop in range(N+1):                                         # 정류장 stop을 요소로 0번에서 N번까지 정류장을 간다.
        if bus_battery == 0 or bus_battery < K:                     # 버스 배터리가 0이거나 완전충전상태보다 작다면
            if bus in charge_stops:                                  # 버스가 충전소에 있다면
                bus_battery = pullcharge                            # bus_battery를 k만큼 최대충전함
                charge_nums += 1                                    # 충전횟수를 1만큼 추가한다.
            elif bus_battery == 0 and bus not in charge_stops:       # 버스 배터리는 0인데 버스가 충전소에 없다면  
                break                                               # 버스 운행 중단
        bus += 1                                                    # 버스가 한 정류장을 지나면 다음 정류장이니
        bus_battery -= 1                                            # 정류소 지날대마다 배터리가 줄어듬
    
    if bus_battery == 0 and bus != N:                               # 충전기 설치 잘못으로 버스가 운행중단한 상황이면
        print(f'#{testcase} 0')                                     # 0을 출력
    else:                                                           # 잘 작동했으면
        print(f'#{testcase} {charge_nums}')                         # 출력값대로 출력
'''
# 수정할 것
# 충전소를 매번 들리지 말자!
# 매 충전소 마다 안들리자
# 1. 충전소의 위치 확인, 버스의 위치 확인, 버스가 갈 수 있는 위치 확인
# 2. 버스가 갈 수 있는 위치 안의 충전소 위치 확인 결과 2개 이상이면 숫자가 더 큰 충전소에서 충전.
# 3. bus < charge_stop 리스트 안의 숫자 중 <= bus+bus_battery 에서 해당하는 charge_stop 숫자 중 큰 곳 에서 버스 충전하기


# K = 최대 이동가능정류장
# M = 충전기가 설치된 정류장 개수
# N = 버스 정류장 갯수
T = int(input())                                                    # testcase 횟수 T
for testcase in range(1, T+1):                                      # testcase를 인자로하는 1~T회 반복 실행
    K, N, M = map(int, input().split())                             # K,N,M을 따로 받아야 하므로 map(int, input().split())으로 받아줌
    charge_stops = list(map(int, input().split()))                   # 충전소의 위치를 리스트로 받아 넣어준다.

    pullcharge = K                                                  # 완전충전상태
    bus_battery = K                                                 # 현재 버스 배터리
    bus = 0                                                         # bus의 위치
    charge_nums = 0                                                 # 충전횟수를 계산하기 위한 charge_nums 변수 할당

    for stop in range(N+1):                                         # 정류장 stop을 요소로 0번에서 N번까지 정류장을 간다.
        if bus_battery == 0:                                        # 버스 배터리가 0이거나 완전충전상태보다 작다면
            if bus in charge_stops:                                 # 버스가 충전소에 있다면
                bus_battery = pullcharge                            # bus_battery를 k만큼 최대충전함
                charge_nums += 1                                    # 충전횟수를 1만큼 추가한다.
            elif bus_battery == 0 and bus not in charge_stops:      # 버스 배터리는 0인데 버스가 충전소에 없다면  
                break                                               # 버스 운행 중단
        
        elif bus_battery < K:                                       # 버스 배터리가 최대 충전이 아니라면
            is_charge = [0]                                         # 충전어디서 할건지 정하기 위한 변수
            if (bus + bus_battery) >= N:                            # 버스가 충분히 종점까지 갈 수 있다면
                break                                               # 다른 행동 하지마라.
            else:
                for charge_stop in charge_stops:                    # 버스 충전소 리스트 안의 버스 충전소의 위치 값을 인자로 하여 반복문 생성
                    if bus <= charge_stop <= (bus+bus_battery):     # 만약 bus의 현재 위치보다 멀리 충전소가 있고, 버스가 갈 수 있는 곳안에 충전소가 있다면
                        is_charge.append(charge_stop)               # 해당 충전소 위치를 is_charge리스트에 추가
                
                if bus == is_charge[-1]:                            # bus 위치가 충전을 해야 하는 위치라면
                    bus_battery = pullcharge                        # bus_battery를 k만큼 최대충전함
                    charge_nums += 1                                # 충전횟수를 1만큼 추가한다.

        bus += 1                                                    # 버스가 한 정류장을 지나면 다음 정류장이니 +1
        bus_battery -= 1                                            # 정류소 지날 때마다 배터리가 줄어듬 고로 -1
    if bus_battery == 0 and bus != N:                               # 종점이 아닌데 충전기 설치 잘못으로 버스가 운행중단한 상황이면
        print(f'#{testcase} 0')                                     # 0을 출력
    else:                                                           # 잘 작동했으면
        print(f'#{testcase} {charge_nums}')                         # 출력값대로 출력