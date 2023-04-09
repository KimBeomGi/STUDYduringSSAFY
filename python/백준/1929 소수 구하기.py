# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# import sys

# M, N = map(int, sys.stdin.readline().strip().split())

# for i in range(M, N-1):
#     if i%2 !=0:
#         for x in range(3,i):
#             if not i%x:
#                 break
#         else:
#             print(i)

#### '에라토스테네스의 체' 가 필요한 문제이다

import sys

M, N = map(int, sys.stdin.readline().strip().split())
sieve = [True] * (N+1)                      # 모두 소수라고 가정중(인덱스를 이용하므로 N+1개)
sieve[0] = sieve[1] = False                 # 소수가 아님

for i in range(2, int(N**0.5)+1):           # 2부터 N의 제곱근 까지 반복하기
    # 에라토스테네스의 체 알고리즘 개념에 따라 N**5까지만 확인하도록 함
    if sieve[i]:                            # 만약 sieve[i] 가 True라면 확인을 하는데
        for j in range(2*i, N+1, i):        # 배수인지 확인하기 위해 2*i부터 쭉 확인
            sieve[j] = False                # 배수인 sieve[j] 는 약수가 있으니 소수가 아님.

for k in range(M, N+1):                     # 이제 M~N까지 소수를 찾자
    if sieve[k]:                            # sieve[k] True라면
        print(k)                            # 소수니까 print


# import sys

# M, N = map(int, sys.stdin.readline().strip().split())

# # M과 N 사이의 모든 숫자를 소수(True)라고 가정
# sieve = [True] * (N+1)

# # 0과 1은 소수가 아니므로 False로 변경
# sieve[0] = sieve[1] = False

# # 2부터 N의 제곱근까지 반복하면서, i의 배수들을 False로 변경
# for i in range(2, int(N**0.5)+1):
#     if sieve[i]:
#         for j in range(i+i, N+1, i):
#             sieve[j] = False

# # M부터 N까지 반복하면서, sieve[i]가 True인 숫자를 출력
# for i in range(M, N+1):
#     if sieve[i]:
#         print(i)
