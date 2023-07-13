# # 문제
# # 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# # 1+1+1+1
# # 1+1+2
# # 1+2+1
# # 2+1+1
# # 2+2
# # 1+3
# # 3+1
# # 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# # 입력
# # 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

# # 출력
# # 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.


# 입력값
# 3
# 4
# 7
# 10

# 출력값
# 7
# 44
# 274

import sys                          # 빠른 입력받기를 위한 import sys

# find_many라는 1,2,3을 이용해 n을 만들수 있는 갯수 찾는 함수
def find_many(value):
    global count                    # global로 count를 설정
    if value == n:                  # value == n이면 count+1 하고 반환
        count += 1
        return
    elif value > n:                 # vlaue > n이면 count는 냅두고 반환
        return
    else:                           # 그 이외는 그냥 더해주기
        for i in range(3):          # for 문으로 1,2,3을 돌아가며 더하기
            value += numbers[i]
            find_many(value)
            value -= numbers[i]     # 빼주는 이유는 그래야 똑같은 상황을 만들어주니까
        return

# 입력받고 출력해주기
T= int(sys.stdin.readline())
for testcase in range(T):
    n = int(sys.stdin.readline())
    numbers = [1,2,3]
    count = 0
    find_many(0)
    print(count)