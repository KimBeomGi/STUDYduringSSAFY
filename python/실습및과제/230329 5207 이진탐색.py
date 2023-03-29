import sys
sys.stdin = open('230329 5207 이진탐색.txt','r')

# [문제풀이]
# 0. A와 B라는 리스트 2개가 주어질 때 B의 인자 몇개가 A안에 들어있는지 확인하는 요소이다.
# 0-1. 따라서 key는 B의 인자가 되고 이진검색을 하게 될 곳은 A리스트가 된다.

# def binary_search(start, end, key):
#     k = False
#     middle = (start+end)//2                     # 중간값 설정
#     if A[middle] == key:                        # 키 값이 중간값과 같다면
#         k = True
#         return k
#     elif key < A[middle]:                       # 키 값이 중간값 보다 작다면
#         if start <= middle-1:
#             return binary_search(start, middle-1, key)
    
#     elif key > A[middle]:                       # 키 값이 중간값 보다 크다면
#         if end >= middle+1:
#             return binary_search(middle+1, end, key)
#     return k
def binary_search(array,start, end, key):
    prev = 0
    while start <= end:
        middle = (start+end)//2
        if array[middle] == key:
            return 1
        
        elif array[middle] < key:                   # A[middle]값이 키보다 작으면
            if prev == 1:
                return 0
            start = middle+1
            prev = 1
        else:                                   # A[middle]값이 키보다 크면면
            if prev == 2:
                return 0
            end = middle-1
            prev = 2
    return 0
        
T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())                # 각 리스트 A와 B의 길이
    A = sorted(list(map(int, input().split())))     # B의 인자를 찾을 A 리스트
    B = sorted(list(map(int, input().split())))             # A 리스트에서 key값으로 쓰일 B리스트
    count = 0
    for b in B:                                     # B의 인자를 이용해 반복
        count += binary_search(A,0, N-1, b)           # answer에 return값 출력
    
    print(f'#{testcase} {count}')