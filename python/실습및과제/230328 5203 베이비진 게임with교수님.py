import sys
sys.stdin=open('230328 5203 베이비진 게임.txt')

def check_win(arr):
    # run or triplet 이 나오면 True, 아니면 False
    for i in range(len(arr)-2):
        if arr[i] >= 3:
            return True
        if i < len(arr):
            if arr[i] and arr[i+1] and arr[i+2]:
                return True
    return False

T = int(input())
for testcase in range(1,T+1):
    data = list(map(int,input().split()))
    arr_a = [0]*10
    arr_b = [0]*10
    winner = 0
    for i in range(0,12,2):
        arr_a[data[i]] += 1
        if check_win(arr_a):
            winner = 1
            break
        arr_b[data[i+1]] += 1
        if check_win(arr_b):
            winner = 2
            break
    print(f'#{testcase} {winner}')