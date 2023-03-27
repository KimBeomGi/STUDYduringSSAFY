# 골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

# 각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

# 두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

# N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

# e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

# e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

#   1  2  3 도착
# 1 0 18 34
# 2 48 0 55
# 3 18 7 0
# 출발

# 이 경우 최소 소비량은 89가 된다.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('5189 전자카트.txt')

# [문제풀이]
# 0. 각 사무실을 돌아다니되 전기 카트의 최소 배터리 사용량을 구해야한다.
# 0-1. 모든 사무실을 들려야 하는데, 각 사무실로 가는데 드는 배터리 사용량이 다르다.
# 해설을 보니 행의 값이 출발지고, 열의 값이 도착지이므로 배터리 사용량 보는 법은 2번방에서 1번 방이면 [2][1]이다.
# 각 방은 연결되어야하므로 내가 2번 방이면 [2][?]의 경로가 내가 갈 수 있는 경로이다.


def battery_spend(matrix, start, arrival, spend_q, spend_batteries, count):
    spend_q += matrix[start][arrival]                               # spned_q 를 더하기
    count += 1                                                      # count += 1 해주기
    if arrival == 0 and count != N:                               # 모든 방을 돌지 않았는데 내 원래 방에 들어갔다면
        count -= 1                                                  # 카운트 1 빼기
        spend_q -= matrix[start][arrival]                           # 더해줬던 spend_q값 빼주기
        return                                                      # 돌아가기
    elif arrival == 0 and count == N:                             # 모든 방을 돌고 내 원래 방에 들어갔다면
        spend_batteries.append(spend_q)                             # spend_q값을 리스트에 추가
        count -= 1                                                  # 카운트 1빼기
        spend_q -= matrix[start][arrival]                           # 더해줬던 spend_q값 빼주기
        return

    for i in range(N):                                              # N 만큼 반복해주기(도착지 설정임)
        if arrival != i:                                            # 출발지와 도착지가 같지 않을때 실행
            battery_spend(matrix, arrival, i, spend_q, spend_batteries)     # 도착지가 출발지가 되기.
    return spend_batteries
    


T =int(input())                                                     # 테스트 케이스
for testcase in range(1, T+1):                                      # 테스트 케이스만큼 반복
    N = int(input())                                                # 길이 N 입력받음
    matrix = [list(map(int,input().split())) for _ in range(N)]     # N by N의 행렬 생성
    spend_batteries = []
    A = battery_spend(matrix, 0, 0, 0, spend_batteries, 0)
    print(A)
    
    