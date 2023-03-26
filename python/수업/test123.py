# import sys
#
# sys.stdin = open('230216 5일차-토너먼트 카드게임.txt', 'r')


# 가위바위보
def r_s_p(card_num, left_group, right_group):  # 가위바위보 게임실시
    if card_num[left_group] == 1:  # 왼쪽 학생이 가위면?
        if card_num[right_group] == 1 or card_num[right_group] == 3:  # 오른쪽 학생이 가위거나, 보를 내면
            return left_group  # 왼쪽 학생이 이김
        else:  # 아니면?
            return right_group  # 오른쪽 학생이 이김

    elif card_num[left_group] == 2:  # 왼쪽 학생이 바위면?
        if card_num[right_group] == 2 or card_num[right_group] == 1:  # 오른쪽 학생이 바위거나, 가위를 내면
            return left_group  # 왼쪽 학생이 이김
        else:  # 아니면?
            return right_group  # 오른쪽 학생이 이김

    elif card_num[left_group] == 3:  # 왼쪽 학생이 보면?
        if card_num[right_group] == 3 or card_num[right_group] == 2:  # 오른쪽 학생이 보, 바위 면
            return left_group  # 왼쪽 학생이 이김
        else:  # 아니면?
            return right_group  # 오른쪽 학생이 이김


# 둘로나누기
def divide_group(card_num, start, end):  # 그룹을 둘로 나눠야해서 만든 함수(재귀함수임.....ㅠㅠ)

    if start == end:  # 만약 시작과 끝이 같다면?
        return start  # start를 반환
    left_group = divide_group(card_num, start, (start + end) // 2)  # left_group은 중간값을 기준으로 처음부터~중간
    right_group = divide_group(card_num, ((start + end) // 2) + 1, end)  # right_group은 중간값을 기준으로 중간~마지막

    return r_s_p(card_num, left_group, right_group)  # 나눴으면 가위바위보하러 가야지.


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())  # 인원수 N을 입력받음
    card_num = list(map(int, input().split()))  # 각 인원이 고른 카드(가위바위보 숫자)
    winner = divide_group(card_num, 0, N - 1)  # 승자는? divide_group함수의 마지막에 남은 자가 승자
    print(f'#{testcase} {winner + 1}')  # winner+1은 학생번호가 0번부터가 아닌 1번부터라서
