# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 
# 10 1 9 2 8 3 7 4 6 5
 
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100
 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.


import sys
sys.stdin = open('파이썬 sw문제해결 기본-list2 8차시 2일차-특별한정렬.txt', 'r')
#[문제풀이]


T = int(input())
for testcase in range(1, T+1):
    N = int(input())                                        # 정수의 개수
    initial_list = list(map(int, input().split()))          # 처음 한 줄을 입력 받음
    
    for i in range(N-1):
        for j in range(N-1):
            if initial_list[j] < initial_list[j+1]:
                initial_list[j], initial_list[j+1] = initial_list[j+1], initial_list[j]
    print(f'#{testcase}', end = ' ')
    for i in range(5):
        print(f'{initial_list[i]}', end =' ')
        print(f'{initial_list[-(i+1)]}', end =' ')
    print()
