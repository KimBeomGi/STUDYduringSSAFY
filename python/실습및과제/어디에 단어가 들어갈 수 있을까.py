# [문제풀이]
# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

# [예제]
# N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때
# 길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로 4번)이 된다.

# [제약 사항]
# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
# 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

#[문제풀이]
# 0. N by N 의 퍼즐이 주어지는데 주어지는 K와 동일한 길이의 흰색구간을 찾아야한다.
# 0-1. 가로 세로로 확인이 가능하다. 가로로 3개가 연속된 3칸(초과는 x)이면 단어가 들어갈 수 있는 곳에 +1
# 0-2. 세로로 3개가 연속된 3칸(초과는 x)이면 단어가 들어갈 수 있는 곳에 +1
# 1.흰색부분은 1로 주어지고, 검은색 부분은 0으로 주어지므로 우선 연속 된 1의 갯수를 확인 먼저해보자.
# 1-1. 가로는 for i_list in list: for j in i_list로 리스트 안의 리스트에서 연속되는 1의 갯수로 확인
# 1-2. 세로는 for i in range(N): for j in range(N) list[j][i]로 찾아보자.
# 2. 구한 1을 이용해 K와 동일한지 비교 후 값 계산

T = int(input())
for testcase in range(1,T+1):
    N, K = map(int, input().split())    # N, K를 띄어쓰기로 구분해서 주어지므로 .split
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    for row in puzzle:                  # 퍼즐의 한 행
        row_max_1 = []                  # 퍼즐의 한 행에서 흰색읜 연속되는 최대 길이를 담을 리스트
                                        # 이유는 행이 길어져서 2,3,5,4,6 뭐 이런 식으로 될 수도 있으니까
        is_row_max_1 = 0                # 한 행의 가장 긴 흰색길인지 확인을 위한 변수
        for i_row in puzzle:            # 퍼즐의 한 행의 인자
            if i_row == 1:              # 퍼즐의 한 행의 인자가 1(흰색)이면
                is_row_max_1 += 1       # iw_row_max_1에 + 1
            elif i_row != 1:
                row_max_1.append(is_row_max_1)
                is_row_max_1 = 0
            pass