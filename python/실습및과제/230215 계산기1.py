

# 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
# 예를 들어

# “3+4+5+6+7”
# 라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

# "34+5+6+7+"
# 변환된 식을 계산하면 25를 얻을 수 있다.
# 문자열 계산식을 구성하는 연산자는 + 하나뿐이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 문자열 계산식의 길이가 주어진다. 그 다음 줄에 문자열 계산식이 주어진다.
# 총 10개의 테스트 케이스가 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다


import sys
sys.stdin = open('230215 계산기1.txt', 'r')

# [문제풀이]
# 1. 중위표기법을 후위표기법으로 바꾼후, 후위표기법 연산식으로 연산해보자.

# 연산자 우선순위
isp = {'*':2, '/':2, '+':1, '-':1, '(':0}                       # 인스택, 스택안에 들어있을 때
icp = {'*':2, '/':2, '+':1, '-':1, '(':3}                       # 인커밍, 스택에 들어갈 때

# 중위표기법에서 후위표기법으로 전환
def infix_postfix(infix_cal):
    num_list = []                                               # 중위표기법 연산식에서 후위표기법으로 변환 시 숫자를 담아둘 리스트
    stack =[0]*N                                                # stack을 만들어서 후위표기법으로 만들어서 계산을 하기 위함
    top = -1                                                    # stack에 사용할 때 쓸 top 변수
    for i in range(N):                                          # infix_cal의 길이만큼 반복문 실행
        # 정수를 받음
        if infix_cal[i] not in '*/+-()':                        # 연산자 아닌 숫자 받기
            num_list.append(infix_cal[i])                       # 현재 정수를 출력한다.
        
        # 연산자를 받음
        else:
            if infix_cal[i] == ')':                             # 닫힌괄호를 만나게 된다면
                while stack[top] != '(':                        # 스택에서 열린괄호를 만날때까지
                    num_list.append(stack[top])                 # 현재 stack값을 출력한다
                    top -= 1                                    # top도 한 칸 내린다.
                top -= 1                                        # 열린괄호를 마저 stack에서 빼주기 위해서 top을 또 1칸 내린다.
            
            elif top == -1:                                     # top이 -1이면, 즉 stack활용 값이 없으면
                top += 1                                        # top을 한칸 올리고
                stack[top] = infix_cal[i]                       # stack[top]을 현재 i의 값으로 만들어준다.
            
            else:                                               # top이 -1이 아니면, 즉 활용가능한 stack 값이 있으면
                if isp[stack[top]] < icp[infix_cal[i]]:         # stack[top]의 값보다 infix_cal[i]의 값이 우선순위가 높다면
                    top += 1                                    # top을 한칸 올리고
                    stack[top] = infix_cal[i]                   # stack[top]에 infix_cal[i]값을 대입
                else:                                           # stack[top]의 값보다 infix_cal[i]의 값이 우선순위가 낮거나 같다면
                    # 만약 현재 infix_cal[i]연산자의 우선순위가 stack에 들어있는 우선순위보다 작으면
                    while top > -1 and isp[stack[top]] >= icp[infix_cal[i]]:
                        num_list.append(stack[top])             # stack에 있는 연산자를 먼저 출력한 후
                        top -= 1
                    top += 1                                    # infix_cal[i]연산자를 stack에 넣어라
                    stack[top] = infix_cal[i]
    while top > -1:                                             # 활용가능한 stack값이 있을 때 까지
        num_list.append(stack[top])
        top -= 1
    return num_list

def postfix_cal(postfix_cal_list):
    stack =[0]*N                                                # stack을 만들어서 후위표기법을 계산 하기 위함
    top = -1                                                    # stack에 사용할 때 쓸 top 변수
    for i in range(N):                                          # N만큼의 반복문 실행    
        # 정수를 받음
        if postfix_cal_list[i] not in '*/+-':                   # 정수를 받으면
            top += 1
            stack[top] = int(postfix_cal_list[i])               # 문자로 되어있는 정수를 숫자로 변경
        
        # 연산자를 받음
        else:                                                   # 이때 순서 중요!
            if postfix_cal_list[i] == '*':                      # *연산자의 경우
                stack[top-1] = stack[top-1] * stack[top]        # top-1의 값과 top의 값을 곱해줌
                top -=1                                         # 연산 후 top을 한칸 내려준다.
            elif postfix_cal_list[i] == '/':                    # /연산자의 경우
                stack[top-1] = stack[top-1] / stack[top]        # top-1의 값을 top의 값으로 나눠줌
                top -=1                                         # 연산 후 top을 한칸 내려준다.
            elif postfix_cal_list[i] == '+':                    # + 연산자의 경우
                stack[top-1] = stack[top-1] + stack[top]        # top-1의 값에 top의 값을 더해줌
                top -=1                                         # 연산 후 top을 한칸 내려준다.
            elif postfix_cal_list[i] == '-':                    # - 연산자의 경우
                stack[top-1] = stack[top-1] - stack[top]        # top-1의 값에 top의 값으로 빼줌
                top -=1                                         # 연산 후 top을 한칸 내려준다.
    return stack[top]


T = 10
for testcase in range(1, T+1):
    # 입력받기
    N = int(input())
    infix_cal = input()                                         # 중위표기법 연산식을 입력받음
    postfix_cal_list = infix_postfix(infix_cal)                 # 중위표기법에서 후위표기법으로 저장된 리스트
    answer = postfix_cal(postfix_cal_list)                      # 후위표기법 연산 완료
    print(f'#{testcase} {answer}')                              # 출력값 출력