'''
라이브강의에서 만든 스택
# 스택1
stack = [0]*3
top = -1

top += 1    # push(10)
stack[top] = 10

top += 1    # push(20)
stack[top] = 20

top += 1    # push(30)
stack[top] = 30

top -=1
print(stack[top+1])

top -=1
print(stack[top+1])

top -=1
print(stack[top+1])

top -=1             # 삭제되게 아니어서 스택의 맨 마지막 값을 다시 출력
print(stack[top+1])
'''

# 내가 푼거
# 연습문제2
'(asdf(aa)adsf'
s = input()
# for i in range(len(s)):
# stack만들기

stack_training = [0]*100
top = -1

for i in range(len(s)):
    if s[i] == '(':
        top += 1
        stack_training[top] = s[i]
    elif s[i] == ')':
        top -= 1
        if top < -1:
            raise IndexError(("')'가 많다!"))
# if top < -1:
#     raise IndexError("')'가 많다!")
if top > -1:
    raise IndexError("'('가 많다!")
else:
    print('정상입니다.')



'''
#  교수님이 푸는 방법
# stack
# 여는 괄호는  stack에 넣어주기
# 닫는 괄호를 만나면 

# 연습문제2
'(asdf(aa)adsf)'
data = input()

def check_bracket(data):
    stack = []

    for c in data:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:       # 무슨 뜻?? 비어있으면. 자연스러운 True와 False를 이용할 줄 알아야지
                return False    # 짝 안맞음
            stack.pop()
    # 반복문이 끝났을 때, 괄호 짝이 맞았으면 스택이 비어있을 것.
    if stack:       # 비어 있지 않으면
        return False
    # 괄호가 남지 않았다. 괄호 짝이 맞았다.
    return True

result = check_bracket(data)
print(result)
'''