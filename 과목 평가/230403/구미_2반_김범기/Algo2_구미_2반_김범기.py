# [문제풀이]
# 0. 로봇을 이용해 각반에 필요한 물품 전달
# 1. 사무국을 출발해 모든 강의실을 돌아야하고, 각 강의식을 한 번씩만 방문
# 2. 선후로 방문해야하는 2개의 강의실이 주어지는데 a를 먼저 방문해야하고, 그다음 b를 방문해야한다.
# 3. 어떻게 가든 상관 없다 꼭 바로 옆강의실로 갈필요는 없다.
# 2-1. 이대 a와 b 사이에는 어떤 강의실이 있든 상관없다.
# 3. 단 a 가 꼭 모든 강의실중 1번째로 들릴필요는 없다.

# 함수 생성
def min_battery(start, end, battery):
    # print(end)
    global min_value                        # 배터리 최저 사용량을 global로 데려오기

    # 모든 곳을 방문했다면?
    if all(visited):
        battery = battery + matrix[end][0]  # battery는 battery + matrix[end][0]의 값과 같다.
        if min_value > battery:             # 만약 min_value가 battery보다 크면 
            min_value = battery             # min_value를 battery로 교체
        return

    # 가지치기 가능할 거 같은데.....
    # # 가지치기
    # if min_value != 100*N*N+1:
            # 아래를 쓰면 끝까지 가기전에 모든 함수가 다 return 해버림
    #     if sum(visited) > 2 and min_value > battery:    # min_value가 현재 battery보다 더 크면 보지말고 돌아가
    #         return

    for j in range(1, N):               # 모든 강의실 방문해보기:
        if j == B and not visited[A]:   # 지금 확인하는 강의실이 B강의실인데 A를 방문하지 않았다면
            continue                    # 넘어가고 다른 강의실 찾으러 가자
        if not visited[j]:              # 방문 안했으면
            visited[j] = 1              # 방문 했음으로 변경하고  # 멍청하게 visited[j] == 1로 해놓고 안된다 하고 있었음.
            min_battery(end, j, battery+matrix[end][j]) # 방문하자
            visited[j] = 0              # 확인 완료했으니 다음 확인하러 가려면 방문기록 삭제
    return

# 입력받기
T = int(input())
for testcase in range(1, T+1):
    N = int(input())                # (사무국1개 + 강의실 갯수) N
    matrix = [list(map(int, input().split())) for _ in range(N)]    # N by N 행렬 생성
    A, B = map(int, input().split())       # 먼저 방문해야할 A와 뒤에 방문할 B 입력받음
    visited = [0] * N               # 사무국과 N-1개의 강의실을 방문
    visited[0] = 1                  # 사무국은 방문한걸로 표시하기
    min_value = 100*N*N+1           # 배터리 사용량 최댓값으로 설정

    # 함수 활용
    for i in range(1, N):           # i를 통해 첫 출발할 강의실을 생성
        if i == B:                  # B가 제일 먼저 출발하는 경우는 제외 시킴
            continue
        visited[i] = 1              # 이제 방문하는 곳이 방문했음을 기록
        min_battery(0, i, matrix[0][i])     # 함수카드 발동!
        visited[i] = 0              # 확인하고 왔으니 방문기록 삭제
    print(f'#{testcase} {min_value}')