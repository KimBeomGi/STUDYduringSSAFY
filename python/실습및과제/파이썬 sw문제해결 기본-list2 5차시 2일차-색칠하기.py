# 그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
# 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
# 예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
# 2
# 2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
# 3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
# 다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
# color = 1 (빨강), color = 2 (파랑)
 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('파이썬 sw문제해결 기본-list2 5차시 2일차-색칠하기.txt', 'r')


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    matrix = [[0]*10 for _ in range(10)]
    colors = [list(map(int, input().split())) for _ in range(N)]            # 리스트 안에 N만큼 리스트를 생성 [[],[],[],,,]

    purple = 0
    # 행별로 작동하면서 빈 공간에 컬러추가하기
    # 추가로 남의 색 있으면 겹침 표기하기
    for color in colors:          # 각 컬러별 작동 실시.
        for row in range(color[1], color[3]+1):                             # 행은 (x,y) 중 y값
            for column in range(color[0], color[2]+1):                      # 행은 (x,y) 중 x값
                if matrix[row][column] == 0:                                # 색을 칠하려는 공간이 빈 공간이면 색칠하기
                    matrix[row][column] = color[4]
                elif matrix[row][column] != color[4]:                       # 색을 칠하려는 공간이 0이 아닌데, 내가 칠할 색도 아니면?
                    matrix[row][column] = 3                                 # 겹치는 색인 보라색으로 칠하기
                    purple += 1
    # 이제 3이 칠해진 공간은 보라색 이므로 보라색의 수를 출력
    print(f'#{testcase} {purple}')