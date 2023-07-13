# 문제
# 모든 자리가 1로만 이루어져있는 두 자연수 A와 B가 주어진다. 이때, A와 B의 최대 공약수를 구하는 프로그램을 작성하시오.

# 예를 들어, A가 111이고, B가 1111인 경우에 A와 B의 최대공약수는 1이고, A가 111이고, B가 111111인 경우에는 최대공약수가 111이다.

# 입력
# 첫째 줄에 두 자연수 A와 B를 이루는 1의 개수가 주어진다. 입력되는 수는 263보다 작은 자연수이다.

# 출력
# 첫째 줄에 A와 B의 최대공약수를 출력한다. 정답은 천만 자리를 넘지 않는다.



# 입력값
# 3 4
# 1679 874
# 3762 4047
# 6080 3876


# 출력값
# 1
# 23
# 57
# 76  


# 유클리드 호제법은 다음과 같은 원리로 동작합니다:

# 두 개의 정수를 가지고 시작합니다. 이를 a와 b라고 합시다. (a ≥ b)
# a를 b로 나눈 나머지를 구합니다. 나머지를 r이라고 합시다. (r = a % b)
# r이 0이면, b가 최대공약수입니다. 알고리즘을 종료합니다.
# r이 0이 아니라면, a에는 b를 대입하고, b에는 r을 대입한 후, 2번부터 다시 반복합니다.

# # uclid 호제법을 이용한 최대공약수 찾기
def uclid(a, b):
    r = a % b       # a, b, a%b로 3가지로 구분하기 위함.
    if r == 0:      # r == 0 이면 b가 최대공약수가 됨
        return b
    # else:
    #     a = b
    #     b= r
    return_value = uclid(b,r)
    return return_value

# 입력받기
import sys

a, b = map(int, sys.stdin.readline().strip().split())
if a < b :
    a, b = b, a

print('1'*uclid(a, b))




# import sys

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# a, b = map(int, sys.stdin.readline().split())
# answer = gcd(a, b)

# print('1' * answer)