# 문제
# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.

import sys

A = sys.stdin.readline().strip()
dec = int(A, 2)
# print(dec)
octa = oct(dec)
print(octa[2:])