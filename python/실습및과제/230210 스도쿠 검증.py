# [문제]
# 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다
# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
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
sys.stdin = open('230210 스도쿠 검증.txt', 'r')
# [문제풀이]
# 0. 스도쿠는 N by N개의 행렬로 이루어져있는 숫자판으로 각 세로와 가로에 1~9까지의 숫자가 겹치지 않게 하나씩 들어가며,
# 0-1. 스도쿠판 안의 작은 격자안에서도 1~9까지의 숫자가 겹치지 않게 하나씩 들어가도록 하는 놀이이다.
# 1. 해당 문제는 9 by 9의 행렬로 이루어진 숫자판에서 진행되며,
# 1-1. 입력받는 숫자로 이루어진 스도쿠가 제대로된 스도쿠라면 1을, 제대로되지 않은 스도쿠라면 0을 출력하면된다.
# 2. 우선 1~9까지 모두 더하면 45이므로 sum값이 45인지 확인과 동시에
# 2-1. 1~9의 숫자가 모두 들어있는지를 확인해야된다.
# 3. 2의 과정을 가로, 세로, 각 3x3의 격자마다 실행하면 된다. 참고로 여기는 9x9이므로 총 9개의 작은 격자가 있다.

T= int(input())
for testcase in range(1, T+1):
    N = 9                       # 테스트 케이스
    sudoku = [list(map(int, input().split())) for _ in range(N)]        # N행의 스도쿠 생성
    
    # 가로 행의 스도쿠 여부 확인
    def row_sudoku(sudoku):
        for i in range(N):                                  # i인자로 N만큼 반복
            is_okay_list = []                               # 각 세로 열마다 스토쿠 가능 여부 확인하기 위해 만든 빈 리스트
            for j in range(N):                              # j인자로 N만큼 반복
                is_okay_list.append(sudoku[i][j])           # is_okay_list에 한 행을 입력받음.
            is_okay_list_sum = 0                            # 스도쿠는 1~9까지 합해서 45가 되야하니 sum을 사용하기 위한 변수
            for is_it in range(N):                          # N개 받았을 거니까 range(N)
                is_okay_list_sum += is_okay_list[is_it]     # 스도쿠 한 행에 들어있는 값 SUM하기
            is_overlap = len(set(is_okay_list))             # 겹치는 수가 있는지 확인하고 그 길이로 계산
            if (is_overlap != 9) or (is_okay_list_sum != 45): # 만약 중복제거한 is_okay_list가 9개 또는 45가 아니면
                return False                                # 스도쿠가 아니니 종료
        else:                                               # 스도쿠 조건에 일치하면
            return True

    # 세로 행의 스도쿠 여부 확인
    def column_sudoku(sudoku):
        for i in range(N):                                  # i인자로 N만큼 반복
            is_okay_list = []                               # 각 세로 열마다 스토쿠 가능 여부 확인하기 위해 만든 빈 리스트
            for j in range(N):                              # j인자로 N만큼 반복
                is_okay_list.append(sudoku[j][i])           # is_okay_list에 한 열을 입력받음.
            is_okay_list_sum = 0                            # 스도쿠는 1~9까지 합해서 45가 되야하니 sum을 사용하기 위한 변수
            for is_it in range(N):                          # N개 받았을 거니까 range(N) is_it은 계속 sum하기 위해서 쓰이는 인자
                is_okay_list_sum += is_okay_list[is_it]     # 스도쿠 한 열에 들어있는 값 SUM하기
            is_overlap = len(set(is_okay_list))             # 겹치는 수가 있는지 확인하고 그 길이로 계산
            if (is_overlap != 9) or (is_okay_list_sum != 45): # 만약 중복제거한 is_okay_list가 9개 또는 45가 아니면
                return False
        else:
            return True

    def lattice_sudoku(sudoku):
        lattice_position = [0,3,6]                          # 각 격자가 시작하는 위치인덱스를 표현한 리스트
                                                            # 9 by 9에서는 인덱스 위치가 0,3,6으로 나눠지니까.
        for lattice in lattice_position:                    # 각 격자에서 시작할 수 있도록 만들어주는 반복문
            is_okay_list = []                               # 각 격자마다 스토쿠 가능 여부 확인하기 위해 만든 빈 리스트
            is_okay_list_sum = 0                            # 스도쿠는 1~9까지 합해서 45가 되야하니 sum을 사용하기 위한 변수
            for i in range(lattice, lattice+3):             # 각 격자 안에서만 i인자를 반복
                for j in range(lattice, lattice+3):         # 각 격자 안에서만 j인자를 반복
                    is_okay_list.append(sudoku[i][j])       # is_okay_list에 해당 격자내 스도쿠 값 추가
            for is_it in range(N):                          # N개 받았을 거니까 range(N) is_it은 계속 sum하기 위해서 쓰이는 인자
                is_okay_list_sum += is_okay_list[is_it]     # 스도쿠 한 열에 들어있는 값 SUM하기
            is_overlap = len(set(is_okay_list))             # 겹치는 수가 있는지 확인하고 그 길이로 계산
            if (is_overlap != 9) or (is_okay_list_sum != 45): # 만약 중복제거한 is_okay_list가 9개 또는 45가 아니면
                return False
        else:                                               # 스도쿠 조건에 일치하면
            return True
    
    # 스도쿠 여부 확인 실시 및 출력
    if (row_sudoku(sudoku) == True) and (column_sudoku(sudoku) == True) and (lattice_sudoku(sudoku) == True):
        print(f'#{testcase} {1}')
    else:
        print(f'#{testcase} {0}')