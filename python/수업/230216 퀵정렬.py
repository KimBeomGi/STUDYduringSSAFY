# partition파티션: 기준을 잡고 작은값과 큰값으로 구분
# quick_sort: 나뉘어진 작은 값들과 큰 값들을 또 각각 같은 작업을 반복

# arr = [6,3,2,1,4,5,9,7,8]
arr = [5,1,8,6,7,9,0,2,4,3]
# 여기서 arr은 global로 사용하려고 def 매개변수에 쓰지 않음

def partition(start, end):
    pivot = arr[start]
    i = start
    j = end
    while i <= j:
        # i는 1씩 증가하면서 pivot보다 큰값찾기
        # j는 1씩 감소하면서 pivot보다 작은값찾기
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        # 찾으면 교환하는데 단, i가 j보다 작을 때만
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 교환이 끝났으면 pivot 자리 잡아주기
    arr[start], arr[j] = arr[j], arr[start]

    # pivot의 위치를 반환
    # 임의의 값 x를 잡아서, x보다 큰값과 작은값으로 나누어주기
    # pivot의 위치를 반환
    return j

def quick_sort(start, end):
    # 만약에 정렬하는 구간의 길이가 1 이라면 요소가 하나라면 아무 작업도 안함(# 기저영역 설정!!!)
    if start >= end:        # start와 end가 같으면 길이가 1이나 다름없으므로
        return
    # partition을 수행
    pivot = partition(start, end)
    # 수행 결과로 나온 pivot을 기준으로
    # 왼쪽과 오른쪽 부분을 별도로 각각 정렬 수행(# 재귀함수 수행!!)
    quick_sort(start, pivot-1)
    quick_sort(pivot+1, end)

N = len(arr)
quick_sort(0, N-1)
print(arr)