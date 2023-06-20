# 문제
# C언어 성적이 나쁜 학생이 C언어를 드랍하고 경제학 원론을 듣는다면, 그 학생은 두 과목 수강생의 평균 IQ를 올려준다.
# 이 말은 어떤 학생이 직접 C언어를 드랍하고 경제학 원론을 수강하면서 증명하였다.
# 각 학생의 IQ가 주어진다. 이때, C언어 수강생 중에 C언어를 드랍하고 경제학 원론을 수강해서 두 과목의 평균 IQ를 모두 올려줄 수 있는 사람의 수를 구하시오.


# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 빈 줄로 구분되며, 다음과 같이 구성되어 있다. 
# 테스트 케이스의 첫째 줄에는 C언어 수강생의 수 N과 경제학 원론 수강생의 수 M이 주어진다. 둘째 줄에는 N+M 개의 숫자가 공백으로 구분되어 주어진다. 
# 처음 N개의 숫자는 C언어 수강생의 IQ이며, 다음 M개의 숫자는 경제학 원론 수강생의 IQ이다.
# N과 M은 200,000보다 작거나 같은 자연수이고, N은 2보다 크거나 같다. IQ는 100,000보다 작거나 같은 자연수이다.

# 출력
# 각 테스트 케이스의 정답을 한 줄에 하나씩 차례대로 출력한다.

# 예제 입력 1 
# 1

# 5 5
# 100 101 102 103 104
# 98 100 102 99 101
# 예제 출력 1 
# 1
# 힌트
# C언어 수강생의 IQ를 올릴 수 있는 학생은 1번 학생과, 2번 학생이다. 근데, 1번 학생은 너무 멍청해서 경제학 원론을 수강해도 평균 IQ를 올리지 못한다. 하지만, 2번 학생은 할 수 있다.


# 문제풀이
# 1. c언어를 드랍하고 경제학 원론을 수강해서 두 과목으 ㅣ평균 IQ를 모두 올려줄 수 있는 사람의 수!
# 1.1 뭔말이냐면 C언어 대신 경제학 원론을 듣겠다는 말임

import sys

T = int(sys.stdin.readline().strip())
for testcase in range(T):
    space = input()                                                      # 테스트케이스의 빈 공백 입력 받음
    N, M = map(int, sys.stdin.readline().strip().split())                # C언어, 경영학 학생 수
    C_list = list(map(int, sys.stdin.readline().strip().split()))        # C언어 듣는 사람의 IQ
    Eco_list = list(map(int, sys.stdin.readline().strip().split()))      # 경영학 듣는 사람의 IQ
    C_sum = sum(C_list)                                                  # C언어 듣는 사람들의 IQ합
    Eco_sum = sum(Eco_list)                                              # 경영학 듣는 사람들의 IQ합
    count_a = 0   # C언어 드랍시 각 강의의 전체 IQ를 올려줄 수 있는 사람 수
    
    for i in range(N):      # 0 ~ N-1까지 이용. 인덱스를 이용
        # C언어 듣는 사람들의 평균 보다 낮은 사람만 확인하면 됨. 그리고 이 인간의 IQ가 경영학을 듣는 사람의 평균IQ보다 높을때만!
        if C_list[i] * N < C_sum and C_list[i] * M > Eco_sum:
            count_a += 1                                                 # count +1하기
    print(count_a)





# import sys

# T = int(input())

# for _ in range(T):
#     sys.stdin.readline()
#     n, m = map(int, input().split())
#     arra = list(map(int, input().split()))
#     suma = sum(arra)
#     sumb = sum(map(int, input().split()))
#     s = 0
#     for i in range(n):
#         if arra[i] * n < suma and arra[i] * m > sumb:
#             s += 1
#     print(s)