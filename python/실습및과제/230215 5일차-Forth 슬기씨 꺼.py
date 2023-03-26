import sys
sys.stdin = open('230215 5일차-Forth.txt', 'r')

T = int(input())                                    # 테스트케이스 받음

for testcase in range(1, T+1):
    calculation = list(input(). split())            # 입력값 받음
    stack = []                                      # 스택 활용 위한 리스트
    operator = ['*', '/', '+', '-', '.']            # 연산자.
    cal_len = len(calculation)                      # 입력받은 값의 길이
    for i in range(cal_len):                        # calculation의 길이만큼 반복
        if calculation[i] not in operator:          # 연산자가 아니면
            stack.append(int(calculation[i]))       # stack에 추가하기
        
        else:                                       # 연산자일 경우
            if calculation[i] == '.':               # . 이면
                if len(stack) != 1:                 # stack의 길이가 1이 아닌지 확인하고
                    result = 'error'                # 1이 아니라면 에러를 출력(값이 1개만 남아야함)
                    break
                else:
                    result = stack[-1]              # stack의 길이가 1이면 결과는 stack[-1]
                    break
            elif len(stack) < 2:                    # 스택의 길이가 2보더 적으며느 결과를 error로 받고, 반복문 멈춤
                result = 'error'
                break
            
            elif calculation[i] == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                ans = b + a
                stack.append(ans)

            elif calculation[i] == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                ans = b-a
                stack.append(ans)

            elif calculation[i] == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                ans = b*a
                stack.append(ans)

            elif calculation[i] == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                ans = b//a
                stack.append(ans)
    print(f'#{testcase} {result}')
