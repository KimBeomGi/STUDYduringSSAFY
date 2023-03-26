

# [문제]
# N X N크기의 농장이 있다.
# 이 농장에는 이상한 규칙이 있다.
# 규칙은 다음과 같다.
#    ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
#    ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.

# 1 X 1크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.
# 3 X 3크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16 (3 + 2 + 5 + 4 + 2)이다.
# 5 X 5크기의 농장에서 자라는 농작물의 수확하여 얻을 수 있는 수익은 25 (3 + 2 + 1 + 1 + 2 + 5 + 1 + 1 + 3 + 3 + 2 + 1)이다.
# 농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.

# [제약 사항]
# 농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)
# 농작물의 가치는 0~5이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.

# [출력]
# 각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
sys.stdin = open('230303 농작물 수확하기.txt', 'r')
# [문제풀이]
# 0. N by N의 경작지에서 제일 가운데 부분이 가장  가장 넓게 분포되어있다.
# 0-1. 그 가운데를 중심으로 2칸씩 줄어들고. 마지막 행과 열은 가운데 1칸만이 수확이 가능하다.
# 1. 가운데 행을 기점으로 해서 위쪽으로 2칸씩 줄어들면서 합을하고
# 1-1. 가운데 행을 기점으로 해서 아래쪽으로 2칸씩 줄어들면서 합을해준다.
# 2. 가운데 열을 기준으로 -1 +1을 하면서 해볼까?

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]          # 경작지를 매트릭스화 하기
    middle = N//2                                               # 중앙값을 확인


    # 경작지 중앙
    harvest = 0
    for column in range(N):
        harvest += farm[middle][column]                         # 경작지 가운데 행 수확하기

    # 경작지 중앙 위
    area = 0
    for row in range(middle):                                   # 경작지 행
        harvest += farm[row][middle]
        if row != 0:
            for column_cnt in range(1, area+1):                 # 경작지 열 중앙과의 거리
                right = middle+column_cnt                       # 중앙열에서 오른쪽
                left = middle-column_cnt                        # 중앙열에서 왼쪽
                harvest += farm[row][right]                     # 중앙열에서 오른쪽 수확하기
                harvest += farm[row][left]                      # 중앙열에서 왼쪽 수확하기
        area += 1 

    # 경작지 중앙 아래
    area = 0
    for row in range(N-1, middle, -1):
        harvest += farm[row][middle]
        if row != N-1:
            for column_cnt in range(1, area+1):                 # 경작지 열 중앙과의 거리
                right = middle+column_cnt                       # 중앙열에서 오른쪽
                left = middle-column_cnt                        # 중앙열에서 왼쪽
                harvest += farm[row][right]                     # 중앙열에서 오른쪽 수확하기
                harvest += farm[row][left]                      # 중앙열에서 왼쪽 수확하기
        area += 1 
    
    print(f'#{testcase} {harvest}')