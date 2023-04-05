# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# #################### 퀵정렬 실패
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

##############################
# 계수 정렬
import sys      # 빨리 받을라고

sort_list = [0]*10001       # 1~10000까지의 숫자가 주어지므로 10001까지 인덱스가 있는 리스트 생성
N = int(sys.stdin.readline().rstrip())
for i in range(N):          # N의 갯수 만큼 받음
    sort_list[int(sys.stdin.readline().rstrip())] += 1      # 만들어둔 sort_list에 입력받음
for i in range(10001):                  # 10001 즉, 0~10000 까지 돌리면서 확인
    if sort_list[i] !=0:                # sort_list[i]가 0이 아니면 값이 있으면
        for j in range(sort_list[i]):   # sort_list[i]의 값만큼 반복해서 i를 출력하기
            print(i)