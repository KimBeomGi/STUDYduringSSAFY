
import sys
sys.stdin = open('2일차_sum_input.txt', "r")

T = 10
for testcase in range(1,T+1):
    # integer의 범위를 넘어가지 않는다이므로 result = -21억 정도임
    result = -0xfffffff      # 최댓값을 담을 그릇
    # -0xfffffff 이러면 어마어마하게 작은 값이 된다.-268435455
    board = [list(map(int,input().split())) for _ in range(100)]
    # 100 *100 행렬의 합, 열의 합 구하기
    for i in range(100):    # 가로줄 이동
        # 열이동
        sum_row = 0
        for j in range(100):        # 한 행 순회
            sum_row += board[i][j]
        if sum_row > result:        # sum_row가 현재 sum최댓값 보다 크면 값 교체
            result = sum_row

    for i in range(100):    # 세로줄(열)이동
            sum_col = 0
            # 열이동
            for j in range(100):        # 한 열 순회
                sum_col += board[j][i]
            if sum_col > result:        # sum_col가 현재 sum최댓값 보다 크면 값 교체
                result = sum_col
    
    sum_dia1 = 0 # 대각선 좌표 x y값이 같을때
    sum_dia2 = 0 # 대각선 좌표 x y값을 더한값이 99일때(이 문제에서)
    for i in range(10):
        for j in range(100):
            if i == j:
                sum_dia1 += board[i][j]
            if i + j == 99:
                sum_dia2 += board[i][j]
    # result = max(result, sum_dia1, sum_dia2)  # 현재 최대 결과값인 result , 그리고 대각선 각 2개를 비교해 가장 큰값을 result에 넣어라
    
    # max_v = result                    # 최대값 구하는 방법 1
    # for e in (sum_dia1,sum_dia2):
    #     if e > result:
    #         result = e
    result = result if result > sum_dia1 else sum_dia1      # 최대값 구하는 방법 2
    result = result if result > sum_dia2 else sum_dia2

        





    print(f'{testcase} {result}')