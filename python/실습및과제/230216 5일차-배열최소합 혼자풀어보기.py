import sys
sys.stdin = open('230216 5일차-배열최소합.txt', 'r')


def permutation_sum(row, perm_sum):                                     # 행과 순열의 합을 매개변수로 함수로 받을 것임
    global min_sum                                                      # global로 min_sum을 가져올 것임
    if perm_sum > min_sum:                                              # 현재 구하고 있는 순열의 합이 min_sum보다 더 크면
        return                                                          # 더 탐색할 필요가 없으니 반환시킴
    
    if row == N:                                                        # 행 row 가 마지막 행에서 넘어와서 N이 되어버렸을 때
        if min_sum > perm_sum:                                          # min_sum이 현재 구한 순열의 합보다 크면
            min_sum = perm_sum                                          # min_sum을 현재 구한 순열의 합으로 교체
        return                                                          # 자신이 호출된 곳으로 돌아간다.
    
    for column in range(N):                                             # column 즉, 각 행마다 열을 알아보기 위한 반복문
        if used_column[column] == 0:                                    # 해당 열이 이번 순열에서 사용되지 않은 열이라면
            used_column[column] = 1                                     # 이제 사용할 거니까 used_column에 해당 열을 사용했음을 기록
            permutation_sum(row+1, perm_sum + matrix[row][column])      # 재귀호출로 다음 행과, 현재 [행][열]의 값을 더한 순열합ㅇ르 매개변수로 함수재개
            used_column[column] = 0                                     # 사용완료했으니 다시 0으로 돌리고 이제 반복문으로 돌아감(반복문 내에선 이 행을 안쓸 거니까.)


T = int(input())
for testcase in range(1,T+1):
    N = int(input())                                                    # 행렬의 길이 N
    matrix = [list(map(int, input().split())) for _ in range(N)]        # N만큼 입력받고 N by N 행렬만들기
    min_sum = 10*N*N                                                    # 순열의 합 최솟값을 입력받을 변수 min_sum
    used_column = [0]*N                                                 # 각 순열에서 사용한 열을 기록하면서 순열을 작성하기 위함

    permutation_sum(0,0)                                                # min_num을 구함
    print(f'#{testcase} {min_sum}')                                     # 출력