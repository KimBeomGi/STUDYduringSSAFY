# Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
# 3 4 + .
# Forth에서는 동작은 다음과 같다.
# 숫자는 스택에 넣는다.
# 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
# ‘.’은 스택에서 숫자를 꺼내 출력한다.
# Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
# 다음은 Forth 연산의 예이다.

# 코드        출력
# 4 2 / .     2
# 4 3 - .     1

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
# 나눗셈의 경우 항상 나누어 떨어진다.

# [출력]
# #과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다

import sys
sys.stdin = open('230215 5일차-Forth.txt', 'r')

# # [문제풀이]
# # 0. 후위 표기법으로 되어있는 연산식을 연산해야 하는 것이다.
# # 0-1. '.'은 문장의 맨 마지막에서 사용되며, 이를 만나면 연산을 시작한다.
# # 1. 스택을 이용해서 해결해보자.

def postifix_cal(calculation):
    cal_len = len(calculation)
    stack = [0]*cal_len                                         # stack을 받을 것이고, top을 이용해 볼것이다.
    top = -1                                                    # top은 -1로 해서 값이 텅텅 비어있다면 -1을 가리키게 될 것이다.
    cal_operation = ['*', '/', '+', '-', '.']
    # 계산 시작
    for i in range(cal_len):                                    # calculation의 길이만큼 반복해서 calculation의 요소들을 이용한다.
        if calculation[i] not in cal_operation:                 # 연산식의 요소가 연산자가 아닌 숫자이면
            try:                                                # 다음 내용이 가능하다면 다음을 실행행
                top += 1                                        # tyr-1. top을 +1 해주고
                stack[top] = int(calculation[i])                # try-2 stack[top]에 연산자의 숫자를 기입한다.
            except:                                             # try의 내용이 불가하면 다음울 출력
                return 'error'
        # 연산자를 만나게 된다면, top > 0을 작성한 이유는 적어도 2개의 요소는 필요하기 때문.
        elif top > 0 and calculation[i] == '*':                 # 연산식의 요소가 *연산자라면
            stack[top-1] = stack[top-1] * stack[top]
            top -= 1
        elif top > 0 and calculation[i] == '/':                 # 연산식의 요소가 /연산자라면
            stack[top-1] = stack[top-1] // stack[top]           # / 사용시혹시 모를 '실수'발생에 대비하기 위해//이용
            top -= 1
        elif top > 0 and calculation[i] == '+':                 # 연산식의 요소가 +연산자라면
            stack[top-1] = stack[top-1] + stack[top]
            top -= 1
        elif top > 0 and calculation[i] == '-':                 # 연산식의 요소가 -연산자라면
            stack[top-1] = stack[top-1] - stack[top]
            top -= 1
        elif top == 0 and calculation[i] == '.':                # 연산식의 요소가 -연산자라면
            return stack[top]
        else:
            return 'error'
    return 'error'

T = int(input())
for testcase in range(1, T+1):
    calculation = list(map(str, input().split()))               # 연산식을 받는데 연산식이 띄어쓰기로 입력되므로 더 잘 활용하기위해 split이용 리스트로 받음.

    print(f'#{testcase} {postifix_cal(calculation)}')