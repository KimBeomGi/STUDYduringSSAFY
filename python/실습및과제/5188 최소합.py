# 그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면,
# 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

# 그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다.
# 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('5188 최소합.txt', 'r')

# [문제풀이]
# 0. 행렬로 되어있고 (0,0) 에서부터 (N-1,N-1)까지 가야한다.
# 0-1. 가는 방법은 1,2,3,4,5 순으로 움직이게 된다.
# 1. 가능한 모든 경로에 대해 각 경로내 숫자를 합을 계산하고 그 중 최솟값은 찾아낸다.
# 2. 3<=N<=13 이며 수는 10 이하의 자연수 이다.
# 3. 재귀함수로 풀어보자.

def min_go(N, matrix, row, column, perm, sum_value):                    # 함수 제작
    sum_value += matrix[row][column]                                    # 가는 길의 값 더해주기
    # 델타 우 하
    dr = [0, 1]                                                         # 행 델타값
    dc = [1, 0]                                                         # 열 델타값
    
    if row == N-1 and column == N-1:                                    # 만약 끝지점에 다다랐으면
        perm.append(sum_value)                                          # 해당값을 리스트에 입력하고
        sum_value -= matrix[row][column]                                # 돌아가기전에 현재 위치의 값을 빼기
        return                                                          # 이전으로 돌아가기
    
    # 우
    if row+dr[0] < N and column+dc[0] < N:                              # 행렬의 범위를 안벗어날때만 작동
        min_go(N, matrix, row+dr[0], column+dc[0], perm, sum_value)     # 오른쪽으로 가보기
    # 하
    if row+dr[1] < N and column+dc[1] < N:                              # 행렬의 범위를 안벗어날때만 작동
        min_go(N, matrix, row+dr[1], column+dc[1], perm, sum_value)     # 아래쪽으로 가보기
    return perm                                                         # 행렬을 반환


T = int(input())
for testcase in range(1, T+1):                                      # 테스트 케이스 만큼 반복
    N = int(input())                                                # N 입력받기
    matrix = [list(map(int,input().split())) for _ in range(N)]     # N by N 행렬 만들기
    perm = []                                                       # 모든 경로의 값을 받을 perm 리스트
    min_go(N, matrix, 0, 0, perm, 0)                                # 함수를 통해 perm 값을 제출
    # print(perm)
    min_value = min(perm)                                           # 경로의 최소합을 min_value 변수에 대입
    # print(A)
    print(f'#{testcase} {min_value}')                               # 출력값 출력