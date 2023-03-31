import sys
sys.stdin = open('2230331 수영장.txt','r')
# 월별로 돈을 내는 모든 경우의 수를 다 따져보기
# month: 돈을 내는 달
# 이전 달까지 낸 돈
def solve(month, money):
    global min_v
    if month >= 13: # 12월까지 모두 돈을 냈으니.. 총합만 계산하면 됩니다.
        min_v = min(min_v, money, y)    # y는 1년치 요금
        return
    # 일별로 계산 : 여태까지 낸 돈 + 이번달 나온 횟수 * 일별 요금
    solve(month+1, money+days[month]*d)
    # 월별로 계산
    solve(month+1, money+m)
    # 분기별 계산
    solve(month+3, money+q)


T = int(input())
for testcase in range(1, T+1):
    d, m, q, y = map(int,input().split())
    days = [0] + list(map(int,input().split())) # 월과 인덱스를 맞춰주기 위해 앞에 [0]을 더해줌
    min_v = 0xffffffff
    solve(1, 0)
    print(f'#{testcase} {min_v}')