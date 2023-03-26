# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
# (시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)

# [제약 사항]
# 시는 1 이상 12 이하의 정수이다. 분은 0 이상 59 이하의 정수이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
# 첫 번째 수가 시를 나타내고 두 번째 수가 분을 나타낸다. 그 다음 같은 형식으로 두 번째 시각이 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 시를 출력하고 공백을 한 칸 둔 다음 분을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
sys.stdin = open('1976 시각 덧셈.txt', 'r')


def times_modify(times):
    if times[1] > 59:
        times[1] = times[1]%60
        times[0] = times[0] + 1
    if times[0] > 12:
        times[0] = times[0]%13+1
    return times

T= int(input())
for testcase in range(1,T+1):
    two_times = list(map(int, input().split()))
    times = [two_times[0]+two_times[2], two_times[1]+two_times[3]]
    # print(times, 'and', end=' ')
    times = times_modify(times)
    print(f'#{testcase} {times[0]} {times[1]}')
