import sys
sys.stdin=open('230328 5202 화물도크.txt','r')

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    data = [tuple(map(int, input().split())) for _ in range(N)]
    # 활동 선택 문제
    # 최대한 많은 활동을 선택하기 위해서는 어떻게 해야 하는가?
    # 1. 종료시간을 기준으로 정렬
    # 2. 가장 빨리 끝나는 활동을 선택
    #   단, 시작 시간이 이전 활동의 종료시간보다는 이후여야 한다.
    cnt = 0         # 선택한 활동의 갯수
    data.sort(key = lambda x:x[1])     # 종료 시간 기준으로 정렬
    # print(data)
    prev = data[0]
    cnt += 1
    for i in range(1,N):
        # 선택하려는 활동이 이전 활동이 끝나고 시작했는지 화인
        if data[i][0] >= prev[1]:   # 시작 시간이 이전활동의 종료시간보다 뒤에 있냐?
            cnt += 1
            prev = data[i]
    print(f'#{testcase} {cnt}')