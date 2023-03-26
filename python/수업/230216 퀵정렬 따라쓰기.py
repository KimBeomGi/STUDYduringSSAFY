# 퀵정렬
arr = [5,1,8,6,7,9,0,2,4,3]

def partition(start, end, arr):                     # 파티션 함수를 만들어서 분할정복을 하기 위함
    pivot = arr[start]                              # pivot이라는 위치를 만들어서 pivot기준으로 분할하기 위함
    i = start                                       # arr의 첫 위치 인자인 [0] 을 의미
    j = end                                         # arr의 끝 위치 인자인 [-1] 을 의미
    while i<=j:                                     # i가 j보다 작거나 같은 경우에만 반복
        while i <= j and arr[i] <= pivot:           # arr[i]값이 pivot보다 작다면, i가 j보다 작거나 같은 경우에만 반복
            i += 1                                  # i에 +1을 하면서 pivot 보다 크게 되는 경우를 찾음
        while i <= j and arr[j] > pivot:            # arr[j]값이 pivot보다 크다면, i가 j보다 작거나 같은 경우에만 반복
            j -= 1                                  # j에 -1을 하면서 pivot 보다 작게 되는 경우를 찾음
        if i < j:                                   # 두 while문을 실행했는데 i < j면 아직 완벽히 찾은 것은 아니니까
            arr[i], arr[j] = arr[j], arr[i]         # arr[i]와 arr[j]의 위치를 바꿔준다.
    # 첫 while문이 끝나면 i>=j가 된 것이므로 첫 start의 값과 j의 값을 바꿔주면 pivot이 들어가줘야 할 곳에 들어가주게 됨
    arr[start], arr[j] = arr[j], arr[start]

    return j                                        # pivot의 위치인 j를 반환

def quick_sort(start, end):
    if start >= end:                                # 만약 start >= end면 마지막 정렬이 된 것이므로
        return                                      # 반환하기

    # partition 수행
    pivot = partition(start, end, arr)                   # partition함수를 수행함으로 pivot의 위치를 재정의
    quick_sort(start, pivot-1)                      # pivot 기준 앞쪽의 값을 퀵정렬하기
    quick_sort(pivot+1, end)                        # pivot 기준 뒤쪽의 값을 퀵정렬하기

N = len(arr)
quick_sort(0, N-1)                                  # 첫 인덱스와 마지막 인덱스를 quick_sort 함수에 기입
print(arr)

        