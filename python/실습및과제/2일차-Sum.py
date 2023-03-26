# [문제]
# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
# 다음과 같은 5X5 배열에서 최댓값은 29이다.

# [제약 사항]
# 총 10개의 테스트 케이스가 주어진다.
# 배열의 크기는 100X100으로 동일하다.
# 각 행의 합은 integer 범위를 넘어가지 않는다.
# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
# [입력]
# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

# [문제풀이]
# 0. 행열에서 각 행 또는 열, 또는 대각선의 합을 구하고 그 중 가장 큰 값을 출력하는 문제이다.
# 0-1. 배열이 100×100 이므로 각 행 또는 열 또는 대각선은 100개의 값을 합하게 된다.
# 0-2. 동일한 최댓값이 여러개여도 하나만 출력하면 되므로, max를 구해도 되지만, 추가로 리스트에 넣고 set으로 중복 제거 후 출력하는 방법도 있을 듯하다.
# 1. 각 행별로 리스트화해서 전체 행렬에 입력
# 2. 총 4가지 방법의 sum을 이용함(실제로 sum을 이용하진 않음)
# 2-1. 각 행 별로 sum(행렬 리스트 안의 각 리스트를 sum)
# 2-2. 각 열 별로 sum(행렬 리스트 안의 각 리스트[i]를 모두 더하기)
# 2-3. 좌상우하의 sum(리스트[0][0]+리스트[1][1]+리스트[2][2]+...+리스트[99][99])
# 2-4. 우상좌하의 sum(리스트[0][100-1]+리스트[1][100-2]+리스트[2][100-3]+...+리스트[99][100-100])
# 3. 2.에서 구한 각 값들을 한 리스트에 모아놓은 뒤 max값을 구한다.
# 4. 3.에서 구한 max 값을 출력한다.

import sys
sys.stdin = open('2일차_sum_input.txt', "r")

T= 10
for testcase in range(1,T+1):                                           # 테스트 케이스
    testcase = int(input())                                             # 입력값 처음에 테스트 케이스가 적혀있으므로 받아야함.
    A_matrix = []                                                       # 테스트 케이스에 쓰일 행렬
    for _ in range(100):                                                # 100 by 100의 행렬이므로 100번 받아야 되어서
        A_matrix.append(list(map(int,input().split())))                 # 테스트 케이스에 쓰일 행렬당 들어갈 입력값을 A_matrix에 리스트화해서 추가
    # 이건 A_matrix = [[1,2,3,4...], [1,2,3,4...], [1,2,3,4...], [1,2,3,4...], [1,2,3,4...], ....]의 형식임
    all_sum_value = []
    for row in A_matrix:                                                # A_matrix리스트안의 리스트를 row 인자로 반복문 실행 2-1. 각 행별로 sum을 하기 위함
        row_sum = 0                                                     # 각 행의 sum을 위해 이용될 row_sum
        for i in row:                                                   # 각 행의 sum
            row_sum += i                                                # 각 행의 인자 i를 더함
        all_sum_value.append(row_sum)                                   # 각 행의 sum값을 모든 행 열 대각선의 합 리스트에 추가.
    
    for row in range(100):                                              # 0~99를 이용해서 각 열의 합을 도출해낼 것임 리스트[column][row]
        column_sum = 0                                                  # 각 열의 sum을 위해 이용될 column_sum
        for column in range(100):                                       # 각 열의 동일한 행 위치를 돌아가기 위함 예) a[1][0] + a[2][0] + a[3][0]
            column_sum += A_matrix[column][row]                         # 각 열의 인자를 sum 하기    
        all_sum_value.append(column_sum)                                # 각 열의 sum값을 모든 행 열 대각선의 합 리스트에 추가.

    right_down_sum = 0                                                  # 좌상우하 대각선의 sum을 위해 이용될 right_down_sum
    for i in range(100):                                                # 좌상우하 대각선의 합을 구하기 위한 반복문
        right_down_sum += A_matrix[i][i]                                # sum(리스트[0][0]+리스트[1][1]+리스트[2][2]+...+리스트[99][99])가 되어야 하므로.
    all_sum_value.append(right_down_sum)

    left_down_sum = 0                                                   # 우상좌하 대각선의 sum을 위해 이용될 left_down_sum
    for j in range(100):                                                # 우상좌하 대각선의 합을 구하기 위한 반복문
        left_down_sum += A_matrix[j][100-(j+1)]                         # sum(리스트[0][100-1]+리스트[1][100-2]+리스트[2][100-3]+...+리스트[99][100-100])가 되어야 하므로.
    all_sum_value.append(left_down_sum)

    max_sum_value = 0                                                   # 구한 합들 중 가장 큰 값을 구하기 위해서 max_sum_value 변수를 이용
    for sum_value in all_sum_value:                                     # 모든 합들 중 각 인자들을 하나씩 돌아가면서 확인
        if max_sum_value < sum_value:                                   # 현재의 max_sum_value가 인자로 나온 sum_value 보다 작으면
            max_sum_value = sum_value                                   # 인자로 나온 sum_value값을 max_sum_value로 대입
    print(f'#{testcase} {max_sum_value}')