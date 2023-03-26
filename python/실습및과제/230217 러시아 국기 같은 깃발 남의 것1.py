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

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    # for row in flag:
    #     print(row)

    # 각 줄에서 화이트 레드 블루 각각의 색으로 바꾸려면 몇번 바꿔야 하는지 2중 배열 형태로 저장한다.
    change_color_cnt = []
    for row in flag:
        w = M - row.count('W')
        b = M - row.count('B')
        r = M - row.count('R')
        change_color_cnt.append([w, b, r])

    answer = 99999999
    # for row in change_color_cnt:
    #     print(row)

    # w와 b 두가지 숫자를 정하면 r은 자동으로 정해진다. w,r은 0부터, b는 최소 1부터이다.
    for w in range(0, N - 3 + 1):
        for b in range(1, N - 2 + 1 - w):
            r = N - w - b - 2

            # 정해진 라인 수 만큼 자신의 색깔로 바꾸는 카운트를 세어준다.
            cnt = 0
            for i in range(w):
                cnt += change_color_cnt[1:-1][i][0]
            for j in range(w, w + b):
                cnt += change_color_cnt[1:-1][j][1]
            for k in range(w + b, w + b + r):
                cnt += change_color_cnt[1:-1][k][2]

            # 최솟값을 찾고
            answer = min(answer, cnt)

    # 맨윗줄과 맨아랫줄도 바꿔준다.
    answer += change_color_cnt[0][0] + change_color_cnt[-1][2]
    print('#{} {}'.format(tc, answer))