#################
# 너무 시간이 오래걸려서 중도 포기
# 다시 풀어야함
# N, M = map(int, input().split())    # 행 N, 열 M을 입력받음


# board = [list(input()) for _ in range(N)]

# count = 0
# for row in range(N-8+1):                # 행 길이가 8이면 1번 가능, 9면 2번 확인 가능
#     for column in range(M-8+1):         # 열 길이가 8이면 1번 가능, 9면 2번 확인 가능
#         # 각 행별로 확인해보자
#         # 'BWBWBWBW' 나 'WBWBWBWB'가 아니면 바로 끝
#         tmp_board = []
#         for i in range(8):              # 8번 반복해야함
#             tmp = ''
#             for j in range(8):
#                 tmp += board[row+i][column+j]
#             tmp_board.append(tmp)
#             # 'BWBWBWBW' 나 'WBWBWBWB'인지 확인하기
#             # 첫 행
#             if i == 0:
#                 if tmp not in ('BWBWBWBW', 'WBWBWBWB'):
#                     count += 1
#                     break
#             # 첫 행 아닐 때
#             elif i != 0:
#                 if tmp_board[i-1] == 'BWBWBWBW' and tmp != 'WBWBWBWB':
#                     count += 1
#                     break
#                 elif tmp_board[i-1] == 'WBWBWBWB' and tmp != 'BWBWBWBW':
#                     count += 1
#                     break
#                 elif tmp not in ('BWBWBWBW', 'WBWBWBWB'):
#                     count += 1
#                     break

# print(count)


################### 빼낌

N,M = map(int,input().split())

board = []
count = []

#이중배열 만들기
for i in range(N):
    board.append(input())

#8 x 8 돌리기
#행렬은 왼쪽 상단이 (0,0)임
#행
for y in range(N-7):
    #열
    for x in range(M-7):
        index = 0
        index2 = 0
        #BWBW 8x8 
        for i in range(y,y+8):
            for j in range(x,x+8):
            #WBWBWBWB
            #BWBWBWBW에서 W인 것들의 공통점은 행 + 열의 값이 짝수라는 것
                if((i+j) % 2 == 0): #()?? 필수
                    if(board[i][j] != 'W'):
                        index += 1
                    if(board[i][j] != 'B'):
                        index2 += 1
                else:
                    if(board[i][j] != 'B'):
                        index += 1
                    if(board[i][j] != 'W'):
                        index2 += 1 # +=를 =+로...
                
        count.append(min(index,index2))

print(min(count))