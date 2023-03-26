for tc in range(1, 11):                     # 10번의 테스트케이스
    M = int(input())                        # 구할 회문의 길이
    N = 8
    result = 0
    board = [input() for _ in range(8)]
    # 가로 회문 검사
    for i in range(8):                      #길이 8고정. 행 순회!
        # 각 행마다 여러개의 회문 검사
        # 회문 검사의 시작점 0~ N-M
        for j in range(N-M+1):
            # 회문 검사: 회문 검사 할 때... 회문의 전체길이의 절반만
            for k in range(M//2):           # 회문에서 몇 번째 글자를 검사하냐?
                if board[i][j+k] != board[i][j+M-1-k]:# 만약에 회문이 아니면
                    break                   # 굳이 더 검사ㄴㄴ 멈춰!
            else:                           # for-else break가 한 번도 안걸림. 즉 여기서는 회문이면~
                result += 1

        # 세로 검사
        for j in range(N-M+1):
            # 회문 검사: 회문 검사 할 때... 회문의 전체길이의 절반만
            for k in range(M//2):           # 회문에서 몇 번째 글자를 검사하냐?
                if board[j+k][i] != board[j+M-1-k][i]:# 만약에 회문이 아니면
                    break                   # 굳이 더 검사ㄴㄴ 멈춰!
            else:                           # for-else break가 한 번도 안걸림. 즉 여기서는 회문이면~
                result += 1

    print(f'#{tc} {result}')
