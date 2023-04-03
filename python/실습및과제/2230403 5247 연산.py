# [문제]
# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
# 단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
# 예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.

# [입력]
# 첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('2230403 5247 연산.txt')

# [문제풀이]
# 0. +1, -1, *2, -10 의 네 가지 연산을 이용해서  최소 몇 번의 연산을 거치면 N이 M이 되는지를 확인하는 문제이다.
# 1. DFS로 풀어야지 생각했지만 BFS로 풀어야, 무한반복을 멈출수 있다.(멈춰!!!!)
# 2. 중간 결과도 항상 백만 이하의 자연수 이어야 하므로 0 < x < 1000000의 조건을 달고 있어야한다.

def find(n, count):
    queue = [(n, count)]
    visited = set()
    visited.add(n)

    while queue:
        n, count = queue.pop(0)

        if n == M:
            return count
        
        if n > 1000000:
            continue
        
        if n+1 not in visited:
            queue.append((n+1, count+1))
            visited.add(n+1)

        if n-1 not in visited:
            queue.append((n-1, count+1))
            visited.add(n-1)

        if n*2 not in visited:
            queue.append((n*2, count+1))
            visited.add(n*2)

        if n-10 not in visited:
            queue.append((n-10, count+1))
            visited.add(n-10)


T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    result = find(N, 0)
    print(f'#{testcase} {result}')