# 문제
# 자연수 
# \(N\)과 정수 
# \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 
# \(N\)과 
# \(K\)가 주어진다. (1 ≤ 
# \(N\) ≤ 4,000,000, 0 ≤ 
# \(K\) ≤ 
# \(N\))

# 출력
 
# \(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 출력한다.

#################
# # 실패
# import sys

# # def factorial(N):
# #     if N ==1:
# #         return 1
# #     return N*factorial(N-1)

# def facto(N):
#     value = 1
#     for i in range(1, N+1):
#         value = value*i
#     return value

# N, K = map(int, sys.stdin.readline().strip().split())

# combination = facto(N) /(facto(N-K)*facto(K))
# print((int(combination) % 1000000007))

##################################
######## 시간 초과
# def binomial(N, K):
#     # K가 0이거나 N이라면 1을 반환 nCn =1 이니까
#     if K == 0 or K == N:
#         return 1
#     # 이후 계산량을 줄이기 위해 조합의 대칭성을 이용함
#     if K > N - K:
#         K = N - K
#     # i개의 원소중 j개를 선택하는 경우의 수
#     dp = [0] * (K+1)
#     dp[0] = 1
#     for i in range(1, N+1):
#         for j in range(min(i, K), 0, -1):
#             dp[j] = (dp[j] + dp[j-1]) % 1000000007
    
#     # K 개를 선택하는 경우의 수를 반환
#     return dp[K]

# import sys
# N, K = map(int, sys.stdin.readline().strip().split())
# print(binomial(N, K))

# 페르마의 소정리를 반드시 알아야한다!
# 추가로 나머지(Modulo)연산 분배법칙도!
n, k = map(int,input().split())
P = 1000000007

def factorial(num, mod):
    result = 1
    for i in range(2, num+1):
        result = result * i % P
    return result

def power(num, p, mod):
    if p == 1:
        return num % mod
    
    # 분할 정복 이용!
    if p % 2:
        return ((power(num,p//2,mod) ** 2) * num) % mod
    else:
        return (power(num,p//2,mod) ** 2) % mod
    
print(factorial(n, P) * power((factorial(k, P) * factorial(n-k, P)), P-2, P) % P)