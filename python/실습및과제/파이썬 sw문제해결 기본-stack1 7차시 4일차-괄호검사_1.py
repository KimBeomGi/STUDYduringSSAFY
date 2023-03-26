# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
# 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
# print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.
 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다

import sys
sys.stdin = open('파이썬 sw문제해결 기본-stack1 7차시 4일차-괄호검사.txt','r')

# [문제풀이]
# 0. 괄호가 제대로 짝을 이뤘는지 확인하는 문제이다.
# 1. '(' 가 있어야 ')' 도 작동을 하는 것을 인지하고
# 2. ')'이 먼저 나오면 이것은 잘 못된 것이니 그것 또한 알아 두면 되겠다.
# 3. 순서 또한 }이게 나오는데 (이것이 앞에 있으면 안된다.
# 4. 스택을 이용해보자.

T = int(input())
for testcase in range(1,T+1):
    problem = input()                   # 문제의 입력값 입력받음
    N = len(problem)                    # 문제의 길이
    stack = [0]*(N+1)                   # stack을 생성하는데 문제의 길이보다 1개 더 많이 생성(혹시 있을 오류 방지)
    top = -1                            # top을 이용해서 stack을 사용
    
    # for-else 문을 활용해보자
    for i in range(N):
        if problem[i] == '(':           # 열린 소괄호라면
            top += 1                    # 탑을 한칸 올리고
            stack[top] = problem[i]     # 해당 스택의 값을 problem[i]의 괄호를 넣는다.
        elif problem[i] =='{':          # 열린 중괄호라면
            top += 1                    # 탑을 한칸 올리고
            stack[top] = problem[i]     # 해당 스택의 값을 problem[i]의 괄호를 넣는다.
        elif 0 <= top and problem[i] == ')':        # 닫힌 소괄호라면
            if stack[top] == '(':                   # 현재 가리키는 stack[top]이 열린 소괄호면
                top -= 1                            # top을 한칸 내린다.
            else:                                   # 열린 소괄호가 있고 닫힌 소괄호를 만난게 아니면
                print(f'#{testcase} 0')             # 잘못되었음을 출력
                break
        elif 0 <= top and problem[i] == '}':        # 닫힌 중괄호라면
            if stack[top] == '{':                   # 현재 가리키는 stack[top]이 열린 중괄호면
                top -= 1                            # top을 한칸 내린다.
            else:                                   # 열린 중괄호가 있고 닫힌 중괄호를 만난게 아니면
                print(f'#{testcase} 0')             # 잘못되었음을 출력
                break
        elif top == -1 and problem[i] == ')' or problem[i] ==' }':  # top이 -1 즉 스택이 비었는데 닫힌 괄호를 만나면
            print(f'#{testcase} 0')             # 잘못되었음을 출력
            break
        if i == N-1 and -1 < top:               # 마지막 인덱스를 다 검사했는데도, stack에 열린괄호가 남아있으면
            print(f'#{testcase} 0')             # 잘못되었음을 출력
            break
    
    else:
        print(f'#{testcase} 1')