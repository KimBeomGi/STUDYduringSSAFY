import sys
sys.stdin = open('230217 러시아 국기 같은 깃발.txt', 'r')

# 2016년은 삼성전자가 러시아 현지법인을 설립한지 20주년이 된 해이다. 이를 기념해서 당신은 러시아 국기를 만들기로 했다.
# 먼저 창고에서 오래된 깃발을 꺼내왔다. 이 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나로 칠해져 있다.
# 당신은 몇 개의 칸에 있는 색을 다시 칠해서 이 깃발을 러시아 국기처럼 만들려고 한다. 다음의 조건을 만족해야 한다.

# 위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
# 다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
# 나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.

# 이렇게 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여라.
# 첫 번째 예제이다. 왼쪽에 있는 그림이 입력이다. 중간에 있는 그림에 X가 적힌 칸들을 새롭게 색칠하여 오른쪽에 있는 그림과 같은 깃발을 만들면 최적이다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 N,M(3≤N,M≤50)이 공백으로 구분되어 주어진다.
# 다음 N개의 줄에는 M개의 문자로 이루어진 문자열이 주어진다. i번 째 줄의 j번째 문자는 깃발에서 i번째 행 j번째 열인 칸의 색을 의미한다.
# ‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미한다. ‘W’, ‘B’, ‘R’외의 다른 문자는 입력되지 않는다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여 T 줄에 걸쳐서 출력한다.

# [문제풀이]
# 0. 적어도 한줄 씩은 흰색, 파란색, 빨간색으로 이루어져야 하는데 위에서부터 흰색, 파란색, 빨간색으로 이루어져야 한다.
# 1. 각 행에서 흰색, 파란색, 빨간색 중 더 많은 색으로 이루어진 색으로 색을 칠하는데 
# 1-1. 위의 행에서부터는 파란색이 더 많은 행이 생기면 바로 파란색으로 바뀌도록 하고
# 1-2. 1-1과 마찬가지로 빨간색이 더 많은 행이 생기면 바로 빨간색을 바뀌도록 해보자.
# 2. 우선 첫행과 마지막 행은 흰색과 빨간색으로 만들어두자.

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int,input().split())                                             # 행 N과 열 M을 받음
    Flag = [list(map(str, input().split())) for _ in range(N)]                  # 행 N만큼 입력받아 국기를 만듬

# [문제풀이]
# 0. 적어도 한줄 씩은 흰색, 파란색, 빨간색으로 이루어져야 하는데 위에서부터 흰색, 파란색, 빨간색으로 이루어져야 한다.
# 1. 각 행별로 확인해보자.
# 1-1. 1,2,3,4,5 있으면 흰 파 빨 빨 빨, 흰 파 파 빨 빨, --- 흰 흰 흰 파 빨 처럼 한 행별로 확인할 수 있도록 해보자.
# 1-2. 우선 흰색을 먼저 확인하고, 그리고 파란색, 빨간색을 확인해보자.
# 1-3. 파란색과 빨간색은 꼭 있어야하고 순서도 중요하니까 순서가 이루어지게 하자.
# 1-4. 한번 확인이 끝날때마다 최솟값인지 여부를 확인 될 수 있도록 하자.
 
T = int(input())
for testcase in range(1, T+1):
    N, M = map(int,input().split())                 # 행 N과 열 M을 받음
    Flag = [list(input()) for _ in range(N)]        # 행 N만큼 입력받아 국기를 만듬. 문자열은 list에 생으로 넣으면 분리되므로. list(input())으로 작성
    min_change = (N*M)+1                            # 최대 바꿀수 있는 경우는 다 바꾸는 경우니까 그보단 많게하기 위해 N*M +1
 
    # 흰색이 1행인 경우부터 최대 행인 경우까지 확인. 파란색도, 빨간색도 마찬가지.
    white_count = 0                                 # 흰색으로 바꾼 칸의 갯수를 확인하는 변수. for문 밖에 있는 이유는 1행 그리고 1행에 추가해서 1행.의 식으로 증가하면서 생기기 때문
    for white in range(N-2):                        # 파란색과 빨간색이 1줄씩은 차지해야하니까. 흰색이 차지하는 공간이 [0] ~ ([0]~[N-3]) 인 경우를 확인
        for column_w in range(M):                   # 흰색의 열을 확인
            if Flag[white][column_w] != 'W':        # 흰색이 차지해야 할 행에 있는 칸이 W 흰색이 아니라면
                white_count += 1                    # 흰색으로 바꿨다고 하고 갯수를 추가(진짜로 바꿔버리면 다음 반복문에서 못쓰니까 횟수만 확인)
             
        blue_count = 0                              # 파란색으로 바꾼 칸의 갯수를 확인하는 변수
        for blue in range(white+1, N-1):            # 흰색 다음 행부터 파란색이고 또, 빨간색이 1줄씩은 차지해야하니까. 파란색이 차지하는 공간이 [1] ~ ([1]~[N-2]) 인 경우를 확인
            for column_b in range(M):               # 파란색의 열을 확인
                if Flag[blue][column_b] != 'B':     # 파란색이 차지해야 할 행에 있는 칸이 B 파란색이 아니라면
                    blue_count += 1                 # 파란색으로 바꿨다고 하고 갯수를 추가(진짜로 바꿔버리면 다음 반복문에서 못쓰니까 횟수만 확인)
 
            red_count = 0                           # 빨간색으로 바꾼 칸의 갯수를 확인하는 변수
            for red in range(blue+1, N):            # 파란색 다음 행부터 빨간색이 가능하니까. 빨간색이 차지하는 공간이 [2] ~ ([2]~[N-1]) 인 경우를 확인
                for column_r in range(M):           # 빨간색의 열을 확인
                    if Flag[red][column_r] != 'R':  # 빨간색이 차지해야 할 행에 있는 칸이 R 빨간색이 아니라면
                        red_count += 1              # 빨간색으로 바꿨다고 하고 갯수를 추가(진짜로 바꿔버리면 다음 반복문에서 못쓰니까 횟수만 확인)
             
            # 빨간색을 다 확인했으면 한번의 확인이 끝난 거니까 이제 칸을 바꾼 횟수가 최솟값인지 확인
            change_count = white_count + blue_count + red_count     # 이번 탐색에서 바꾼횟수를 기록
            if min_change > change_count:           # min_change가 이번 탐색에서의 횟수인 change_count보다 크면
                min_change = change_count           # min_change에 change_count를 대입
     
    print(f'#{testcase} {min_change}')              # 출력값 출력