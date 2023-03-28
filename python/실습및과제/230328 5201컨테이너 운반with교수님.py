import sys
sys.stdin = open('230328 5201컨테이너 운반.txt','r')

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    # 무거운 컨테이너를 중량이 큰 트럭에 실어주기
    containers.sort()
    trucks.sort()
    i, j= N-1, M-1
    result = 0
    while i >= 0 and j >= 0:     # 트럭과 컨테이너 둘다 남아있으면 검사
        # j 번째 트럭이 i 번째 컨테이너를 실을 수 있나?
        if trucks[j] >= containers[i]:
            result += containers[i]
            j -= 1
            i -= 1
        else:   # j번째 트럭이 i번째 container를 싣지 못한다.
            i -=1   # i번째 container는 다른 트럭도 어차피 못 실음.
    print(f'#{testcase} {result}')