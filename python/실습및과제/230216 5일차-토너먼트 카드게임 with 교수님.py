import sys
sys.stdin = open('230216 5일차-토너먼트 카드게임.txt', 'r')

def solve(left, right):
    if left == right:
        return left

    # 전체범위의 승자를 알기 위해서... 절반 범위의 승자들을 구해야한다.
    mid = (left + right) //2
    winner1 = solve(left, mid)
    winner2 = solve(mid+1, right)

    # winner1과 winner2의 대결의 승자를 반환
    
    # 아래쪽에서 가위바위보해서..winner2가 이기면 바꿔주면 딤
    # 승자 구하기는... 조건문으로 처리하시면 됩니다.
    # data[winner1], data[winner2]
    # 초기값을 winner1로 잡아서 winner2가 이기는 경우만 고려.
    result = winner1
    if data[winner1] == 1: #가위
        if data[winner2] == 2:
            result = winner2
    elif data[winner1] ==2: #바위
        if data[winner2] == 3:
            result = winner2
    else:                  #보
        if data[winner2] == 1:
            result = winner2

    return result

T= int(input())
for testcase in range(1, T+1):
    N = int(input())
    data = [0]+list(map(int,input().split()))
    winner = solve(1, N)
    print(f'{testcase} {winner}')