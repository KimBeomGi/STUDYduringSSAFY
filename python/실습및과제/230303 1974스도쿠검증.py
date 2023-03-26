
# [문제]
# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

# [제약 사항]
# 1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
# 2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
sys.stdin = open('230303 1974스도쿠검증.txt', 'r')
# [문제풀이]
# 0. 스도쿠가 맞다면 1을 틀리다면 0을 출력하는 문제이다.
# 1. 한줄, 한 격자에 1~9의 숫자만이 들어있어야한다.
# 1-1. 따라서 겹치는 숫자가 있다면 틀렸으며 또한 한 격자의 합이 45가 아니라도 틀린문제가 된다.
# 격자 0~2 3~5 6~8 인덱스별로 확인하도록 해주기

def is_sdoku(sdoku):
    # 행에 문제 여부 확인
    for row in range(9):                        # 각 행만 확인 할 것임.
        if len(set(sdoku[row])) != 9:           # 정렬했더니 스도쿠가 겹치는게 있어서 9개가 아니면
            return 0                            # 스도쿠가 아니므로 0을 출력

    # 열에 문제 여부 확인
    for column in range(9):                     # 열마다 확인하기 위함
        temp_list = []                          # 임시로 각 열의 행 값을 받을 리스트 생성
        for row in range(9):                    # 행을 반복
            temp_list.append(sdoku[row][column])# temp_list에 값을 추가
        if len(set(temp_list)) != 9:            # 중복되는 값이 있어 중복 제거후 숫자가 9개가 아니면
            return 0                            # 스도쿠가 아니므로 0을 출력

    # 격자에 문제 여부 확인
    lattice = [0,3,6]                                   # 격자 위치 0,3,6
    for lett in lattice:                                # 격자 위치별로 반복해주기
        temp_list = []                                  # 새로 temp_list 생성
        for row in range(lett, lett+3):                 # 격자의 행만큼 반복
            for column in range(lett, lett+3):          # 격자의 열만큼 반복
                temp_list.append(sdoku[row][column])    # temp_list에 값을 추가
        if len(set(temp_list)) != 9:                    # 중복되는 값이 있어 중복 제거후 숫자가 9개가 아니면
            return 0                                    # 스도쿠가 아니므로 0을 출력
    return 1                                            # 모든 행위를 했음에도 return 0을 거치지 않았다면 올바른 스도쿠 이므로 스도쿠임.

T = int(input())
for testcase in range(1, T+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]     # 스도쿠 만들어 둠
    A = is_sdoku(sdoku)                                 # A에값을 입력
    print(f'#{testcase} {A}')