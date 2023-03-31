#idx : 현재 위치 , cnt : 교환횟수
def solve2(idx,cnt):
    global min_v
    if cnt >= min_v:
        return
    if idx >= N-1:
        #여기 시점에서 결과를 구하라
        min_v = min(cnt,min_v)
        return 
    #현재위치에서는 무조건 배터리를 교환할겁니다.
    #어디에서 베터리를 교환할지 결정할 수 있음
    # i : 현재 교환한 배터리로 갈 수 있는 정류장의 번호
    for i in range(idx+1,idx+station[idx]+1):
        solve2(i,cnt+1)


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    station = arr[1:]
    battery = station[0]
    min_v = 100  # 정류장 수가 3 <= N <= 100 이라고 주어짐.
    # solve(1, battery - 1, 0)  # 시작 정류장에서의 배터리 장착은 교환횟수에서 제외한다고 했기 때문에
    # 두번째 정류장부터 확인해봄.
    solve2(0,0)
    print(f'#{tc} {min_v-1}')