
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


T = int(input())
for testcase in range(1, T+1):
    count = 0
    K, N, M = map(int,input().split())  # K는 이동할수 있는 거리, N은 정류장 갯수, M은 충전소 갯수
    # 충전기가 설치되어 있는 정류장 리스트 받기
    stops = list(map(int, input().split()))
    stops.append(N) # 충전소 리스트 뒤에 마지막 정류장 번호를 붙임
    stops.insert(0,0) # 충전소 맨 앞에 출발 지점을 붙임

# 이전에 충전한 위치 기억, 해당 정류장까지
# 충전 안하고 올 수 있으면 다음 정류장으로 이동
# 충전 안하고 못오면 이전 정류장에서 충전
position = 0        # 이전에 내가 충전한 정류장 번호를 저장
for i in range(1, M+2): # 첫 정류장과 마지막 정류장을 stop리스트에 집어넣어 M+2개가 되었기 때문
    if stops[i] - stops[i-1] > K:   # 현재 충전소와 이전 충전소의 거리가 K보다 크다면
        count = 0
        break                       # 왜냐하면 거리가 멀어서 못 가니까.
    if stops[i] > position + K:     # 현재 충전소가 현재의 내위치에 K를 더한 곳 보다 멀다면
        count +=1                   # 이전 정류장에서 충전하고 옴
        position = stops[i-1]
    else:
        pass

print(f'{testcase} {count}')
