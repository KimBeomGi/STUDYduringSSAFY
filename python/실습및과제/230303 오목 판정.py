import sys
sys.stdin = open('230303 오목 판정.txt','r')

# [문제]
# N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.
# 다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다. 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.

# [출력]
# 각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다.

# [문제풀이]


def is_omok(game):
    # 델타를 이용해 확인해주자.# 함수를 이용해버릴까?
    # 8방향(상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    for row in range(N):                                # 행으로 돌리기
        for column in range(N):                         # 열로 돌리기
            if game[row][column] == 'o':                # 만약 바둑돌이 들어있는 칸이라면 검사 시작해보자.
                for i in range(8):                      # 8방향으로 확인
                    count = 1                           # 오목여부 확인하기 위한 count변수
                    for j in range(1,5):                # 1~4까지 확인 해줄 것이기 때문
                        nr = row + dr[i]*j              # 다음 행위치 
                        nc = column + dc[i]*j           # 다음 열위치
                        # 범위 내에 있고, 바둑돌이 있으면 카운트 없으면 중단
                        if 0 <= nr < N and 0 <= nc < N and game[nr][nc] == 'o' :
                            count += 1
                            if count ==5:               # 만약 5개가 되었으면
                                return 'YES'            # yes 출력
                        else:
                            break
    return 'NO'                                         # 다 찾아도 없으니까 no출력

T = int(input())
for testcase in range(1, T+1):
    N = int(input())                                    # 오목판의 크기
    game = [list(input()) for _ in range(N)]            # 만들어진 오목판 만들기
    A = is_omok(game)                                   # Answer인 A에 is_omok()의 값을 입력
    print(f'#{testcase} {A}')                           # 출력
    # print(game)