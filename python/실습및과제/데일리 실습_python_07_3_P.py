# [문제]
# 1. add, subtract, multiply, divide 메소드를 가진 Calculator클래스를 생성하고,
# 1-1. 아래의 계산 결과를 출력하라
# 2. 단, 숫자는 0으로 나눌 수 없다. 이 경우, 예외처리로 0으로 나눌 수 없습니다.를 출력하라.


# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator:                                       # Calculator 클래스 생성
    def add(num1, num2):                                # add 메소드
        return num1+num2
    def subtract(num1, num2):                           # subtract 메소드
        return num1-num2
    def multiply(num1, num2):                           # multiply 메소드
        return num1*num2
    def divide(num1, num2):                             # divide 메소드
        if num2 == 0:
            return '예외처리로 0으로 나눌 수 없습니다.'   # 0으로는 무엇도 나눌 수 없으므로 출력
        else:
            return num1/num2

print(Calculator.add(1,2))
print(Calculator.subtract(2,1))
print(Calculator.multiply(3,4))
print(Calculator.divide(4,0))
