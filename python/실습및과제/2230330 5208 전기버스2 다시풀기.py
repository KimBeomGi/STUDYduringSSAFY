import sys
sys.stdin = open('2230330 5208 전기버스2.txt')


def charge_count(stop, battery, count):
    global min_charge

    if stop == N-1 and battery >= 0:
        if min_charge > count:
            min_charge = count
            return

    elif battery >= 0 and not went[stop]:
        went[stop] = 1
        if battery > 0:
            charge_count(stop+1, battery-1, count)
        if min_charge >= count+1:
            charge_count(stop+1, batteries[stop]-1, count+1)
        went[stop] = 0
    else:
        return

T = int(input())
for testcase in range(1, T+1):
    N, *batteries = map(int, input().split())
    min_charge = N+1
    went = [0]*(N-1)
    charge_count(0, batteries[0], 0)
    print(f'#{testcase} {min_charge}')