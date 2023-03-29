# 1. 정렬된 두 배열을 합치는 과정 - merge()
# 2. 정렬된 배열을 반환하는 함수 - merge_sort()

def merge(left, right):
    # 정렬된 것들 합치기
    merged_arr = []
    while left and right:           # 아직 둘다 요소가 남아있으니까
        if left[0] < right[0]:
            merged_arr.append(left.pop(0))
        else:
            merged_arr.append(right.pop(0))

    # 둘 중 하나라도 없으면 남은 쪽 순서대로 붙여주기
    while left:
        merged_arr.append(left.pop(0))
    while right:
        merged_arr.append(right.pop(0))
    return merged_arr


def merge_sort(arr):
    # 요소가 하나가 남으면.. 자르는 작업이 필요가 없음
    # 이미 정렬이 된 상태니까...
    if len(arr) == 1:
        return arr
    # 전체를 절반으로 나누어서 각각 정렬 뒤 합침
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    # left와 right는 각가 정령이 안된 상태
    
    # merge_sort 함수를 이용해서 각각 정렬
    left = merge_sort(left)
    right = merge_sort(right)
    # 3 4 1 5
    # 자르다 보면 결국 요소가 하나가 남을 건데..
    # 요소가 하나인 배열은 정렬 되었다.
    return merge(left, right)       # 정렬된 2개의 배열을 합쳐서 반환

arr = [5,2,3,6,1,2,7,8,4,9]
print(merge_sort(arr))