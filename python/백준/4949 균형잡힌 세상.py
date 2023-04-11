# # pop. append를 이용한 스택을 써보자
# # import sys


string = input().rstrip()
while string:
    stack = []
    if len(string) == 1 and string[0] == '.':
        break
    for i in range(len(string)):
        # 대괄호 일 때
        if string[i] == '[':
            stack.append('[')
        elif string[i] == ']':
            if not stack:
                answer = 'no'
                break
            elif stack[-1] != '[':
                answer = 'no'
                break
            else:
                stack.pop()
        # 소괄호일 때
        elif string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            if not stack:         # 열린 소괄호가 없으면
                answer = 'no'
                break
            elif stack[-1] != '(':
                answer = 'no'
                break
            else:
                stack.pop()
    else:
        answer = 'yes'
    if stack:
        answer = 'no'
    print(answer)
    
    # print('---------------------------')
    string = input().rstrip()


#####################
# 어떤이가 작성해준 것. 나보다 시간 짧음
import sys

target = ['[', ']', '(', ')']

while True:
    input = sys.stdin.readline
    line = list(map(str, input()))
    if len(line) == 2 and line[0] == '.' and line[1] == '\n':
        break
    ans = "yes"
    stack = []
    for i in range(len(line)):
        if line[i] == target[0]: # [
            stack.append(0)
        elif line[i] == target[1]: # ]
            if len(stack) == 0:
                stack.append(1)
                # ans = "no"
                break
            if stack[-1] == 0:
                stack.pop()
            else:
                stack.append(1)
                # ans = "no"
                break
        elif line[i] == target[2]:# (
            stack.append(2)
        elif line[i] == target[3]:# )
            if len(stack) == 0:
                # ans = "no"
                stack.append(3)
                break
            if stack[-1] == 2:
                stack.pop()
            else:
                # ans = "no"
                stack.append(3)
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
    # print(ans)