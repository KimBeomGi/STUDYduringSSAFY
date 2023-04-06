# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# import sys      # 빨리 받을라고

# sort_list = [0]*10001       # 1~10000까지의 숫자가 주어지므로 10001까지 인덱스가 있는 리스트 생성
# N = int(sys.stdin.readline().rstrip())

# for _ in range(N):
#     a = int(sys.stdin.readline().rstrip())
#     sort_list[a] += 1

# # 정렬하기
# for i in range(10001):  # sort_list를 돌리기 위함
#     if sort_list[i] > 0:
#         for _ in range(sort_list[i]):
#             print(i)


# # 퀵 정렬 이용하기

# import sys

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#         left = []
#         right = []
#         for i in range(1, len(array)):
#             if array[i] < pivot:
#                 left.append(array[i])
#             else:
#                 right.append(array[i])
#         return quick_sort(left) + [pivot] + quick_sort(right)


# N = int(sys.stdin.readline().rstrip())
# problem = []
# for i in range(N):
#     problem.append(int(sys.stdin.readline().rstrip()))

# sorted_problem = quick_sort(problem)

# for i in range(N):
#     print(sorted_problem[i])


# # 병합정렬 이용하기
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2
#     left_arr = arr[:mid]
#     right_arr = arr[mid:]

#     left_arr = merge_sort(left_arr)
#     right_arr = merge_sort(right_arr)
    
#     return merge(left_arr, right_arr)

# def merge(left_arr, right_arr):
#     result = []
#     left_idx, right_idx = 0, 0
#     while left_idx < len(left_arr) and right_idx < len(right_arr):
#         if left_arr[left_idx] <= right_arr[right_idx]:
#             result.append(left_arr[left_idx])
#             left_idx += 1
#         else:
#             result.append(right_arr[right_idx])
#             right_idx += 1
    
#     if left_idx < len(left_arr):
#         result.extend(left_arr[left_idx:])
#     else:
#         result.extend(right_arr[right_idx:])

#     return result

# import sys

# N = int(sys.stdin.readline().strip())
# problem = []
# for i in range(N):
#     problem.append(int(sys.stdin.readline().strip()))

# problem = merge_sort(problem)
# # print(problem)

# for i in problem:
#     print(i)


import sys

N = int(sys.stdin.readline().strip())
problem = []
for i in range(N):
    problem.append(int(sys.stdin.readline().strip()))

problem.sort()
# print(problem)
for i in range(N):
    print(problem[i])