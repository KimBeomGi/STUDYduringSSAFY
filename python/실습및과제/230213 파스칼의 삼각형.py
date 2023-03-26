# 크기가 N인 파스칼의 삼각형을 만들어야 한다.
# 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
# 1. 첫 번째 줄은 항상 숫자 1이다.
# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
# N이 4일 경우,

# 1
# 1 1
# 1 2 1
# 1 3 3 1

# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

# [제약 사항]
# 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.

# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
# 삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
sys.stdin = open('230213 파스칼의 삼각형.txt', 'r')

# [문제풀이]
# 0. 파스칼으 삼각형은 양 맨끝은 1의 값을 유지하면서,
# 0-1. 그 가운데 값은 위의 2개의 값을 더한 값이 된다.
# 0-2. 여기서 N이 4일 경우 4개의 행렬로 [1] [1 1] [1 2 1] [1 3 3 1]이 만들어 졌으므로 ([]는 없음)
# 0-3. 출력 방식에 대해서도 생각해볼 필요가 있다.


T = int(input())
for testcase in range(1, T+1):              # 테스트케이스 반복
    N = int(input())                        # 몇 행 받을 것인지를 나타내는 N 입력받음
    
    # 파스칼의 삼각형 입력받을 리스트(행렬처럼)만들기
    pascal_triangle = []
    for i in range(1,N+1):                  # N개의 행을 만들것인데
        pascal_triangle.append([0]*i)       # [[0], [0,0], [0,0,0],,,] 의 형식으로 만들 것이다.

    for i in range(N):                      # N번 반복하면서 파스칼의 삼각형을 만들어낼 것임.
        if i == 0:                          # 1, 한개만 들어있는 1행이면
            pascal_triangle[i][i] = 1       # 1행의 값을 1로 만들자.
        elif i == 1:
            pascal_triangle[i][0] = 1       # 2행의 첫번째와 마지막은 1의 값을 가져야 하므로
            pascal_triangle[i][1] = 1
        else:                               # 1행 말고 나머지는
            pascal_triangle[i][0] = 1       # 첫 값: 1
            pascal_triangle[i][-1] = 1      # 마지막 값: 1
            for j in range(1, len(pascal_triangle[i])-1):                                           # [1]~[행의 길이 -1]에 대해서 진행 [1, ~, ~, ~ 1] ~ 표시에 대한 진행
                pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]         # ~의 값이 이전 행의 같은 열의 자리값과 이전열의 자리값을 더한것이 현재 값
    
    # 출력하기
    print(f'#{testcase}')                                           # 테스트케이스 출력
    for i in range(N):                                              # 각 행별로 출력
        for j in range(len(pascal_triangle[i])):                    # 숫자로 이루어진 각 행의 요소들을 문자로 바꿔주기 위함
            pascal_triangle[i][j] = str(pascal_triangle[i][j])      # 숫자로 이루어진 각 행의 요소들을 문자로 전환!
        pascal_triangle[i] = ' '.join(pascal_triangle[i])           # 한 행을 리스트를 풀어서 출력하도록하기
        print(f'{pascal_triangle[i]}')