# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# import sys

# def binary_search(arr, target):
#     left = 0
#     right = len(arr)-1

#     while left <= right:
#         mid = (left+right)// 2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             left = mid +1
#         elif arr[mid] > target:
#             right = mid-1
#     return False

# N = int(sys.stdin.readline().strip())
# A = list(map(int, sys.stdin.readline().strip().split()))
# M = int(sys.stdin.readline().strip())
# B = list(map(int, sys.stdin.readline().strip().split()))
# A.sort()

# for i in B:             # B요소를 i로 반복
#     result = binary_search(A, i)
#     if result == False:
#         print(0)
#     else:
#         print(1)


# 이진 탐색!
import sys

def binary_search(array, key):
    left = 0
    right = len(array)-1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == key:
            return True
        elif array[middle] > key:
            right = middle - 1
        elif array[middle] < key:
            left = middle + 1
    return False

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().strip().split()))
A.sort()

for i in B:             # B요소를 돌아가면서
    result = binary_search(A, i)
    if result == True:
        print(1)
    else:
        print(0)