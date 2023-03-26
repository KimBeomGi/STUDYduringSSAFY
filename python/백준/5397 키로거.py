# 문제
# 창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.

# 키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다. 

# 강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오. 강산이는 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한줄로 이루어져 있고, 강산이가 입력한 순서대로 길이가 L인 문자열이 주어진다. (1 ≤ L ≤ 1,000,000) 강산이가 백스페이스를 입력했다면, '-'가 주어진다. 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다. 화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다. 나머지 문자는 비밀번호의 일부이다. 물론, 나중에 백스페이스를 통해서 지울 수는 있다. 만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

# 출력
# 각 테스트 케이스에 대해서, 강산이의 비밀번호를 출력한다. 비밀번호의 길이는 항상 0보다 크다.


# [문제풀이]
# 0. 사용자가 키보드를 누른 명령을 모두 기록. 화살표나 백스페이스도 입력
# 0-1. 강산이가 비밀번호 창에서 입력한 키가 주어졌을때 비밀번호를 알아내시오.
# 0-2. 대문자 소문자, 숫자, 백스페이스, 화살표가 주어진다.
# 1. 길이가 L인 문자열이 주어진다.
# 1-1. 백스페이스는 '-'
# 1-2. 화살표의 입력은 < 또는 >가 주어진다. 각 왼쪽 오른쪽이며,
# 1-3. 커서의 위치를 움직일 수 있다면, 왼쪽 도는 오른쪽으로 1만큼 움직인다.
# 1-4. 나머지가 문자의 비밀번호이다
'''
T = int(input())                    # 테스트 케이스 입력받음
for testcase in range(T):           # 테스트 케이스 만큼 돌리기
    all_string = input()            # 문자열 입력받기 < - 포함한 녀석
    L = len(all_string)             # 문자열의 길이만큼 생성
    stack = [None]*(L+1)             # 스택을 이용하기 위해 stack 생성, 특수키는 입력값으로 없으므로.
    top = -1                        # 스택에 이용할 top 생성
    for i in range(L):
        # '<' 일 때
        if all_string[i] == '<':
            if top > -1:            # top이 -1보다 크다면
                top -= 1            # top에 -1 빼기
                stack.insert(top+1, '!')    # stack에 공간을 만들어줌으로서 값을 넣을 수 있게 해줌
            else:                   # top이 -1이면
                top = -1            # top을 -1로 고정
        # '>' 일 때
        elif all_string[i] == '>':  
            if top == L:            # top의 길이와 같다면
                top = L             # top을 길이 L로 고정
            elif stack[top+1] == None:   # top+1이 '!'라면?
                continue            # 더 갈 필요 없으니까 다른거 확인
            elif top < L:           # top이 stack의 길이보다 작다면
                top += 1
        # '-' 일 때
        elif all_string[i] == '-':  # 백스페이스라면
            stack[top] = None       # 해당 문자는 None으로 바꾸기
            if top > -1:
                top -= 1                # top -1 해주기
            elif top == -1:
                top = -1                # top -1 해주기
        else:                           # 비밀번호에 쓰이는 값들이라면
            top +=1                     # top을 올려주고
            stack[top] = all_string[i]  # stack[top]에 기입
    
    # 출력 단계
    for i in range(top+1):         # STACK의 값을 인자로 해서
        print(stack[i], end='')
    print()
'''

T = int(input())
for testcase in range(T):
    initial_pw = input()
    stack = []
    stack_temp =[]
    L = len(initial_pw)             # 문자열의 길이 L
    for i in range(L):              # L만큼 반복하면서 문자를 확인할 것임.
        # 왼쪽 화살표 <를 눌렀을 때는
        if initial_pw[i] == '<':
            if stack :                              # stack안에 값이 있으면
                stack_temp.append(stack.pop())      # stack의 마지막 값을 빼서 stack_temp에 추가하기
                pass
            elif not stack:                         # stack안에 값이 없으면
                continue                            # 할 거 없으니 지나가기.
        # 오른쪽 화살표 >를 눌렀을 때는
        elif initial_pw[i] == '>':
            if stack_temp:                          # stack_temp에 값이 있을 경우에는
                stack.append(stack_temp.pop())      # stack_temp의 마지막 값을 빼서 stack에 추가하기
            elif not stack_temp:                    # stack_temp 값이 False 즉, 비었으면
                continue                            # 할 거 없으니 지나가기.  
        # 백스페이스를 눌러 지웠으면
        elif initial_pw[i] == '-':
            if stack:                               # stack에 값이 있으면
                stack.pop()                         # stack의 마지막 값을 빼기
            elif not stack:                         # stack에 값이 없으면
                continue                            # 할 것 없으니 지나가기
        # 비밀번호에 쓰이는 숫자 문자면
        else:
            stack.append(initial_pw[i])             # stack에 값 집어넣기
    while stack_temp:                               # stack_temp 값이 혹 남아 있으면 이것도 출력해야하니까
        stack.append(stack_temp.pop())              # stack_temp의 마지막 값을 빼서 stack의 마지막에 집어넣어주기
    print(''.join(stack))