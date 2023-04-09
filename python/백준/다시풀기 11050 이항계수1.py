

# 11050 이항 계수1
# import sys

# # 조합을 구하는 nCr이므로 여기선 NCK를 구하는 문제이다.
# N, K = map(int, sys.stdin.readline().strip().split())
# tmp = [1] * (N+1)
# for i in range(2, N+1):
#     tmp[i] = i * tmp[i-1]

# answer = tmp[N] // (tmp[K] * tmp[N-K])

# print(answer)

import sys
# 팩토리얼을 만들자!
def factorial(N):
    if N == 0:
        return 1
    else:
        return N*factorial(N-1)

# 조합을 구하는 nCr이므로 여기선 NCK를 구하는 문제이다.
N, K = map(int, sys.stdin.readline().strip().split())

print(int(factorial(N) / (factorial(K)*factorial(N-K))))