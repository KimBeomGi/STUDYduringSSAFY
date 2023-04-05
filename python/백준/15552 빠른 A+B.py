# import sys

# # 한 줄을 입력받아 처리하는 예시 코드
# line = sys.stdin.readline().rstrip() # 입력된 문자열의 개행 문자를 제거합니다.
# print(line) # 입력된 문자열을 출력합니다.

import sys

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)