import sys
sys.stdin = open('230216 6일차-계산기2.txt', 'r')

# 1. 후위 표기식으로 바꾸기
# 1-1. 토큰을 읽으면서 숫자라면 출력, 연산자라면 stack에 저장
# 1-2. 단 우선 순위가 높은 연산자가 먼저 나와야하니까 위에 있어야함.
# 1-2-1.그래서 우선순위가 낮은 연산자라면, 우선 순위 높은 연산자를 먼저 빼고, 스택에 push

T= 10
for testcase in range(1, T+1):
    N = int(input())
    data = list(input())                # 이래도 문자의 하나하나인덱스가 리스트 하나인덱스로 하나하나 들어가줌
    # 후위표기식으로 바꾸고
    postfix = ''
    stack = []
    for i in range(N):
        if data[i] in '0123456789':
            postfix += data[i]
        # 연산자
        else:
            if data[i] == '*':
                if not stack:
                    stack.append(data[i])
                else:
                    if stack[-1] == '+':
                        stack.append(data[i])
                    else:
                        postfix += stack.pop()
                        stack.append(data[i])
                    # 곱하기라면 stack에 push
                    # 더하기라면 다빼고 넣기
            else:   # 토큰이 '+'일대
                # 비어있으면 그냥 넣기
                # 아니라면, 다 빼고 넣기
                if not stack:
                    stack.append(data[i])
                # 아니라면, 다빼고 넣기
                else:
                    while stack:
                        postfix += stack.pop()
                    stack.append(data[i])
    # 연산하기
    while stack:
        postfix += stack.pop()
    # print(postfix)
    # 연산하기
    # 연산자가 나오면 피연산자 2개 빼서 연산해서 다시 스택에 넣기
    # 피연산자는 스택에 넣기
    stack = []
    for i in range(N):
        if postfix[i] in '0123456789':
            # 연산해야되니 숫자로 바꿔서 넣어주기
            stack.append(int(postfix[i]))
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            if postfix[i] == '*':
                stack.append(n1*n2)
            else:
                stack.append(n1+n2)
    print(f'{testcase} {stack[-1]}')
            
