# [문제]
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
sys.stdin = open('230209 4861. 3일차 - 회문.txt', "r")

# [문제풀이]
# 0. N은 글자수이자 줄수, 그러니까 N by N행이 출력된다. 그리고 M인 회문을 찾아 출력하면된다.
# 0-1. 길이가 10인데 M= 7이면 인덱스[0] [1] [2] [3] 에서 각각 찾을 수 있다.
# 1. 회문을 보면서 세로로보는 방법과 가로로 보는 방법에 대해서 확인이 필요하다.
# 1-1. 가로로 본다면 리스트[고정][변화], 세로로 본다면 [변화][고정]으로 보면 되겠다.
# 2. 회문이 행렬의 길이보다 짧다면 그 처음과 끝을 비교할 수 있는 인덱스의 값을 정밀하게 고려하고 작성
# 3. 가로와 세로는 행과 열의 위치 인덱스만 바꿔주면 됨

T = int(input())
for testcase in range(1, T+1):                                      # 테스트케이스만큼 반복
    N, M = map(int, input().split())                                # 행렬의 각 길이N, 회문으로 이용할 길이 M을 입력받음
    matrix = [list(map(str,input())) for _ in range(N)]
    # N만큼의 행을 입력받으며 이를 리스트화해서 리스트에 넣음으로 행렬을 만듬
    # 가로로 확인
    for row1 in range(N):                                           # 행으로 0 ~ N-1 만큼의 인덱스를 받을 예정
        for column1 in range(N-M+1):                                # 열로 0 ~ N-M 만큼의 인덱스를 받을 예정 N=10 M=7 이면 0~3 까지만
            a = column1                                             # 구간 내에서 이용하기 위해 a변수에 column인자를 할당
            isnot_cir_let1 = 0                                      # 회문 여부를 확인하기 위함(회문이면 0 아니면 1)
            while a < ((M+column1)//2):                             # 각 행에서 주어진 M만큼의 공간안에서 비교하기 위함. 시작이 [7]인데 길이가 13 이면 중간인 9까지만 검사하므로 7+13//2 인 10보다 작을 때 실행
                # 증가하는 a가 M의 반쪽까지만 작동하게 만듬
                if matrix[row1][a] == matrix[row1][(M-1)+column1-(a-column1)]:  # 끝과 끝이 같다면
                    a += 1                                          # 다음을 확인하러 가자
                elif matrix[row1][a] != matrix[row1][(M-1)+column1-(a-column1)]:# 끝과 끝이 같다면
                    isnot_cir_let1 = 1                              # 회문여부를 확인하는 isnot_cir_let을 1로 만들고 퇴장
                    break

            if isnot_cir_let1 == 0:                                 # 검사한 것이 회문이라면
                cir_let_list = []                                   # 회문을 만들어내기위한 cir_let리스트
                for i in range(M):                                  # 0~ M-1까지 i인자를 통한 반복문으로
                    cir_let_list.append(matrix[row1][column1+i])    # 현재 위치의 단어부터 총 M개의 단어를 입력
                cir_let = ''.join(cir_let_list)                     # 리스트로 받은 문자들을 문자열로 전환
                print(f'#{testcase} {cir_let}')                     # 출력값 출력
                break
    
    # 세로로 확인(작동 확인)
    for column2 in range(N):                                        # 열로 0 ~ N-1 만큼의 인덱스를 받을 예정
        for row2 in range(N-M+1):                                   # 행으로 0 ~ N-M 만큼의 인덱스를 받을 예정 N=10 M=7 이면 0~3 까지만
            b = row2                                                # 구간 내에서 이용하기 위해 b변수에 row인자를 할당
            isnot_cir_let2 = 0                                      # 회문 여부를 확인하기 위함(회문이면 0 아니면 1)
            while b < ((M+row2)//2):                                # 각 열에서 주어진 M만큼의 공간안에서 비교하기 위함. 시작이 [7]인데 길이가 13 이면 중간인 9까지만 검사하므로 7+13//2 인 10보다 작을 때 실행
                if matrix[b][column2] == matrix[(M-1)+row2-(b-row2)][column2]:  # 끝과 끝이 같다면
                    b += 1                                          # 다음을 확인하러 가자
                elif matrix[b][column2] != matrix[(M-1)+row2-(b-row2)][column2]:# 끝과 끝이 같다면
                    isnot_cir_let2 =1                               # 회문여부를 확인하는 isnot_cir_let을 1로 만들고 퇴장
                    break

            if isnot_cir_let2 == 0:                                 # 검사한 것이 회문이라면
                cir_let_list = []                                   # 회문을 만들어내기위한 cir_let리스트
                for i in range(M):                                  # 0~ M-1까지 i인자를 통한 반복문으로
                    cir_let_list.append(matrix[row2+i][column2])    # 현재 위치의 단어부터 총 M개의 단어를 입력
                cir_let = ''.join(cir_let_list)                     # 리스트로 받은 문자들을 문자열로 전환
                print(f'#{testcase} {cir_let}')                     # 출력값 출력
                break