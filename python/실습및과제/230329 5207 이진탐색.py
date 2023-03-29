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


def binary_search(start, end, key):
    global temp
    while start <= end:
        middle = (start+end)//2
        if A[middle] == key:
            return True
        
        elif A[middle] < key:                   # A[middle]값이 키보다 작으면
            start = middle+1
            temp.append('r')
        else:                                   # A[middle]값이 키보다 크면면
            end = middle-1
            temp.append('l')
    return False
        
T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())                # 각 리스트 A와 B의 길이
    A = sorted(list(map(int, input().split())))     # B의 인자를 찾을 A 리스트
    B = list(map(int, input().split()))             # A 리스트에서 key값으로 쓰일 B리스트
    count = 0
    temp = []
    for b in B:                                     # B의 인자를 이용해 반복
        isit = True
        answer = binary_search(0, N-1, b)           # answer에 True 또는 False 입력
        # if answer:                                  # 값이 0이 아니라면
        #     # isit = True
        #     if len(temp)>2:
        #         for i in range(len(temp)-1):
        #             if temp[i] == temp[i+1]:
        #                 isit = False
        if answer and isit:
            count += 1
    
    print(f'#{testcase} {count}')

    # print(binary_search(0,N-1,2))