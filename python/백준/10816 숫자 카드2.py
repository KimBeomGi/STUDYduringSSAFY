# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.


# import sys
# # 입력받기
# N = int(sys.stdin.readline().strip())
# cards1 = list(map(int, sys.stdin.readline().strip().split()))
# cards1.sort()                                                   # 이진 탐색을 위해 정렬해주기
# M = int(sys.stdin.readline().strip())
# cards2 = list(map(int, sys.stdin.readline().strip().split()))
# count_cards = [0]*M

# for i in range(M):
#     cards2[i]
#     find = []                                                   # card1에 들어간 idx를 넣기 위함
#     # 이진 탐색 이용
#     # 인덱스 이용할 거임
#     left = 0
#     right = N-1

#     while left <= right:                                         # left가 right보다 커지면 안되지
#         mid = (left+right) // 2                                 # mid 인덱스를 생성
#         if cards1[mid] == cards2[i] and mid not in find:        # card1에 card2[i]의 값이 있으면
#             count_cards[i] += 1
#             find.append(mid)
#             if mid < N//2:
#                 left = mid+1
#             else:
#                 right = mid -1
#         elif cards1[mid] > cards2[i]:
#             right = mid -1
#         elif cards1[mid] < cards2[i]:
#             left = mid + 1

# print(count_cards)



# print(N)
# print(cards1)
# print('----------------')
# print(M)
# print(cards2)


##########################
# # gpt 미쳤네
# import sys
# from bisect import bisect_left, bisect_right

# n = int(sys.stdin.readline().rstrip())
# cards = list(map(int, sys.stdin.readline().rstrip().split()))
# m = int(sys.stdin.readline().rstrip())
# targets = list(map(int, sys.stdin.readline().rstrip().split()))

# cards.sort()

# for target in targets:
#     left = bisect_left(cards, target)
#     right = bisect_right(cards, target)
#     print(right - left, end=' ')


# import sys

# N = int(sys.stdin.readline().strip())
# cards = list(map(int, sys.stdin.readline().strip().split()))
# cards_dict = {}
# for card in cards:
#     if card in cards_dict:
#         cards_dict[card] += 1
#     else:
#         cards_dict[card] = 1

# M = int(sys.stdin.readline().strip())
# check_list = list(map(int, sys.stdin.readline().strip().split()))

# for check in check_list:
#     if check in cards_dict:
#         print(cards_dict[check], end=' ')
#     else:
#         print(0, end=' ')


import sys
N = int(sys.stdin.readline().strip())
cards1 = list(map(int, sys.stdin.readline().strip().split()))
# print(N)
# print(cards1)
cards_dict = {}
for card in cards1:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1
    
M = int(sys.stdin.readline().strip())
cards2 = list(map(int, sys.stdin.readline().strip().split()))

for i in cards2:
    if i in cards_dict:
        print(cards_dict[i], end =' ')
    else:
        print(0, end=' ')
print()


# # 입력 받기
# N = int(input())
# cards1 = list(map(int, input().split()))
# cards1.sort()
# M = int(input())
# cards2 = list(map(int, input().split()))

# # 이진 탐색 함수 구현
# def binary_search(arr, target, left, right):
#     left_idx, right_idx = None, None
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             if mid == 0 or arr[mid-1] != target:
#                 left_idx = mid
#                 break
#             right = mid - 1
#         elif arr[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             if mid == len(arr)-1 or arr[mid+1] != target:
#                 right_idx = mid
#                 break
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     return left_idx, right_idx

# # 이진 탐색을 이용하여 등장 횟수 계산
# count_cards = []
# for target in cards2:
#     left_idx, right_idx = binary_search(cards1, target, 0, len(cards1)-1)
#     if left_idx is None or right_idx is None:
#         count_cards.append(0)
#     else:
#         count_cards.append(right_idx - left_idx + 1)

# # 출력
# print(' '.join(map(str, count_cards)))
