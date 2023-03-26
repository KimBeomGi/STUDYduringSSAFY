# [문제]
# 오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.
# 보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).
# 4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.

# 그리고 흑, 백이 번갈아가며 돌을 놓는다.
# 처음엔 흑부터 시작하는데 이 때 흑이 돌을 놓을 수 있는 곳은 다음과 같이 4군데이다.

# 플레이어는 빈공간에 돌을 놓을 수 있다.
# 단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
# (여기에서 "사이"란 가로/세로/대각선을 의미한다.)
# (2, 3) 위치에 흑돌을 놓은 후의 보드는 다음과 같다.


# 이런 식으로 번갈아가며 흑, 백 플레이어가 돌을 놓는다.
# 만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.
# 보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.

#  [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.
# 그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.
# 돌의 색이 1이면 흑돌, 2이면 백돌이다.
# 만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.
# 돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.

#  [출력]
# 각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.
# 흑돌이 30개, 백돌이 34인 경우 30 34를 출력한다.

import sys
sys.stdin = open('230210 재미있는 오셀로 게임.txt', 'r')

# [문제풀이]
# 0. 오셀로는 보드판에 내 색이 더 많을 시 이기는 게임이다. 여기서는 흑돌과 백돌의 개수를 출력해야한다.
# 0-1. 예로 21110 이렇게 있을 때 21112로 두게 되면 22222로 바뀐다고 생각하면 된다.
# 0-2. 0에만 둘 수 있으며, 상대의 색을 바꾸려면 상대의 돌이 있는 양끝(행 또는 열 또는 대각선 끝)에 돌을 두게 될 시에 바뀐다.
# 1. 우선 N by N이므로 가로세로 N만큼의 행렬을 만든다. M을 이용해 턴으로 이용을 해준다.
# 2. 해당 문제의 예시를 보아하니 (0,0)이 왼쪽 상단이 아닌, (1,1)이 왼쪽 상단으로 가정한다.
# 2-1. a b 가 있다면 b가 행이고 a가 열이니 기억하면 되겠다.
# 2-2. 3 2 1 식으로 주어지는 입력값을 이용해 해당 값을 리스트[1][2] = 1로 만들어준다.

