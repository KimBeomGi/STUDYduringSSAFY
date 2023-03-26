import sys
sys.stdin = open('2007 패턴 마디의 길이.txt','r')

T = int(input())
for testcase in range(1, T+1):
    problem = input()                       # 문제의 문자열 입력받기
    for i in range(1, 11):                  # 반복 문자열의 최대길이는 10이므로
        repeat = problem[0:i]               # 반복 문자열.
        if repeat == problem[i:i*2]:        # 반복 문자열이 맞다면
            answer = i                      # 반복 문자열의 길이는 i
            break                           # 더 찾을 필요 없으니 중단
    print(f'#{testcase} {answer}')          # 출력