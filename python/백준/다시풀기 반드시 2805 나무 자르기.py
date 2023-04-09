# 문제
# 상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

# 목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

# 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

# 출력
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.


# # 이진 탐색을 이용해서 풀기
# import sys

# N, M = map(int, sys.stdin.readline().strip().split())
# trees = list(map(int, sys.stdin.readline().strip().split()))
# # tree - saw 하기.

# # left와 right, middle 모두 높이 
# left = 0                # 0
# right = max(trees)      # right는 가장 높은 나무의 길이
# max_middle = 0
# while left <= right:
#     middle= (left+right)//2     # 중앙 값을 만들어주자.
    
#     value = 0                   # 생성된 나무길이를 더할 수 있는 value 변수
#     for tree in trees:          # 각 나무별 확인하는데
#         tmp = tree-middle       # tree-middle 값이 목재 길이니까
#         if tree-middle < 0:     # 만약 더 작으면 안자른게 되니까
#             tmp = 0
#         value += tmp            # value값에 생성된 목재길이 더해주기
    
#     if M == value:              # 가져가려는 값과 같다면
#         if max_middle < middle:
#             max_middle = middle
#         left = middle +1
#     elif M > value:             # 가져가려는 값보다 작다면
#         right = middle -1       # 목재절단기 높이를 낮게해서 더 길게 자르기
#     elif M < value:             # 가져가려는 값보다 크다면
#         left = middle +1        # 목재절단기 높이를 높여서 더 짧게 자르기
# print(max_middle)




# import sys
# # 입력 받기
# n, m = map(int, sys.stdin.readline().strip().split())
# trees = list(map(int, sys.stdin.readline().strip().split()))

# # 이분 탐색을 위한 시작점과 끝점 설정
# bottom, top = 1, max(trees)

# # 이분 탐색 시작
# while bottom <= top:
#     mid = (bottom + top) // 2
#     total = 0
    
#     # mid 높이에서 잘린 나무 길이의 합 계산
#     for tree in trees:
#         if tree > mid:
#             total += tree - mid
    
#     # 나무 길이의 합이 m보다 크거나 같으면 높이를 높여야 함
#     if total >= m:
#         bottom = mid + 1
#     # 나무 길이의 합이 m보다 작으면 높이를 낮춰야 함
#     else:
#         top = mid - 1

# # 결과 출력
# print(top)



# 이진탐색이용, 함수로 사용

def find():
    # bottom과 top은 절단기가 갈 수 있는 구간
    bottom = 0
    top = max(trees)

    while bottom <= top:                    # 역전하면 못찾음
        middle = (bottom + top) // 2        # 중앙값을 생성
        result = 0                          # 결과는?
        for tree in trees:                  # 나무 한그루당 보는데
            if result >= M:                 # 결과값이 M보다 커지면 더 검사할 필요가 엄서
                break
            if tree > middle:               # 나무가 middle보다 크면
                result += tree - middle     # result에 기입하기

        if result >= M:                     # result가 M보다 더 크거나 같으면
            bottom = middle + 1             # 더 높이 잘라볼까?
        elif result < M:                    # result가 Mqhek 더 작으면
            top = middle - 1                # 더 낮게 잘라야지
    return top                              # 끝까지 확인했으니 top을 자르면 되겠군

N, M = map(int, input().split())

trees = list(map(int, input().split()))

print(find())


# ############
# # 이방법도 있네??
# N, M=map(int, input().split()) 
# X=list(map(int, input().split()))

# s=1
# e=max(X)

# while s<=e :
#     a=0
#     c=(s+e)//2
#     for i in X :
#         if i>=c : a+=i-c

#     if a>=M : s=c+1
#     else : e=c-1

# print(e)