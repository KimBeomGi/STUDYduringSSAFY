# [문제풀이]
# 0. 오셀로는 보드판에 내 색이 더 많을 시 이기는 게임이다. 여기서는 흑돌과 백돌의 개수를 출력해야한다.
# 0-1. 예로 21110 이렇게 있을 때 21112로 두게 되면 22222로 바뀐다고 생각하면 된다.
# 0-2. 0에만 둘 수 있으며, 상대의 색을 바꾸려면 상대의 돌이 있는 양끝(행 또는 열 또는 대각선 끝)에 돌을 두게 될 시에 바뀐다.
# 1. 우선 N by N이므로 가로세로 N만큼의 행렬을 만든다. M을 이용해 턴으로 이용을 해준다.
# 2. 해당 문제의 예시를 보아하니 (0,0)이 왼쪽 상단이 아닌, (1,1)이 왼쪽 상단으로 가정한다.
# 2-1. a b 가 있다면 b가 행이고 a가 열이니 기억하면 되겠다.
# 2-2. 3 2 1 식으로 주어지는 입력값을 이용해 해당 값을 리스트[1][2] = 1로 만들어준다.
# 3. 가로세로 뿐 아니라 대각선까지 생각해야하므로 총 8개의 방향을 생각해야한다.
# 4. 각 방향인 8개의 델타값을 생성하고 for문을 이용해 델타값을 활용한다.


T = int(input())
for testcase in range(1,T+1):                                       # 입력값 만큼 반복
    N, M = map(int, input().split())                                # N by N 보드의 길이인 N과 돌을 놓을 총 횟수인 M을 입력받음.
    othello_board = [[0]*N for _ in range(N)]                       # [0]*N이 N개 들어있는 리스트를 만들어서 행렬, 즉 게임판을 만듬
    black = 2                                                       # 초기 세팅된 검은돌 2개
    white = 2                                                       # 초기 세팅된 흰돌 2개
    # 오셀로 게임 세팅
    initial_setting_position = int(N//2)-1
    othello_board[initial_setting_position+1][initial_setting_position] = 1        # 초기 세팅된 검은돌 위치
    othello_board[initial_setting_position][initial_setting_position+1] = 1        # 초기 세팅된 검은돌 위치
    othello_board[initial_setting_position][initial_setting_position] = 2          # 초기 세팅된 흰돌 위치
    othello_board[initial_setting_position+1][initial_setting_position+1] = 2      # 초기 세팅된 흰돌 위치
    
    # 이동에 사용될 델타변수
    # [좌, 우, 상, 하, 좌상, 우상, 좌하, 우하]
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]                                # 열(좌, 우, 상, 하, 좌상, 우상, 좌하, 우하)
    dy = [0, 0, -1, 1, -1, -1, 1, 1]                                # 행(좌, 우, 상, 하, 좌상, 우상, 좌하, 우하)
    # gameboard = [0,1,2,3,4,5, --- , N-3, N-2, N-1]

    # 오셀로 게임 시작
    for turn in range(M):                                           # M은 돌을 넣는 총 횟수이므로 즉, '턴'이 된다.
        x, y, color = map(int, input().split())                     # x,y값 그리고 색을 입력받음.
        x = x - 1                                                   # 주어지는 x값이 리스트[]의 인덱스로 따지면 1을 빼준 위치이기 때문
        y = y - 1                                                   # 주어지는 y값이 리스트[]의 인덱스로 따지면 1을 빼준 위치이기 때문
        othello_board[y][x] = color                                 # 해당 위치에 흑 또는 백의 돌을 둠.
        if color == 1:                                              # 1이면 검은색 +1
            black += 1
        elif color == 2:                                            # 2면 흰색 +1
            white += 1
        
        # 델타값을 이용해 색 변환 시작
        for delta in range(8):                                      # '탐색 및 색 변환 반복문', 델타를 이용해 좌우상하 좌상 우상 좌하 우하 8가지를 확인하기 위함.
            ser_x = x                                               # 델타이용 for문에서 사용할 검사좌표x
            ser_y = y                                               # 델타이용 for문에서 사용할 검사좌표y
            is_init_color =  0                                      # 선 상에 나와 같은 돌이 있는지 없는지를 확인하기 위한 변수 is_init
            
            while 0 <= ser_x < N and 0 <= ser_y <= N:               # '탐색 반복문', 찾는 좌표가 보드판 내에 있을 때 작동, 
                ser_x += dx[delta]                                  # 찾으려는 x좌표 값을 델타값을 이용해 찾으러 가기 위함
                ser_y += dy[delta]                                  # 찾으려는 y좌표 값을 델타값을 이용해 찾으러 가기 위함
                if 0 <= ser_x < N and 0 <= ser_y < N:
                    if othello_board[ser_y][ser_x] == 0:            # 탐색중에 0을 만나면 뒤집을 값이 없는 거니까 멈추기
                        break
                    elif othello_board[ser_y][ser_x] != color and othello_board[ser_y][ser_x] != 0:     # 탐색중에 상대방 돌의 색을 만나면
                        continue
                    elif othello_board[ser_y][ser_x] == color:                                          # 탐색중에 내 돌과 같음을 확인되면
                        is_init_color = 1                           # 선 상에 나와 같은 돌이 있음을 표기.
                        break                                       # 다음 행동을 하기 위해 탐색 반복문을 벗어남
            
            if is_init_color == 1:                                  # 탐색 중 내 돌과 같음을 확인했다면
                ser_x -= dx[delta]                                  # 마지막 탐색위치에서 돌을 놓은 위치까지 x를 변경하며 색변환 실시위함
                ser_y -= dy[delta]                                  # 마지막 탐색위치에서 돌을 놓은 위치까지 y를 변경하며 색변환 실시위함
                while 0 <= ser_x < N and 0 <= ser_y < N and othello_board[ser_y][ser_x] != color and othello_board[ser_y][ser_x] != 0:
                    # '색 변환 반복문' 상대방 돌의 색일 때 반복문 실행, 나랑 같은 색이 되면 넘어감. ser_x, ser_y가 보드판안에 있을때만 작동(오류 방지)
                    if othello_board[ser_y][ser_x] == 1:            # 흑돌이면 백돌로 변환
                        othello_board[ser_y][ser_x] = 2
                        black -= 1                                  # 흑돌수 -1
                        white += 1                                  # 백돌수 +1
                    elif othello_board[ser_y][ser_x] == 2:          # 백돌이면 흑돌로 변환
                        othello_board[ser_y][ser_x] = 1
                        black += 1                                  # 흑돌수 +1
                        white -= 1                                  # 백돌수 -1
                    ser_x -= dx[delta]                              # 다음 값 탐색 후 색 변환 하기 위함                                 
                    ser_y -= dy[delta]                              # 다음 값 탐색 후 색 변환 하기 위함
    print(f'#{testcase} {black} {white}')                           # 출력값 출력