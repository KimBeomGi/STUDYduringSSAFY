# 1. 정렬된 두 배열을 합치는 과정 - merge()
# 2. 정렬된 배열을 반환하는 함수 - merge_sort()

def merge(arr, s, m, e):
    # s~m : 왼쪽
    # m+1 ~ e: 오른쪽
    temp = []
    i = s
    j = m+1
    # 두 부분 비교해서 작은 거 복사
    while i <= m and j<= e:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= m:
        temp.append(arr[i])
        i += 1
    while j <= e:
        temp.append(arr[j])
        j += 1
    # 임시로 만든 정렬된 요소들을 원래 배열에 복사해주긴
    x = 0
    for i in range(s, e+1):
        arr[i] = temp[x]
        x += 1

# s : 정렬할 범위의 첫 인덱스
# e : 정렬할 범위의 끝 인덱스

def merge_sort(arr,s,e):
    if s==e:    # 정렬해야하는 범위가 1>> 나눠서 정렬할 필요가 없음.
        return
    # 절반나눠서 각각 정렬
    # 각각 정렬된 부분을 합치기
    mid = (s+e)//2
    # left : s ~ mid, right : mid+1 ~ e
    merge_sort(arr, s, mid)         # 왼쪽 정렬
    merge_sort(arr, mid + 1, e)     # 오른쪽 정렬
    merge(arr, s, mid, e)           # 합치기

arr = [5,2,3,7,1,0,6,8,4,9]
merge_sort(arr, 0 ,len(arr)-1)
print(arr)