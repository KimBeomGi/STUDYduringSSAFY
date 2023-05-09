# 문제
# 영식이가 운동을 하는 과정은 1분 단위로 나누어져 있다. 매 분마다 영식이는 운동과 휴식 중 하나를 선택해야 한다.

# 운동을 선택한 경우, 영식이의 맥박이 T만큼 증가한다. 즉, 영식이의 맥박이 X였다면, 1분 동안 운동을 한 후 맥박이 X+T가 되는 것이다. 영식이는 맥박이 M을 넘는 것을 원하지 않기 때문에, X+T가 M보다 작거나 같을 때만 운동을 할 수 있다. 휴식을 선택하는 경우 맥박이 R만큼 감소한다. 즉, 영식이의 맥박이 X였다면, 1분 동안 휴식을 한 후 맥박은 X-R이 된다. 맥박은 절대로 m보다 낮아지면 안된다. 따라서, X-R이 m보다 작으면 맥박은 m이 된다.

# 영식이의 초기 맥박은 m이다. 운동을 N분 하려고 한다. 이때 운동을 N분하는데 필요한 시간의 최솟값을 구해보자. 운동하는 시간은 연속되지 않아도 된다.

# 입력
# 첫째 줄에 다섯 정수 N, m, M, T, R이 주어진다.

# 출력
# 첫째 줄에 운동을 N분하는데 필요한 시간의 최솟값을 출력한다.. 만약 운동을 N분 할 수 없다면 -1을 출력한다.

# 제한
# 1 ≤ N, T, R ≤ 200
# 50 ≤ m ≤ M ≤ 200


# 1. 운동하면서 1분 단위로 나눠짐
# 2. 운동을 하려는 시간 N분, 초기 맥박 수 m, 최대 맥박수 M, 맥박 증가량 T, 휴식간 맥박 감소량 R,

import sys

N, m, M, T, R = map(int, sys.stdin.readline().strip().split())

count_time = 0          # 시간을 카운트 하는 변수
training_time = 0       # 운동 시간을 카운트 하는 변수

if m+T > M:
    print(-1)
    sys.exit()

pulse = m   

while training_time < N:                # 운동 시간이 목표치에 달하지 않았으면 반복
    count_time +=1                      # 시간 +1 하기
    if pulse + T <= M:                  # pulse + T도 M 이하면,
        pulse = pulse + T               # pulse에 T를 더해주기
        training_time += 1              # 운동 시간 +1
    elif pulse + T > M:                 # pulse + T도 M 이상이면,
        pulse -= R                      # 휴식을 취해서 pulse-R로 만들어주자.
        if pulse < m:                   # 휴식을 취했는데 초기 맥박 m보다 낮아져버리면
            # count_time = -1             # count_time = -1로 하고 종료\
            pulse = m
            # break

print(count_time)