T = int(input())
for testcase in range(1,T+1):
    N, M = map(int, input().split())            # N by N 보드의 길이인 N과 돌을 놓을 총 횟수인 M을 입력받음.
    game_board = [[0]*N for _ in range(N)]      # [0]*N이 N개 들어있는 리스트를 만들어서 행렬, 즉 게임판을 만듬
    black = 2
    white = 2
    # 오셀로 게임 세팅
    initial_setting_position = int(N/2)-1
    game_board[initial_setting_position+1][initial_setting_position] = 1
    game_board[initial_setting_position][initial_setting_position+1] = 1
    game_board[initial_setting_position][initial_setting_position] = 2
    game_board[initial_setting_position+1][initial_setting_position+1] = 2

    # 오셀로 게임 시작
    for turn in range(M):                       # M은 돌을 넣는 총 횟수이므로 즉, '턴'이 된다.
        x, y, color = map(int, input().split()) # x,y값 그리고 색을 입력받음.
        game_board[y-1][x-1] = color            # 해당 위치에 흑 또는 백의 돌을 둠.
        if color == 1:                          # 1이면 검은색 +1
            black += 1
        elif color == 2:                        # 2면 흰색 +1
            white += 1
        
        # 오셀로 규칙인 돌 색 변환
        # 행, 즉 가로에서 있으면 변환
        # 놓은 위치 왼쪽
        for i in range(x-1-1, -1, -1):                                              # i를 인자로 해서 돌을 놓은 위치인 x-1의 왼쪽부터 왼쪽끝까지 오셀로판에서 확인
            if (game_board[y-1][i] != 0) and (game_board[y-1][i] != color):         # 놓은 돌 옆에 붙어있는 돌색이 놓은 돌 색이 아니라면
                continue
            elif game_board[y-1][i] == color and i != (x-2):                        # i가 놓은 위치 바로 옆이 아니고, 같은 돌 색이면
                for anothercolor in range(i+1, x-1):                                # [i+1] ~ [x-2]까지 다른 색 돌을 변환시키기 위한 반복문
                    game_board[y-1][anothercolor] = color                           # 다른 색 돌을 현재 돌 색으로 바꾼다.
                    if color == 1:                                                  # 현재 색이 1이면 흰색을 검은색으로!
                        black +=1                                                   # 검은색 돌은 +1
                        white -=1                                                   # 흰색 돌은 -1
                    elif color == 2:                                                # 현재 색이 2이면 검은색을 흰색으로!
                        white +=1                                                   # 흰색 돌은 +1
                        black -=1                                                   # 검은색 돌은 -1
            else:
                break
        
        # 놓은 위치 오른쪽
        for i in range(x-1+1, N):                                                   # i를 인자로 해서 돌을 놓은 위치인 x-1의 오른쪽부터 오른쪽끝까지 오셀로판에서 확인
            if (game_board[y-1][i] != 0) and (game_board[y-1][i] != color):         # 놓은돌 옆에 붙어있는 돌색이 놓은 돌색이 아니라면
                continue
            elif game_board[y-1][i] == color and i != x:                            # i가 놓은 위치 바로 옆이 아니고, 같은 돌 색이면
                for anothercolor in range(x-1+1, i):                                # [x] ~ [i-1]까지 다른 색 돌을 변환시키기 위한 반복문
                    game_board[y-1][anothercolor] = color                           # 다른 색 돌을 현재 돌 색으로 바꾼다.
                    if color == 1:                                                  # 현재 색이 1이면 흰색을 검은색으로!
                        black +=1                                                   # 검은색 돌은 +1
                        white -=1                                                   # 흰색 돌은 -1
                    elif color == 2:                                                # 현재 색이 2이면 검은색을 흰색으로!
                        white +=1                                                   # 흰색 돌은 +1
                        black -=1                                                   # 검은색 돌은 -1
            else:
                break
        
        # 열 , 즉 세로에서 있으면 변환
        # 놓은 위치 위쪽
        for i in range(y-1-1, -1, -1):                                              # i를 인자로 해서 돌을 놓은 위치인 y-1의 위쪽부터 위쪽끝까지 오셀로판에서 확인
            if (game_board[i][x-1] != 0) and (game_board[i][x-1] != color):         # 놓은 돌 위에 붙어있는 돌색이 놓은 돌 색이 아니라면
                continue
            elif game_board[i][x-1] == color and i != y-2:                          # i가 놓은 위치 바로 위가 아니고, 같은 돌 색이면
                for anothercolor in range(i+1, y-1):                                # [i+1] ~ [y-2]까지 다른 색 돌을 변환시키기 위한 반복문
                    game_board[anothercolor][x-1] = color                           # 다른 색 돌을 현재 돌 색으로 바꾼다.
                    if color == 1:                                                  # 현재 색이 1이면 흰색을 검은색으로!
                        black +=1                                                   # 검은색 돌은 +1
                        white -=1                                                   # 흰색 돌은 -1
                    elif color == 2:                                                # 현재 색이 2이면 검은색을 흰색으로!
                        white +=1                                                   # 흰색 돌은 +1
                        black -=1                                                   # 검은색 돌은 -1
            else:
                break
        
        # 놓은 위치 아래쪽
        for i in range(y-1+1, N):                                                   # i를 인자로 해서 돌을 놓은 위치인 x-1의 아래쪽부터 아래쪽끝까지 오셀로판에서 확인
            if (game_board[i][x-1] != 0) and (game_board[i][x-1] != color):         # 놓은돌 아래에 붙어있는 돌색이 놓은 돌색이 아니라면
                continue
            elif game_board[i][x-1] == color and i != y:                            # i가 놓은 위치 바로 아래가 아니고, 같은 돌 색이면
                for anothercolor in range(y-1+1, i):                                # [x] ~ [i-1]까지 다른 색 돌을 변환시키기 위한 반복문
                    game_board[anothercolor][x-1] = color                           # 다른 색 돌을 현재 돌 색으로 바꾼다.
                    if color == 1:                                                  # 현재 색이 1이면 흰색을 검은색으로!
                        black +=1                                                   # 검은색 돌은 +1
                        white -=1                                                   # 흰색 돌은 -1
                    elif color == 2:                                                # 현재 색이 2이면 검은색을 흰색으로!
                        white +=1                                                   # 흰색 돌은 +1
                        black -=1                                                   # 검은색 돌은 -1
            else:
                break

        # 놓은 위치 대각선 좌상
        # for i in range(x-1-1, -1, -1):
        #     for j in range(y-1-1, -1, -1):
        i= x-2
        j= y-2
        while 0 <= i < x-1 and 0 <= j <y-1:
            # 돌을 놓은 위치에서 좌상단으로 끝까지 확인
            if (game_board[j][i] != 0) and (game_board[j][i] != color):         # 놓은 돌 좌상에 붙어있는 돌색이 놓은 돌 색이 아니면
                i -= 1  # 좌측으로 가면서 확인하므로
                j -= 1  # 위로 가면서 확인하므로
                continue
            elif game_board[j][i] == color and i != (x-2) and j != (y-2):       # i, j가 놓은 위치 바로 좌상이 아니고, 같은 돌 색이면
                anothercolor1 = i+1                                             # while문에 쓰일 행에 해당하는 변수
                anothercolor2 = j+1                                             # while문에 쓰일 열에 해당하는 변수
                while i+1 <= anothercolor1 < x-1 and j+1 <= anothercolor2 < y-1:
                    game_board[anothercolor2][anothercolor1] = color            # 다른 색 돌을 현재 돌 색으로 바꾼다.
                    if color == 1:                                              # 현재 색이 1이면 흰색을 검은색으로!
                        black +=1                                               # 검은색 돌은 +1
                        white -=1                                               # 흰색 돌은 -1
                    elif color == 2:                                            # 현재 색이 2이면 검은색을 흰색으로!
                        white +=1                                               # 흰색 돌은 +1
                        black -=1                                               # 검은색 돌은 -1
                    anothercolor1 += 1
                    anothercolor2 += 1
                i -= 1  # 좌측으로가면서 확인하므로
                j -= 1  # 위로 가면서 확인하므로
            else:
                break

        # 놓은 위치 대각선 우상
        # for i in range(x-1+1, N):
        #     for j in range(y-1-1, -1, -1):
        i = x
        j = y-2
        while x <= i < N and 0 <= j < y-1:
            # 돌을 놓은 위치에서 우상단으로 끝까지 확인
            if (game_board[j][i] != 0) and (game_board[j][i] != color):         # 놓은 돌 옆에 붙어있는 돌색이 놓은 돌 색이 아니면
                i += 1  # 우측으로 가면서 확인하므로
                j -= 1  # 위로 가면서 확인하므로
                continue
            elif game_board[j][i] == color and i != x and j != (y-2):       # i가 놓은 위치 바로 옆이 아니고, 같은 돌 색이면
                anothercolor1 = x
                anothercolor2 = j+1
                while x <= anothercolor1 < i and j+1 <= anothercolor2 < y-1:
                    game_board[anothercolor2][anothercolor1] = color                       # 다른 색 돌을 현재 돌 색으로 바꾼다.
                    if color == 1:                                              # 현재 색이 1이면 흰색을 검은색으로!
                        black += 1                                               # 검은색 돌은 +1
                        white -= 1                                               # 흰색 돌은 -1
                    elif color == 2:                                            # 현재 색이 2이면 검은색을 흰색으로!
                        white += 1                                               # 흰색 돌은 +1
                        black -= 1                                               # 검은색 돌은 -1
                    anothercolor1 += 1
                    anothercolor2 += 1
                i += 1  # 우측으로 가면서 확인하므로
                j -= 1  # 위로 가면서 확인하므로
            else:
                break
        
        # 놓은 위치 대각선 좌하
        # for i in range(x-1-1, -1, -1):
        #     for j in range(y-1+1, N):
        i = x-2
        j = y
        while 0 <= i < x-1 and y <= j < N:
            # 돌을 놓은 위치에서 좌하단으로 끝까지 확인
            if (game_board[j][i] != 0) and (game_board[j][i] != color):         # 놓은 돌 옆에 붙어있는 돌색이 놓은 돌 색이 아니면
                i -= 1  # 좌측으로 가면서 확인하므로
                j += 1  # 아래로 가면서 확인하므로
                continue
            elif game_board[j][i] == color and i != (x-2) and j != y:       # i가 놓은 위치 바로 옆이 아니고, 같은 돌 색이면
                anothercolor1 = i+1
                anothercolor2 = y
                while i+1 <= anothercolor1 < x-1 and y <= anothercolor2 < j:
                    game_board[anothercolor2][anothercolor1] = color                       # 다른 색 돌을 현재 돌 색으로 바꾼다.
                    if color == 1:                                              # 현재 색이 1이면 흰색을 검은색으로!
                        black += 1                                               # 검은색 돌은 +1
                        white -= 1                                               # 흰색 돌은 -1
                    elif color == 2:                                            # 현재 색이 2이면 검은색을 흰색으로!
                        white += 1                                               # 흰색 돌은 +1
                        black -= 1                                               # 검은색 돌은 -1
                    anothercolor1 += 1
                    anothercolor2 += 1
                i -= 1  # 좌측으로 가면서 확인하므로
                j += 1  # 아래로 가면서 확인하므로
            else:
                break

        # 놓은 위치 대각선 우하 # 이상없음 확인완료
        # for i in range(x-1+1, N):
        #     for j in range(y-1+1, N):
        i = x
        j = y
        while x <= i < N and y <= j < N:
            # 돌을 놓은 위치에서 우하단으로 끝까지 확인
            if (game_board[j][i] != 0) and (game_board[j][i] != color):         # 놓은 돌 옆에 붙어있는 돌색이 놓은 돌 색이 아니면
                i += 1  # 우측으로 가면서 확인하므로
                j += 1  # 아래로 가면서 확인하므로
                continue
            elif game_board[j][i] == color and i != x and j != y:       # i가 놓은 위치 바로 옆이 아니고, 같은 돌 색이면
                anothercolor1 = x
                anothercolor2 = y
                while x <= anothercolor1 < i and y <= anothercolor2 < j:
                    game_board[anothercolor2][anothercolor1] = color                       # 다른 색 돌을 현재 돌 색으로 바꾼다.
                    if color == 1:                                              # 현재 색이 1이면 흰색을 검은색으로!
                        black += 1                                               # 검은색 돌은 +1
                        white -= 1                                               # 흰색 돌은 -1
                    elif color == 2:                                            # 현재 색이 2이면 검은색을 흰색으로!
                        white += 1                                               # 흰색 돌은 +1
                        black -= 1                                               # 검은색 돌은 -1
                    anothercolor1 += 1
                    anothercolor2 += 1
                i += 1  # 우측으로 가면서 확인하므로
                j += 1  # 아래로 가면서 확인하므로
            else:
                break

        # print(game_board)
    print(f'#{testcase} {black} {white}')

        # 열, 즉 세로에서 있으면 변환
