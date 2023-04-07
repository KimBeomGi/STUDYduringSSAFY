# nqueen을 위한 함수
def nqueen(row):                        # 각 행마다 확인할거임
    global count                        # global로 count가져오기
    if row == N:                        # row가 N과 같다면 검사 다 한거니까
        count += 1                      # count+=1 해주기
        return
    
    for col in range(N):                # 각 row마다 col을 확인할 거임
        if not check_col[col] and not dia1[row+col] and not dia2[row-col+N-1]:
            # 해당 컬럼을 사용하지 않았고, 해다 대각선도 사용하지 않았다면 진행
            # row+col의 이유는 우하 대각선을 값으로 따졌을때,
            # row-col+N-1의 이유는 좌하 대각선을 값으로 따졌을때,
            check_col[col] = 1          # 해당 열을 1로 바꾸고
            dia1[row+col] = 1           # 해당 대각선도 1로 바꾸고
            dia2[row-col+N-1] = 1       # 해당 대각선도 1로 바꾸고
            queen[row] = col            # queen[row]에 열을 기입해준다.
            nqueen(row+1)               # 다음행 확인해보자.
            # 확인 끝났으면 다시 0으로 만들어두기
            check_col[col] = 0
            dia1[row+col] = 0
            dia2[row-col+N-1] =0 


N = int(input())
board = [[0]*N for _ in range(N)]
check_col = [0]*N
queen = [0]*N
count = 0
dia1 = [0] *(2*N-1)                     # 대각선 갯수는 2*N-1 dlrl Eoans
dia2 = [0] *(2*N-1)                     # 대각선 갯수는 2*N-1 dlrl Eoans
nqueen(0)
print(count)