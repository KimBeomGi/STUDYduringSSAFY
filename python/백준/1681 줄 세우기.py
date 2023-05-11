# 문제
# 민승이는 N(1 ≤ N ≤ 1,000,000)명의 학생들에게 양의 정수로 된 라벨을 붙이려고 한다. 하지만 모든 학생들은 숫자 L(0 ≤ L ≤ 9)이 자신의 라벨 숫자에 포함되길 원치 않는다. 

# 문제는 학생들에게 숫자 L을 쓰지 않고 최소한 작은 N개의 양의 수 세트를 라벨링 할 때 학생들이 받는 라벨 중 가장 큰 수가 몇인지를 구하는 것이다.

# 입력
# 첫째 줄에 N과 L이 공백으로 구분되어 주어진다.

# 출력
# 첫째 줄에 민승이가 학생들에게 붙이는 라벨 중 가장 큰 수를 출력한다.


# 학생 수 N 들어가지 않으려는 수 L

# 우선 입력은 str로 받음
import sys
N, L = map(str, sys.stdin.readline().strip().split())


number = 0                      # number = 0으로 초기화
for i in range(int(N)):         # N만큼 반복해서 수를 찾아내기위함
    number += 1                 # 학생 한명당 수를 1 더해주기
    if L in str(number):        # 만약 들어가지 않으려는 수가 들어있으면
        while L in str(number): # 안들어간 수가 될 때까지 number에 +1 하기
            number += 1
print(number)                   # 출력