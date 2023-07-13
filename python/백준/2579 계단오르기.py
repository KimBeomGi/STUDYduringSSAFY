# 문제
# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.



# <그림 1>

# 예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.



# <그림 2>

# 계단 오르는 데는 다음과 같은 규칙이 있다.

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 입력의 첫째 줄에 계단의 개수가 주어진다.

# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

# 출력
# 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

# 입력값
# 6
# 10
# 20
# 15
# 25
# 10
# 20

# 출력값
# 75

# import sys
# n = int(sys.stdin.readline().strip())
# steps = [0]
# dp = [0]

# #입력받기
# for _ in range(n):
#     steps.append(int(sys.stdin.readline().strip()))
# print('aaaaa',steps)

# dp.append(steps[1])
# if n > 1:
#     dp.append(steps[1] + steps[2])

# for i in range(3, n + 1):
#     dp.append(max(dp[i - 1], dp[i - 3] + steps[i - 1] + steps[i], dp[i - 2] + steps[i]))
# print(dp[n])

# import sys

# n = int(sys.stdin.readline().strip())  # 계단의 개수

# scores = []  # 각 계단의 점수를 담을 리스트
# for _ in range(n):
#     scores.append(int(sys.stdin.readline().strip()))

# dp = [0] * n  # 각 계단까지의 최대 점수를 저장할 DP 테이블

# # 초기값 설정
# dp[0] = scores[0]
# dp[1] = scores[0] + scores[1]
# dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

# # 점화식을 이용하여 DP 테이블 갱신
# for i in range(3, n):
#     dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

# print(dp[n-1])


# import sys
# input = sys.stdin.readline

# n = int(input())  # 계단의 개수

# scores = []  # 각 계단의 점수를 담을 리스트
# for _ in range(n):
#     scores.append(int(input()))

# dp = [] # 각 계단까지의 최대 점수를 저장할 DP 테이블

# # 초기값 설정
# dp.append(scores[0])
# dp.append(max(scores[0] + scores[1], scores[1]))
# dp.append(max(scores[0] + scores[2], scores[1] + scores[2]))

# # 점화식을 이용하여 DP 테이블 갱신
# for i in range(3, n):
#     dp.append(max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i]))

# # print(dp[n-1])
# print(dp.pop())



# import sys
# input = sys.stdin.readline
# arr = []
# dp = []

# l = int(input())
# for _ in range(l):
#     arr.append(int(input()))

# dp.append(arr[0])
# dp.append(max(arr[0]+arr[1],arr[1]))
# dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
# for i in range(3,l):
#     dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]))

# print(dp[n-1])


# 위처럼 하면 시간초과난다.....
########################
# 아래처럼 해야 된다.

N = int(input())
# dp에 사용할 배열과 각 계단에 저장할 값을 선언
dp = [0] * (N+1)
point = [0] * (N+1)
for i in range(1, N+1):
    point[i] = int(input())
if N==1:
    print(point[1])
    exit()
elif N==2:
    print(sum(point[:3]))
    exit()
dp[1] = point[1]
dp[2] = point[1]+point[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i])

print(dp[-1])