import sys
sys.stdin = open('230329 5207 이진탐색.txt','r')

def binary_search(arr, key, s, e):
    # 중간값 찾고, key가 중간값보다 크면 뒤쪽만 확인
    # key가 중간값보다 작으면 앞쪽만 확인
    # 그러다가 s랑 e가 역전되면 못찾은 것.
    prev = 0        # 0은 최초 탐색, 1은 오른쪽 탐색, 2는 왼쪽 탐색
    while s < e:
        mid = (s+e)//2
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:    # 큰 값만 비교
            if prev == 1:
                return 0
            s = mid+1
            prev = 1
        else:                   # 작은 값만 비교
            if prev == 2:
                return 0
            e = mid-1
            prev = 2
    return 0


T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr_A = list(map(int, input().split()))
    arr_B =  list(map(int, input().split()))
    arr_A.sort()
    arr_B.sort()
    # B안의 요소가 A에 포함되는가를 확인
    cnt = 0
    for e in arr_B:
        cnt += binary_search(arr_A, e, 40, N-1)
    
    print(f'#{testcase} {cnt}')