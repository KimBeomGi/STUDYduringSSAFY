#[문제]
#1. 사용자가 입력한 숫자의 각 자릿수를 더해 출력하는 sum_of_digit를 작성하라.
#1-1. 단, 반복문을 활용하지 않는 코드로 작성하라.
#1-2. 단, 반복문을 활용한 방법과 반복문을 활용하지 않은 방법을 모두 작성하라.

# sum_of_digit(3904) # 16

# [문제풀이]
# 1. def sum_of_digit(num): 으로 함수를 정의
# 2. 반복문을 사용하지 않아야하므로 재귀함수 이용

def sum_of_digit(num):
    if num//10 == 0:                            # 기저영역. 더 이상 재귀가 호출 되지 않도록 하는 마지막 영역
        return num%10                           # num/10의 나머지를 반환하시오
    return (num%10) + sum_of_digit(num//10)     # 첫 num/10의 나머지를 더하고 더해서 각 자리 수를 더하는 것과 같도록 만들기

print(sum_of_digit(3904))

'''
def sum_of_digit(num):
    sum_num = 0
    while num > 0:
        sum_num = sum_num + num % 10
        num = num // 10
    return sum_num

print(sum_of_digit(3904))
'''