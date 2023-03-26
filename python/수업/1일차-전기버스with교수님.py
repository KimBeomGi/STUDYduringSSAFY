T = int(input())
for tc in range(1, T+1):
    cnt = 0
    K, N, M =map(int, input().split())
    # 충전기가 설치되어 있는 정류장 리스트 받기
    stops = list(map(int,input().split()))
    stops.append(N)                         # 충전소 뒤에 마지막 정류장 번호를 붙임
    stops.insert(0, 0)

    # 이전에 충전한 위치 기억, 해당 정류장까지
    # 충전 안하고 올 수 있으면 다음 정류장으로 이동
    # 충전 안하고 못오면 이전 정류장에서 충전
    position = 0                            # 이전에 내가 충전한 정류장번호를 저장
    for i in range(1, M+2):                 # 충전소가 설치된 가장 앞쪽 충전소부터 반복문 실행
        if stops[i] - stops[i-1] > K:       # 충전소가 이전 충전소까지 갈 수 없다면(K가 가능거리니까)
            cnt = 0
            break
        if stops[i] > position + K:         # 충전소가 내 위치에서 내가 갈수 있는 것보다 크다면
            #이전 정류장에서 충전
            cnt += 1
            position = stops[i-1]
        else:
            pass

    print(f'#{tc} {cnt}')