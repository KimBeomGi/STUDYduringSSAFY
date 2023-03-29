# 1. 파티션 나누기(pivot을 기준으로 작은 값/큰값으로 나누기)
# 2. 나뉘어진 작은 값들과 큰 값들을 각각 퀵정렬

def partition(arr, s, e):    # 피벗을 기준으로 값 나누고, 피벗위치 반환
    # 임의의 피벗을 설정하고
    # 피벗을 기준으로 값 나누기
    pivot = arr[s]
    i = s
    j = e
    # i는 pivot보다 큰값을 찾을 때까지 오른쪽으로 이동
    # j는 pivot보다 작은값을 찾을 때까지 왼쪽으로 이동
    # i와 j의 위치가 역전되지 않았으면, 교환하기
    # 위 작업을 계속 반복, i와 j가 위치가 역전이 되면
    # pivot이랑 j(작은 애들 중에 제일 뒤에 있는 애의 위치)랑 위치를 교환
    while i<= j:
        while i<=j and arr[i] <= pivot:      # 큰 값찾으러 가는 중
            i += 1
        while i<=j and arr[j] <= pivot:      # 작은 값 찾으러 가는 중
            j -= 1
        # i가 가리키는 큰값이 j가 가리키는 작은값보다 앞에 있으면 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # i와 j의 위치가 역전됨, j의 위치가 작은애들중에 제일 마지막 위치
    arr[s], arr[j] = arr[j], arr[s]
    return j        # pivot의 위치가 j


# s,e: 퀵정렬을 수행할 영역

def quick_sort(arr, s, e):
    if s < e:                           # 정렬해야할 요소가 2개 이상일때만 정렬
        p_idx = partition(arr, s,e)
        quick_sort(arr, s, p_idx - 1)
        quick_sort(arr, p_idx + 1, e)



T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick_sort(arr, 0, N-1)                 # 처음부터 끝까지 정렬
    print(f'#{testcase} {arr[N//2]}')