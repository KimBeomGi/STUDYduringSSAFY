# 문제
# A×B를 계산하다 지겨워진 형택이는 A×B를 새로운 방법으로 정의하려고 한다.

# A에서 한 자리를 뽑고 × B에서 임의로 한 자리를 뽑아 곱한다.

# 의 가능한 모든 조합 (A가 n자리, B가 m자리 수라면 총 가능한 조합은 n×m개)을 더한 수로 정의하려고 한다.

# 예를 들어 121×34는

# 1×3 + 1×4 + 2×3 + 2×4 + 1×3 + 1×4 = 28

# 이 된다. 이러한 형택이의 곱셈 결과를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. 주어지는 두 수는 모두 10,000자리를 넘지 않는 음이 아닌 정수이다. 수가 0인 경우에는 0만 주어지며, 그 외의 경우 수는 0으로 시작하지 않는다.

# 출력
# 첫째 줄에 형택이의 곱셈 결과를 출력한다.


# 1. 양의 정수 A와 B가 주어지면 이를 각 자리수를 곱한후 더해서 그 총합을 낸다.
# 2. 수가 0 인 경우엔 0만 주어진다.

# ##### 시간 초과
# import sys

# numbers = list(map(str, sys.stdin.readline().strip().split()))

# if len(numbers) == 1 and numbers[0] == '0':
#     print(0)
#     sys.exit()

# a = list(numbers[0])
# b = list(numbers[1])

# sum_value = 0
# for i in range(len(a)):
#     for j in range(len(b)):
#         sum_value += int(a[i])*int(b[j])
# print(sum_value)

# 1. 양의 정수 A와 B가 주어지면 이를 각 자리수를 곱한후 더해서 그 총합을 낸다.
# 2. 수가 0 인 경우엔 0만 주어진다.

# 예시의 1×3 + 1×4 + 2×3 + 2×4 + 1×3 + 1×4 = 28는
# (1+2+1)*3+(1+2+1)*4가 되고, 또한 (1+2+1)*(3+4)가 된다.
# 따라서 각 수의 합의 곱이 답이 된다.

import sys
numbers = list(map(str, sys.stdin.readline().strip().split()))
# 입력 조건에서 수가 0인 경우 0만 주어진다고 했기에 if문을 작성
if len(numbers) == 1 and numbers[0] == '0':
    print(0)
    sys.exit()

# 수 2개를 입력받은 리스트 numbers를 이용해서 A,B를 구분하고, 각 수의 합을 구함
A = list(map(int,numbers[0]))
B = list(map(int,numbers[1]))
# 그리고 A*B해서 값 구하기
print(sum(A)*sum(B))