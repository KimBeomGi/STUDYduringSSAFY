# [문제]
# 카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다. 
# 정확한 방식은 다음 그림과 같다.

# N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.
# 만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.
# 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어진다.
# 카드의 이름은 알파벳 대문자와 ‘-’만으로 이루어져 있으며, 길이는 80이하이다.

# [출력]
# 각 테스트 케이스마다 주어진 덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력한다.

import sys
sys.stdin = open('230303 3499 퍼펙트 셔플.txt','r')

# [문제풀이]
# 0. 카드를 반으로 나눈다. 그리고 각 반에서 한장씩 다른 곳에 둠으로 그고샤에서 카드덱이 생성된다라고 생각.
# 0-1. N이 홀수면 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다고 하는데 그냥 반반이 반+1 반 되는 것이다.

T = int(input())
for testcase in range(1, T+1):
    N = int(input())                                    # 카드 갯수 N
    initial_deck = list(map(str, input().split()))      # 최초 덱
    # print(initial_deck)
    first_deck = []
    second_deck = []
    mixed_deck = []
    
    # 카드 갯수가 홀수 일 때
    if N % 2 == 1:
        for first in range(N//2+1):                     # 0~N//2까지
            first_deck.append(initial_deck[first])      # 첫번째 덱에 넣기
        for second in range(N//2+1, N):                 # N//2 +1에서 끝까지는
            second_deck.append(initial_deck[second])    # 두번째 덱에 넣기
    # 카드 갯수가 짝수 일 때
    elif N % 2 == 0:
        for first in range(N//2):                       # 0~(N//2)-1까지
            first_deck.append(initial_deck[first])      # 첫번째 덱에 넣기
        for second in range(N//2, N):                   # N//2에서 끝까지는
            second_deck.append(initial_deck[second])    # 두번째 덱에 넣기
    
    # 카드 갯수가 홀수 일 때
    if N % 2 == 1:
        for i in range(len(first_deck)-1):              # 첫번째덱의 마지막 전까지만 실시
            mixed_deck.append(first_deck[i])            # 첫번째덱 카드 끼우고
            mixed_deck.append(second_deck[i])           # 두번째덱 카드 끼우기
        mixed_deck.append(first_deck[-1])               # 첫번째덱의 마지막 카드 끼우기
    
    # 카드 갯수가 짝수 일 때
    elif N % 2 == 0:
        for i in range(len(first_deck)):                # 첫번째덱 카드 수만큼 실시
            mixed_deck.append(first_deck[i])            # 첫번째덱 카드 끼우고
            mixed_deck.append(second_deck[i])           # 두번째덱 카드 끼우기
    answer = ' '.join(mixed_deck)                       # 리스트를 각 문자로 빼내오기
    print(f'#{testcase} {answer}')

    # for i in range(len(first_deck)):
    #     try:
    #         mixed_deck.append(first_deck[i])
    #         mixed_deck.append(second_deck[i])
    #     except:
    #         pass
    # answer = ' '.join(mixed_deck)                       # 리스트를 각 문자로 빼내오기
    # print(f'#{testcase} {answer}')