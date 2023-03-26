T = int(input())
 
for tc in range(1, T + 1):
    calculation = list(input().split())
    stack = []
    for i in calculation:
        if len(stack) <= 1 and i in '+-*/':
            OP = 'error'
            break
        elif i == '+':
            b, a = stack.pop(), stack.pop()
            stack.append(int(a) + int(b))
        elif i == '-':
            b, a = stack.pop(), stack.pop()
            stack.append(int(a) - int(b))
        elif i == '*':
            b, a = stack.pop(), stack.pop()
            stack.append(int(a) * int(b))
        elif i == '/':
            b, a = stack.pop(), stack.pop()
            stack.append(int(a) // int(b))
        elif i == '.':
            if len(stack) > 1:
                OP = 'error'
                break
            while stack:
                OP = str(stack.pop())
            break
        else:
            stack.append(i)
 
    print(f'#{tc} {OP}')