# 문제
# 학생들은 3주가 지난 기념으로 매점에서 1월 1일이 지나 싸게 파는 폭죽을 사서 터뜨리고 있다.

# 폭죽쇼를 하는 동안 N명의 학생들이 폭죽을 터뜨린다. 그리고 이 N명의 학생은 각각 일정한 주기로 폭죽을 터뜨린다. 물론 이 주기는 학생들마다 같을 수도, 다를 수도 있다. 그리고 우리는 초 단위로 관찰을 하고, 폭죽 역시 초 단위로 터진다.

# 폭죽쇼가 끝날 때까지 얼마나 많은 시간동안 밤하늘에 폭죽이 터지는 것을 볼 수 있는지 궁금해 하는 조교를 도와주자.

# 입력
# 첫 줄에 폭죽을 터뜨리는 학생의 수 N(1 ≤ N ≤ 100)과 폭죽쇼가 끝나는 시간 C(1 ≤ C ≤ 2,000,000)가 주어진다. 그 다음 N개의 줄에는 학생들이 폭죽을 터뜨리는 주기가 한 줄에 하나씩 주어진다. 주기는 1보다 크거나 같고, C보다 작거나 같은 자연수이다.

# 출력
# 폭죽쇼가 시작되고 끝날 때까지 밤하늘에 폭죽을 볼 수 있는 총 시간을 출력한다.


# 1. 학생수 N명, 폭죽쇼 끝나는 시간 C
# 2. 각 학생이 폭죽을 터뜨리는 주기가 N줄 만큼 주어짐. 

import sys

# 입력받기
N, C = map(int, sys.stdin.readline().strip().split())
second = [0]*(C+1)                          # 0~C까지의 인덱스를 사용하기 위함

# 중복되는 간격은 없애기 위한 과정
temp = []
for _ in range(N):
    temp.append(int(sys.stdin.readline().strip()))
temp = set(temp)                            # 중복제거하고
temp = list(temp)                           # 다시 리스트

# 답 구하기
for index in range(len(temp)):              # N명이 폭죽을 쏘니까 N번
    K = temp[index]                         # 쏘는 간격 K를 입력받음
    for i in range(K, C+1, K):              # 배수는 다 색칠하려고
        if second[i] == 0:
            second[i] = 1                   # 해당 부분을 표시함

answer = sum(second)                        # second를 다 더하면 됨.
print(answer)
# print(second)

# C = 15
# K = 2
# second = [0]*(C+1)
# for i in range(K, C+1, K):    # 배수는 다 색칠하려고
#     second[i] = 1
# print(second)
