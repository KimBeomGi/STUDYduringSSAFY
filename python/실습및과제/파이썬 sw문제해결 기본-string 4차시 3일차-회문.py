# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다. 
# 예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('파이썬 sw문제해결 기본-string 4차시 3일차-회문.txt', 'r')

# [문제풀이]
# 0. 가로에서도 찾아보고
# 1. 세로에서도 찾아보고
# 2. 회문은 1개만 존재하니까 찾으면 break
# 3. N by N 행렬임

def tenet(matrix, N, M):
    # 가로 확인
    for row in range(N):                                # 행 N개를 확인
        for column in range(N-M+1):                     # 열은 [0]~ [N-M] 까지 확인 가능
            for i in range((M//2)+1):                   # 확인하는 것은 반절만 확인하면 되니까 데칼코마니처럼
                if matrix[row][column+i] != matrix[row][(column+M-1)-i]:    # 각 끝마다 확인하면서 다르면
                    break                               # 더 확인하지 말고 멈추기
            else:                                       # 확인했는데 break가 안나면
                return (row,column, 'horizontal')       # 시작 위치를 출력

    # 세로 확인
    for column in range(N):                             # 열 N개를 확인
        for row in range(N-M+1):                        # 행은 [0]~ [N-M] 까지 확인 가능
            for i in range((M//2)+1):                   # 확인하는 것은 반절만 확인하면 되니까 데칼코마니처럼
                if matrix[row+i][column] != matrix[(row+M-1)-i][column]:    # 각 끝마다 확인하면서 다르면
                    break                               # 더 확인하지 말고 멈추기
            else:                                       # 확인했는데 break가 안나면
                return (row,column, 'vertical')         # 시작 위치를 출력
            
T = int(input())
for testcase in range(1,T+1):
    N, M = map(int, input().split())                    # 행렬의 크기 N, 회문의 길이 M을 입력받음
    matrix = [list(input()) for _ in range(N)]          # 확인하기 위한 행렬 만들기

    position = tenet(matrix, N, M)                      # 회문 함수입력해 position에 입력받고
    if position[2] == 'horizontal':                     # 가로에 회문이 있으면
        print(f'#{testcase}', end = ' ')                # 우선 테스트케이스 출력하고
        for i in range(position[1], position[1]+M):     # 시작점부터 길이만큼
            print(f'{matrix[position[0]][i]}', end = '')# 출력하기
        print()                                         # 이건 다음 테스트케이스를 진행하기 위한 출력값
    elif position[2] == 'vertical':                     # 세로에 회문이 있으면
        print(f'#{testcase}', end = ' ')                # 우선 테스트케이스 출력하고
        for i in range(position[0], position[0]+M):     # 시작점부터 길이만큼
            print(f'{matrix[i][position[1]]}', end = '')# 출력하기
        print()                                         # 이건 다음 테스트케이스를 진행하기 위한 출력값