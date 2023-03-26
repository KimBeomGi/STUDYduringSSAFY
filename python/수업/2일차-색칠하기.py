# [문제]
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

# [문제풀이]
# 0. 주어지는 문제는 행렬 문제이며, 빨간색과 파란색의 영역이 겹치는 부분의 영역 갯수를 구하는 문제이다.
# 0-1. 우선 행렬을 이용할 수 있도록 입력값을 리스트화(행렬화) 하는 것이 필요하다.
# 1. 어디서부터 어디까지 활용해야하는지를 우선적으로 알아야한다.
# 2. 활용 위치를 알았다면 각 행별 반복문을 돌리면서 좌측부터 우측으로 한칸씩 영역을 색칠해나간다.
# 2-1. 이때 for문을 이용해 color_area_column인 열을 먼저 돌리고, 이후 color_area_row인 행을 한 칸씩 옮기면서 색칠한다.
# 3. 이후 각 빨간색과 파란색이 색칠된 영역을 확인하고, 중복되는 값은 계산의 편이를 위해 set으로 제거한다.
# 3-1. set으로 중복값 제거 후 다시 리스트화 하여 빨간색과 파란색의 영역이 겹치는 것이 있는지 for 문을 이용해 확인한다.


T= int(input())

for testcase in range(1,T+1):
    N = int(input())                                                                # 색 영역 N개
    colors_area = [list(map(int,input().split())) for _ in range(N)]                # 각 색의 영역을 펼칠 수 있는 초안.
    area1 = []                                                                      # 빨간색의 영역을 담을 리스트
    area2 = []                                                                      # 파란색의 영역을 담을 리스트
    for color_area in colors_area:                                                  # 각 색 영역
        # now_dr = color_area[0]                                                      # 현재 타일 위치(x,y) x값
        # now_dc = color_area[1]                                                      # 현재 타일 위치(x,y) y값
        for color_area_column in range(color_area[1], color_area[3]+1):             # 각 행별로 영역을 색칠하기 위함 따라서 color_area의 좌측상단 모서리 (x,y)의 y부터 시작
            for color_area_row in range(color_area[0], color_area[2]+1):            # 현재 위치에서 오른쪽으로 +1 칸씩 영역을 표시할 것임.
                if color_area[4] == 1:                                              # 빨간색이면
                    now_dr = color_area_row                                         # 그리고 현재 위치의 x값은 color_area_row
                    now_dc = color_area_column                                      # 그리고 현재 위치의 y값은 color_area_column
                    area1.append((now_dr, now_dc))                                  # 현재위치를 튜플로 (now_dr,now_dc)화 해서 추가해라
                if color_area[4] == 2:                                              # 파란색이면
                    now_dr = color_area_row                                         # 그리고 현재 위치의 x값은 color_area_row
                    now_dc = color_area_column                                      # 그리고 현재 위치의 y값은 color_area_column
                    area2.append((now_dr, now_dc))                                  # 현재위치를 튜플로 (now_dr,now_dc)화 해서 추가해라
    area1 = set(area1)                                                              # area1(빨간색)영역의 중복을 방지하기 위해 set화
    area2 = set(area2)                                                              # area2(파란색)영역의 중복을 방지하기 위해 set화
    area1 = list(area1)                                                             # area1(빨간색)영역을 이용하기 위해 다시 리스트화
    area2 = list(area2)                                                             # area2(파란색)영역을 이용하기 위해 다시 리스트화
    cross_area = 0                                                                  # 빨간색과 파란색이 겹치는 영역을 확인하기 위해 변수 할당 최초값은 0
    for red in area1:                                                               # 빨간색의 영역을 인자로 하여서
        if red in area2:                                                            # 파란색의 영역안에 빨간색영역이 들어가있다면
            cross_area += 1                                                         # 겹치는 영역으로 1 추가해라.
    print(f'#{testcase} {cross_area}')                                              # 출력값을 출력


# # [하음씨 풀이법]
# T = int(input())
# for testcase in range(1, T+1):
#     paper = [[0]*10 for _ in range(10)]                     # 총 가로세로 10칸 10칸이니까
#     N = int(input())                                        # 영역의 갯수 N개
#     count = 0                                               # 겹치는 영역 세기

#     for _ in range(N):                                      # N개를 하나씩 분해.
#         x1, y1, x2, y2, c = map(int, input().split())       # 좌측 상단, 우측 하단의 xy값과 색깔 c 의 값을 할당
#         for e in range(x1, x2+1):                           # x1, x2까지의 열마다 진행
#             for k in range(y1, y2+1):                       # y1~ y2까지 칸마다 색칠 진행
#                 paper[e][k] += 1                            # paper 행렬에서 e열의 k 행에 색칠
    
#     for i in paper:                                         # paper 행렬에서 각 행마다
#         for j in i:                                         # j를 꺼내는데
#             if j ==2:                                       # j가 2라면(색이 2번 칠해졌다면)
#                 count += 1                                  # 겹쳐진 색 영역에 +1 하기
#     print(f'#{testcase} {count}')                           # 출력