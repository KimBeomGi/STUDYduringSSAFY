# 다음과 같이 두 개의 숫자 N, M이 주어질 때, N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현해 보아라.
# 2 5 = 2 X 2 X 2 X 2 X 2 = 32
# 3 6 = 3 X 3 X 3 X 3 X 3 X 3 = 729

# [제약 사항]
# 총 10개의 테스트 케이스가 주어진다.
# 결과 값은 Integer 범위를 넘어가지 않는다.
 
# [입력]
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 두 개의 숫자가 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

import sys
sys.stdin = open('230213 4일차-거듭제곱.txt', 'r')

# [문제풀이]



# T = int(input())
# for testcase in range(1, T+1):
#     N, M = map(int, input().split())                    # 숫자 N, 거듭제곱횟수 M
#     K = N
#     for i in range(M-1):
#         N = N*K
#     print(N)


# T = 10
# for testcase in range(1, T+1):
#     A = int(input())
#     N, M = map(int, input().split())                    # 숫자 N, 거듭제곱횟수 M
#     def multimulti(N, M):
#         if M == 0:
#             return 1
#         elif M == 1:
#             return N
#         else:
#             return N*multimulti(N, M-1)
#     print(f'#{testcase } {multimulti(N,M)}')

T = 10
for testcase in range(1, T+1):
    A = int(input())
    N, M = map(int, input().split())                    # 숫자 N, 거듭제곱횟수 M
    def multimulti(N, M):
        if M == 2:
            return N*N
        else:
            return N*multimulti(N, M-1)
    print(f'#{testcase } {multimulti(N,M)}')