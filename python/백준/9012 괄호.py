# 문제
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

# 입력
# 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

# 출력
# 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

import sys

T = int(sys.stdin.readline().strip())
for testcase in range(1, T+1):              # 테스트케이스만큼 반복
    A = sys.stdin.readline().strip()        # 괄호들 입력받음
    stack = []                              # STACK생성
    asnwer = ''
    for i in range(len(A)):
        if A[i] == '(':                     # 열린 괄호라면?
            stack.append(A[i])              # stack에 추가해주기

        elif A[i] == ')':                   # 만약 닫힌 괄호라면?
            if stack:                       # stack에 값이 있으면
                stack.pop()                 # 마지막 stack의 값을 뺌(근데 '('이것만 들어있음)
            else:                           # stack에 값이 없으면
                answer = 'NO'               # answer = 'NO'로 생성
                break                       # 멈춰
    else:                                   # for-else문으로 break를 통해 나온게 아니면
        answer = 'YES'                      # answer = 'YES'로 생성

    if stack:                               # 다 확인했는데도 stack에 값이 있으면
        answer = 'NO'                       # answer = 'NO'로 생성
    
    print(answer)