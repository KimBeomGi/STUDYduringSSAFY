# 문제
# 효주는 포도주 시식회에 갔다. 그 곳에 갔더니, 테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다. 효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.

# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다. 1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오. 

# 예를 들어 6개의 포도주 잔이 있고, 각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때, 첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.

# 입력
# 첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

# 출력
# 첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

# 입력값
# 6
# 6
# 10
# 13
# 9
# 8
# 1

# 출력값
# 33


# 문제풀이
# 1.

# 7 10 13 5

# wines = []
# N = int(input())
# for _ in range(N):
#     wines.append(int(input()))

# dp = [0]*N
# dp[0] = wines[0]
# if N > 1:
#     dp[1] = wines[0] + wines[1]ㅁ

# for i in range(2,N):
#     dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-2] + wines[i-1])
# print(dp[N-1])


import sys
n = int(sys.stdin.readline().strip())
wines = [0]                         # 인덱스 1부터 사용하기 위해 wine잔 수 리스트를 생성
dp = [0]                            # 인덱스 1부터 사용할 dp(동적프로그램)

#입력받기
for _ in range(n):
    wines.append(int(sys.stdin.readline().strip()))      # 입력

dp.append(wines[1])                 # dp에 첫 와인잔의 포도주를 집어넣고 시작. dp는 [0, wines[1]의 값] 이 되어있음.
if n > 1:                           # 1보다 N이 크면
    dp.append(wines[1] + wines[2])  # dp에 1째 잔과 2째 잔을 더한 것을 추가. dp는 [0, wines[1]의 값, wines[1]+wines[2]값]

for i in range(3, n + 1):
    # 3개를 연속하지 못하므로 3개의 경우가 있다.
    # 1. i번째 잔을 마시지 않는 경우.(range(3,n+1)로 되어있으니 i는 3번째 잔부터 적용된다.)
    # 2. i번째 잔을 마시고 i-1번째 잔을 마시는 경우.(i-2)을 안마심
    # 3. i번째 잔을 마시고 i-2번째 잔을 마시는 경우.(i-1)을 안마심
    dp.append(max(dp[i - 1], dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i]))
    # 순서대로, 1번, 2번, 3번의 값을 추가 및 비교하고 max값을 dp에 추가한다.
    # max값을 집어넣게되니 추가되는 값은 항상 i번째 잔의 갯수가 있을때의 최댓값이다.

# for 문이 3부터 시작이므로 잔 수가 1또는 2이면 이미 최댓값은 dp.append(wines[1])과 if문으로 정의완료되었으니 문제X
print(dp[n])



###
# 아래는 다른사람이 푼 방식


# N = int(input())
# cups = [int(input()) for _ in range(N)]
# if N <= 2:
#     print(sum(cups))
# else:
#     res = 0
#     dp = [[0, 0, 0] for _ in range(N)]
#     dp[0] = [cups[0], cups[0], 0]
#     dp[1] = [cups[0] + cups[1], cups[1], cups[0]]
#     for i in range(2, N):
#         dp[i] = [dp[i-1][1] + cups[i], max(dp[i-2]) + cups[i], max(dp[i-1])]
#         if res < max(dp[i]):
#             res = max(dp[i])
#     print(res)