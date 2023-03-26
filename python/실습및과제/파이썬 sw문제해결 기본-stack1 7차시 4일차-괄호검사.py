import sys
sys.stdin = open('파이썬 sw문제해결 기본-stack1 7차시 4일차-괄호검사.txt', 'r')

T = int(input())
for testcase in range(1, T+1):
    string = input()                    # 문자열 그대로 입력받음
    A = len(string)                     # 문자열의 길이를 A로 받음
    stack = [0]*(A)                     # string의 크기만큼 stack 만들기
    top = -1                            # stack에서 사용될 top 변수 할당
    for i in range(A):                  # 0~ A-1만큽 반복
        if top < -1:
            print(f'#{testcase} {0}')
            break
        if string[i] == '(':            # 열린 소괄호를 만나면
            top += 1
            stack[top] = '('            # stack[top]에 소괄호 작성
        elif string[i] == '{':          # 열린 중괄호를 만나면
            top += 1
            stack[top] = '{'            # stack[top]에 중괄호 작성
        elif string[i] == ')':
            if stack[top] == '(':
                top -=1
            else:
                print(f'#{testcase} {0}')
                break
        elif string[i] == '}':
            if stack[top] == '{':
                top -=1
            else:
                print(f'#{testcase} {0}')
                break
    else:
        print(f'#{testcase} {1}')