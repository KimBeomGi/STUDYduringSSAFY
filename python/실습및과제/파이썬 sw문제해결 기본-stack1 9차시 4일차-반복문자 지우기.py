import sys
sys.stdin = open('파이썬 sw문제해결 기본-stack1 9차시 4일차-반복문자 지우기.txt','r')

# 문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
# 반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
# 다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다. 
# CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
# CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
# CAA 연속 문자 AA를 지운다.
# C 1글자가 남았으므로 1을 리턴한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
# 다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

# [출력]
# #과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

# [문제풀이]
# 0. 연속해서 반복하는 문자를 지운 뒤 남은 문자의 갯수를 세는 문제이다.
# 1. 스택으로 풀어보자

T = int(input())
for testcase in range(1,T+1):
    problem = list(input())                     # 문제를 입력받음
    N = len(problem)                            # problem의 길이 N
    stack = [0]*(N+1)                           # stack을 (N+1) 크기의 리스트로 생성 N+1은 오류 방지를 위함
    top = -1                                    # stack을 이용할 때 사용하기 위한 top을 생성

    for i in range(N):                          # problem의 길이만큼 반복
        top += 1                                # top을 한칸 올리고
        stack[top] = problem[i]                 # stack[top]에 problem의 문자를 입력
        if stack[top] == stack[top-1]:          # stack[top]을 stack[top-1]과 비교해보니 같다면(반복문자라면)
            top -= 2                            # top을 2칸 내림
    
    print(f'#{testcase} {top+1}')               # 출력값 출력. top+1을 출력하는 이유는 남은 문자의 갯수만 세아리면 되기 때문
                                                # top은 인덱스여서 +1 해줘야 갯수를 나타낼 수 있음