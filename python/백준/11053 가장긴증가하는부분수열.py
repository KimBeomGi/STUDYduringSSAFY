# # 가장 긴 증가하는 부분 수열
 
# # 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# # 1 초	256 MB	139626	55369	36589	37.663%
# # 문제
# # 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# # 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# # 입력
# # 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# # 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# # 출력
# # 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 입력값
# 6
# 10 20 10 30 20 50

# 출력값
# 4


# def find_length(value, i, length):
#     global max_length
#     global N
#     if value >= A[i]:
#         if length > max_length:
#             max_length = length
#         return
#     else:
#         if i + 1 >= N:
#             if length > max_length:
#                 max_length = length
#             return
#         else:
#             find_length(A[i], i+1, length+1)
#             return



# N = int(input())
# A = list(map(int,input().split()))
# max_length = 0
# find_length(0, 0, 0)
# print(max_length)

import sys

n = int(sys.stdin.readline())  # 수열의 길이 입력
A = list(map(int, sys.stdin.readline().split()))  # 수열 입력

dp = [1] * n  # 각 인덱스에서 끝나는 가장 긴 증가하는 부분 수열의 길이 저장

for i in range(n):                          # 0 ~ n-1 까지
    for j in range(i):                      # 0 ~ i-1 까지
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
result = max(dp)  # 가장 큰 값이 가장 긴 증가하는 부분 수열의 길이

print(result)