'''
[[0, 0, 0, 0], 
[1, 1, 1, 0], 
[0, 1, 2, 0], 
[0, 0, 0, 0]]

[[2, 0, 0, 0], 
[1, 1, 1, 0], 
[0, 1, 2, 0], 
[0, 0, 0, 0]]

[[2, 0, 0, 0], 
[1, 1, 1, 0], 
[0, 1, 1, 1], 
[0, 0, 0, 0]]

[[2, 0, 0, 0], 
[1, 1, 1, 0], 
[0, 1, 1, 1], 
[0, 0, 0, 2]]

[[2, 1, 0, 0], 
[1, 1, 1, 0], 
[0, 1, 1, 1], 
[0, 0, 0, 2]]

[[2, 1, 0, 0], 
[1, 1, 1, 2], 
[0, 1, 1, 2], 
[0, 0, 0, 2]]

[[2, 1, 0, 0], 
[1, 1, 1, 2], 
[0, 1, 1, 2], 
[0, 0, 1, 2]]

[[2, 1, 0, 0], 
[2, 1, 1, 2], 
[2, 2, 2, 2], 
[0, 0, 1, 2]]

[[2, 1, 0, 0], 
[2, 1, 1, 2], 
[2, 1, 2, 2], 
[0, 1, 1, 2]]

[[2, 1, 0, 0], 
[2, 1, 1, 2], 
[2, 1, 2, 2], 
[2, 2, 2, 2]]

[[2, 1, 0, 2], 
[2, 1, 1, 2], 
[2, 1, 2, 2], 
[2, 2, 2, 2]]

[[2, 2, 2, 2], 
[2, 1, 2, 2], 
[2, 1, 2, 2], 
[2, 2, 2, 2]]

'''