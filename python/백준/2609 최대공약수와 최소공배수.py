# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

import sys

# 최대 공약수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N, M = map(int, sys.stdin.readline().strip().split())

print(gcd(N,M))
#최대 공배수
lcm = int((N*M)/gcd(N,M))
print(lcm)