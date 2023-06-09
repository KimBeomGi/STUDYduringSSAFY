import sys
sys.stdin=open('2230331 14035 격자판의 숫자 이어 붙이기.txt','r')

# [문제]
# 4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.
# 격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.
# 이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.
# 단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.
# 격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스마다 4개의 줄에 걸쳐서, 각 줄마다 4개의 정수로 격자판의 정보가 주어진다.

# [출력]
# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 격자판을 이동하며 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 출력한다.

# [문제 풀이]
# 0. 4 by 4 크기의 격자판에 각 0~9 사이의 숫자가 적혀있다.
# 0-1. 임의의 위치에서 4방향으로 인접한 곳 총 6번 이동 각 칸에 적혀있는 숫자를 차례대로 이어붙여서 7자리 숫자를 만든다.
# 0-2. 따라서 자기위치포함 7개의 칸을 방문한다. 한 번 거쳐도 상관 없으며
# 0-3. 만들수 있는 다른 일곱자리수의 갯수를 구해라.
# 1. 델타를 이용해서 4방향으로 돌자
# 2. 겹치는 것은 없어야하니까 set을 이용하자.


def find7(ci, cj, count, value):
    global answer_tmp
    if count == 6:                                                  # 6번 이동 했으면
        answer_tmp.append(int(value))                               # answer_tmp에 만들어진 값을 append해주기
        return                                                      # 돌아가서 다시 찾아 이자싁아

    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):                      # 상하좌우확인
        ni = ci +di                                                 # 다음행
        nj = cj +dj                                                 # 다음열
        if 0 <= ni < 4 and 0 <= nj < 4 :                            # 보드 안에있을때만 작동
            find7(ni,nj,count+1, value+board[ni][nj])               # 함수 발동!

T = int(input())
for testcase in range(1, T+1):
    board = [list(map(str, input().split())) for _ in range(4)]
    answer_tmp = []                                                 # 리스트로 각 7자리를 집어넣을거.
    for i in range(4):                                              # 격자 행 4칸
        for j in range(4):                                          # 격자 열 4칸
            find7(i,j,0, board[i][j])                               # 함수 실행
    answer_tmp2 = set(answer_tmp)                                   # 모든 가능 값의 중복을 제거
    answer = len(answer_tmp2)                                       # 중복제거한 모든 가능 값의 수 게산
    print(f'#{testcase} {answer}')