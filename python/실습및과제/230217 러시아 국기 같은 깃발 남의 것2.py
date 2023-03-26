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

# combination(조합)을 사용한 풀이

# 순열로 구할 수도 있지만, 터지지 않는 조합으로 구하는 방법
# 253ms로 가장 빨랐다
def comb(idx, cnt, selected):
    global res

    if cnt == 2: # 두번 짤랐음
        # 만약 여기서 0,1이 나온다면
        total_cnt = 0
        # 0번째 index (첫 번째 행)은 하얀색, 1번째 index (두 번째 행)은 파란색, 그 아래는 모두 빨간색이라는 의미다.
        # index로 들어와있기 때문에 계산하기 위해 구분선마다 + 1을 해 준다.
        first_line = selected[0] + 1 # 첫 번째 구분선
        second_line = selected[1] + 1 # 두 번째 구분선

        # 하얀색
        for i in range(first_line):
            for j in flag[i]:
                if j != 'W':
                    total_cnt += 1

        # 파란색
        for i in range(first_line, second_line):
            for j in flag[i]:
                if j != 'B':
                    total_cnt += 1

        # 빨간색
        for i in range(second_line, N):
            for j in flag[i]:
                if j != 'R':
                    total_cnt += 1

        if res > total_cnt:
            res = total_cnt

        return

    # 만약 idx가 마지막 행이라면, Red Color가 보장되지 않으므로 return
    # ex) 첫 번째 구분선의 idx가 2일 경우, idx+1을 하면 3이 되어 맨 아랫줄의 빨간 부분을 보장할 수 없으므로 바로 return
    if idx == N-1:
        return

    # 현재 idx를 cnt(구분선의 index) 로 지정한 뒤, 구분선을 한개 지정했음을 반영하기 위해 cnt + 1을 해 준 뒤 재귀를 들어간다.
    selected[cnt] = idx
    comb(idx+1, cnt+1, selected)
    # idx만 올리고, cnt를 올리지 않고 재귀를 들어간다.
    # 이렇게 하여, 만약 N이 4일 경우 [0,1] 을 첫 번째 구분선으로 지정할 수 있게 된다.
    comb(idx+1, cnt, selected)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행 M열 , 최대 50행 50열
    flag = [list(input()) for x in range(N)]
    res = 2147483647
    selected = [None, None]

    # 앞은 idx, 뒤는 idx들의 중간합
    comb(0, 0, selected)

    print('#{} {}'.format(tc, res))