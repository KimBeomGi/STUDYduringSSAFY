# 문제
# 주몽은 철기군을 양성하기 위한 프로젝트에 나섰다. 그래서 야철대장을 통해 철기군이 입을 갑옷을 만들게 하였다. 야철대장은 주몽의 명에 따르기 위하여 연구에 착수하던 중 아래와 같은 사실을 발견하게 되었다.

# 갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다. 갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다. 야철대장은 자신이 만들고 있는 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 궁금해졌다. 이러한 궁금증을 풀어 주기 위하여 N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 재료의 개수 N(1 ≤ N ≤ 15,000)이 주어진다. 그리고 두 번째 줄에는 갑옷을 만드는데 필요한 수 M(1 ≤ M ≤ 10,000,000) 주어진다. 그리고 마지막으로 셋째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다. 고유한 번호는 100,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 갑옷을 만들 수 있는 개수를 출력한다.

#####################
# 완탐
# import sys

# N =int(sys.stdin.readline().strip())
# M =int(sys.stdin.readline().strip())
# materials = list(map(int, sys.stdin.readline().strip().split()))
# armor = 0
# for i in range(N-1):
#     for j in range(i+1,N):
#         if materials[i] + materials[j] == M:
#             armor += 1

# print(armor)


#################################
# 조합
# import sys
# from itertools import combinations

# N =int(sys.stdin.readline().strip())
# M =int(sys.stdin.readline().strip())
# materials = list(map(int, sys.stdin.readline().strip().split()))
# armor = 0
# # print(combinations(materials,2))
# for combination in combinations(materials,2):
#     if sum(combination) == M:
#         armor += 1
# print(armor)


# n = int(input())
# m = int(input())
# arr = list(map(int, input().split()))

# arr.sort()  # 배열 정렬
# count = 0  # 쌍의 개수를 저장할 변수 초기화
# left, right = 0, n-1  # 시작 위치 설정

# while left < right:
#     s = arr[left] + arr[right]
#     if s == m:
#         count += 1
#         left += 1
#         right -= 1
#     elif s < m:
#         left += 1
#     else:
#         right -= 1

# print(count)


# 이진탐색을 응용해봤다.
import sys

N =int(sys.stdin.readline().strip())
M =int(sys.stdin.readline().strip())
materials = list(map(int, sys.stdin.readline().strip().split()))
armor = 0
materials.sort()
left = 0
right = N-1
while left < right:     # 같아지면 1개가 되니까
    product = (materials[left] + materials[right])      # 비교하기 위함
    
    if product == M:    # M과 같은 값이면
        armor += 1      # 갑옷 생산 1개
        left += 1       # 다른 값 찾아야하니 left를 오른쪽으로 한칸
        right -= 1      # right는 왼쪽으로 한칸
    elif product < M:
        left += 1       # 찐 이진 탐색이면 left를 mid뒤로 옮겼겠지만 이건 하나씩 탐색하는 거니까
    elif product > M:
        right -= 1       # 찐 이진 탐색이면 right를 mid앞로 옮겼겠지만 이건 하나씩 탐색하는 거니까

print(armor)