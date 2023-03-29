import sys
sys.stdin = open('230328 1244 최대상금.txt','r')

# 트아아암요옥문제가아니다!

# 재귀적으로 교환 작업을 N번 수행하는 재귀함수
# 교환작업: 카드 한 번 교환 할 때 교환할 수 있는 모든 경우의 수 수행
def solve(n):
    global max_v
    value = int(''.join(cards))
    # 만약에 같은 교환 횟수에, 같은 모양이면 다시 연산 하지 않아도 된다
    if (n,value) in checked: # 이미 교환을 해본 경우의 수라면, 수행하지 않음.
        return
    
    # (n, value) 쌍이 checked에 들어있지 않음
    checked.add((n,value))
    if n == N:      # N번 교환 완료!
        # cards의 모양이 최대 값인지 확인!
        if value > max_v:
            max_v = value
        return
    for i in range(len(cards)):             # 모든 카드 교환해보기
        for j in range(i+1,len(cards)):     #
            cards[i], cards[j] = cards[j], cards[i]     # 교환해보기
            solve(n+1)
            cards[i], cards[j] = cards[j], cards[i]     # 원래 대로 돌려놓기
    return

T =int(input())
for testcase in range(1,T+1):
    cards, N = input().split()
    cards = list(cards)
    N = int(N)
    max_v = 0               # 어차피 교환이라 0보다 작은 값은 안들어간다.
    checked = set()         # 중복되는 (교환횟수, value)에 대해서 연산을 하지 않기 위함
    solve(0)
    print(f'#{testcase} {max_v}')
    # print(cards, N)
    