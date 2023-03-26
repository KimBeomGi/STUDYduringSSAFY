# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
# 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
# print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('230213 4일차-괄호검사.txt', 'r')
# [문제풀이]
# 0. 소괄호와 중괄호가 제대로 짝을 이뤘는지 검사하는 문제이다.
# 0-1. 정상적으로 짝을 이룬 경우는 1을, 비정상적이면 0을 출력하도록 하면 된다.
# 1. 오늘 배운 stack을 이용해보도록 하자.
# 2. 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다.의 부분을 확인할 수 있도록
# 2-1. 하나의 stack을 만들어서 집어넣고 그 값이 서로 대칭되지 않으면 빼는 방식으로 가자.
# 2-2. 저것 하나만 해결되어도 stack을 2개 만들 필요가 없다.

T = int(input())
for testcase in range(1, T+1):
    string = input()
    
    # 소괄호 중괄호의 짝 검사 진행
    
    def bracket_check(string):
        stack = [0]*len(string)                    # 소괄호를 확인하기 위해 입력받는 문자열의 길이만큼의 리스트를 만들어 준다.
        top = -1
        for i in range(len(string)):                # string의 길이만큼 반복문을 돌리면서 확인할 것임
            if string[i] == '(':                    # '('를 만나게 되면
                top += 1                            # top에 1을 더하고
                stack[top] = string[i]              # stack[top] = '('를 집어넣기
            
            elif string[i] == '{':                  # '{'를 만나게 되면
                top += 1                            # top에 1을 더하고
                stack[top] = string[i]              # stack[top] = '{'를 집어넣기
            
            elif string[i] == ')':                  # ')'를 만나게 되면
                top -= 1                            # top에 1을 빼고
                if top < -1 or stack[top+1] == '{' : # 만약 '('보다 ')' 더 많다면 또는 ) 매칭이 '{'으로 뜨면
                    return f'#{testcase} 0'         # 반복문을 더 돌 필요 없으니 반복 중단
                
            
            elif string[i] == '}':                  # '}'를 만나게 되면
                top -= 1                            # top에 1을 빼고
                if top < -1 or stack[top+1] == '(':  # 만약 '{'보다 '}' 더 많다면 또는 } 매칭이 '('으로 뜨면
                    return f'#{testcase} 0'         # 반복문을 더 돌 필요 없으니 반복 중단
        # 출력하기
        if top < -1 or top > -1:                    # 소괄호가 비정상이면 비정상을 출력
            return f'#{testcase} 0'
        elif top == -1:                             # 모두 정상이면 정상을 출력
            return (f'#{testcase} 1')
    print(bracket_check(string))




'''
T = int(input())
for testcase in range(1, T+1):
    string = input()
    stack1 = [0]*len(string)                    # 소괄호를 확인하기 위해 입력받는 문자열의 길이만큼의 리스트를 만들어 준다.
    stack2 = [0]*len(string)                    # 중괄호를 확인하기 위해 입력받는 문자열의 길이만큼의 리스트를 만들어 준다.
    top1 = -1                                   # 소괄호에 대해 stack을 이용하기 위해 top1 변수를 생성
    top2 = -1                                   # 중괄호에 대해stack을 이용하기 위해 top2 변수를 생성
    
    # 소괄호 중괄호의 짝 검사 진행
    for i in range(len(string)):                # string의 길이만큼 반복문을 돌리면서 확인할 것임
        if string[i] == '(':                    # '('를 만나게 되면
            top1 += 1                           # top1에 1을 더하고
            stack1[top1] = string[i]            # stack1[top1] = '('를 집어넣기
        
        elif string[i] == '{':                  # '{'를 만나게 되면
            top2 += 1                           # top2에 1을 더하고
            stack2[top2] = string[i]            # stack2[top2] = '{'를 집어넣기
        
        elif string[i] == ')':                  # ')'를 만나게 되면
            top1 -= 1                           # top1에 1을 빼고
            if top1 < -1:                       # 만약 '('보다 ')' 더 많다면
                break                           # 반복문을 더 돌 필요 없으니 반복 중단
        
        elif string[i] == '}':                  # '}'를 만나게 되면
            top2 -= 1                           # top2에 1을 빼고
            if top2 < -1:                       # 만약 '{'보다 '}' 더 많다면
                break                           # 반복문을 더 돌 필요 없으니 반복 중단
    # 출력하기
    if top1 < -1 or top1 > -1:                  # 소괄호가 비정상이면 비정상을 출력
        print(f'#{testcase} 0')
    elif top2 < -1 or top2 > -1:                # 중괄호가 비정상이면 비정상을 출력
        print(f'#{testcase} 0')
    elif top1 == -1 and top2 == -1:             # 소괄호, 중괄호 모두 정상이면 정상을 출력
        print((f'#{testcase} 1'))
'''