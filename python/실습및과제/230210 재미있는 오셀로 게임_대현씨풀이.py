# 게임시작시, 돌을 하나 둘때마다 콘솔에 게임판을 출력시켜서 확인하기 위한 함수
# def testPrint(arr):
#     for i in arr:
#         print(i)
#     print()

import sys
sys.stdin = open('230210 재미있는 오셀로 게임.txt', 'r')

# 돌을 올리면 동작하는 함수
def put(x, y, num):                                                                                         # x,y좌표와 어떤 색인지 표시
    board[x][y] = num # 해당 좌표에 돌을 올림                                                               # 우선 (x, y)좌표 (열,행)좌표 임
    if num == 1: # 올린 내 돌이 1이라면                                                                     # 내 돌이 흑돌이면
        antiNum = 2 # 상대 돌은 2
    else:                                                                                                   # 내 돌이 입력이 0 일 수는 없으니까 백돌이면
        antiNum = 1 # 그것아니라면(올린 내 돌이 2라면) 상대 돌은 1
    #가로 좌 구현
    m = 1
    while y-1-m >= 0 and board[x][y-m] == antiNum: # 돌은 둔자리 왼쪽으로 2칸 이상의 자리가 남았고, 왼쪽 m번째 돌이 상대 돌이라면 아래를 반복
        if board[x][y-m-1] == num: # 왼쪽 m번째 돌의 한칸 왼쪽이 내 돌이라면,
            for j in range(1, m+1): # 그 돌과 내가 둔 돌 사이에 있는 상대돌을 모두
                board[x][y-j] = num # 내 색깔의 돌로 바꿈
            break # while문 벗어나기
        else:
            m+=1 # 왼쪽 m번째 돌의 한칸 왼쪽도 상대 돌이라면, m에 1을 추가함
    #가로 우
    m = 1
    while y+1+m < N and board[x][y+m] == antiNum:
        if board[x][y+m+1] == num:
            for j in range(1, m+1):
                board[x][y+j] = num
            break
        else:
            m += 1
    #세로 상
    m = 1
    while x-1-m >= 0 and board[x-m][y] == antiNum:
        if board[x-m-1][y] == num:
            for j in range(1, m+1):
                board[x-j][y] = num
            break
        else:
            m += 1
    #세로 하
    m = 1
    while x+1+m < N and board[x+m][y] == antiNum:
        if board[x+m+1][y] == num:
            for j in range(1, m+1):
                board[x+j][y] = num
            break
        else:
            m += 1
    # 대각선 상좌
    m = 1
    while x-1-m >= 0 and y-1-m >=0 and board[x-m][y-m] == antiNum: # 내가 둔 돌의 왼쪽과 위 모두 2칸 이상의 칸이 남아있고 왼쪽 위쪽 m칸 위치에 상대 돌이 있다면 반복
        if board[x-m-1][y-m-1] == num: # 내가 둔 돌에서 왼쪽 위쪽으로 m칸보다 한칸 더 이동한 것이 내 돌이라면
            for j in range(1, m+1): # 그 돌과 내가 둔 돌 사이의 상대 돌을
                board[x-j][y-j] = num # 모두 내 돌 색깔로 바꿈
            break # while문 벗어나기
        else:
            m += 1 # 내가 둔 돌의 왼쪽 윗쪽으로 아직 내 돌이 다시 나오지 않았다면 m에 1을 추가하여 반복
    # 대각선 상우
    m = 1
    while x-1-m >= 0 and y+1+m < N and board[x-m][y+m] == antiNum:
        if board[x-m-1][y+m+1] == num:
            for j in range(1, m+1):
                board[x-j][y+j] = num
            break
        else:
            m += 1
    # 대각선 하좌
    m = 1
    while x+m+1 < N and y-m-1 >= 0 and board[x+m][y-m] == antiNum:
        if board[x+m+1][y-m-1] == num:
            for j in range(1, m+1):
                board[x+j][y-j] = num
            break
        else:
            m += 1
    # 대각선 하우
    m = 1
    while x+m+1 < N and y+m+1 < N and board[x+m][y+m] == antiNum:
        if board[x+m+1][y+m+1] == num:
            for j in range(1, m+1):
                board[x+j][y+j] = num
            break
        else:
            m += 1
    # testPrint(board)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())                                                                      # 오셀로판 크기N과 턴수 M 을 받음
    board = [0]*N
    antiNum = 0                         # 함수에서 쓰일 전역변수 '상대돌' 선언 및 초기화                     # 상대방돌이라는 변수를 사용해 돌 색 바꿈 실시위함
    for i in range(N):                                                                                    # 참고, 행렬 만들때 board = [[0]*N for _ in range(N)] 하면 N개의 [[0,0,0,..],[0,0,0,..],[0,0,0,..],[0,0,0,..]] 만들어짐
        tmpList = [0] * N
        board[i] = tmpList              # 0으로 채워진 게임판 생성
    halfN = int(N/2)                                                                                      # 보드 중앙에 세팅하는 흑돌, 백돌 위함(N =4이면 halfN=2 인덱스로 [0][1][2][3]이기 때문에 아래 위치도 들림
    board[halfN-1][halfN-1] = 2                                                                           # 틀림 board[halfN-1][halfN-1] = 2
    board[halfN][halfN] = 2                                                                               # 틀림 board[halfN][halfN] = 2
    board[halfN-1][halfN] = 1                                                                             # 틀림 board[halfN-1][halfN] = 1
    board[halfN][halfN-1] = 1           # 게임판 중앙에 시작돌 1 두개, 2 두개 배치                          # 틀림 board[halfN-1][halfN] = 1
    # testPrint(board)
    for i in range(M):                  # M번만큼 돌을 둘건데,                                              # 턴수인 M만큼 실행
        a, b, c = map(int, input().split()) # a, b, c변수를 입력 받아서 둘거임                              # 받는 (x, y, 색) 즉, (열, 행, 색)
        put(b-1, a-1, c)                    # 입력시 x, y값이 반대이고 입력 인덱스는 0부터가 아니라 1부터 시작이니 1씩 빼주고 함수에 넣어서 돌림
    whtCnt = 0                                                                                              # 흰돌 초기값 0  근데 차이는 없겠지만, 이왕이면 초기값 할거면 put함수 사용이전인 for전에 들어가는게????
    blkCnt = 0                              # 흰돌 검은돌 변수를 0으로 초기화                                 # 검은돌 초기값 0
    for i in range(N):                                                                                      # 행으로 입력받는 i를 인자로 오셀라판의 길이인 N만큼 반복
        for j in range(N):                                                                                  # 열로 입력받는 j를 인자로 오셀라판의 길이인 N만큼 반복
            if board[i][j] == 2:                                                                            # board[i][j]가 백돌이면, 백돌에 +1
                whtCnt += 1
            elif board[i][j] == 1:                                                                          # board[i][j]가 흑돌이면, 흑돌에 +1
                blkCnt += 1                 # 게임판을 모두 훑어서 흰돌과 검은돌이 각각 몇개씩 있는지 카운팅
    print(f'#{tc+1} {blkCnt} {whtCnt}')     # 결과 출력