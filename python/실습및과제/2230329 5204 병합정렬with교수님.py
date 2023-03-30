import sys
sys.stdin = open('2230329 5204 병합정렬.txt', 'r')

# def merge_sort(arr):
#     global count

#     if len(arr) == 1:
#         return arr
#     # arr을 절반씩 left와 right를 나누어서 각각 정렬
#     # 나누어진 left와 right를 합병
#     # 합쳐진 배열을 반환
    
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     # left와 right 합병하기
#     result = []
#     while left and right:       # 둘다 요소가 남아있으면
#         # 가장 앞요소 비교해서 더 작은 것 결과 배열에 추가하기
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     if left:
#         count += 1
#         result.extend(left)
#     if right:
#         result.extend(right)
#     return result


# T = int(input())
# for testcase in range(1,T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     count = 0
#     arr = merge_sort(arr)
#     print(f'#{testcase} {arr[N//2]} {count}')


###########################


def merge_sort2(arr, s, e):
    global cnt
    if s >= e:
        return
    # arr을 절반씩 left와 right로 나누어서 각각 정렬
    # 나누어진 left와 right를 합병
    # 합쳐진 배열을 반환
    mid = (s + e + 1) // 2
    merge_sort2(arr, s, mid-1)
    merge_sort2(arr, mid, e)
    # left와 right합병하기
    i = s
    j = mid
    tmp = []
    if arr[mid-1] > arr[e]:
        cnt += 1
    while i < mid and j < e + 1:  # 둘다 요소가 남아있으면
        # 가장 앞요소 비교해서 더 작은거 결과 배열에 추가하기
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i < mid:
        tmp.append(arr[i])
        i += 1
    while j < e + 1:
        tmp.append(arr[j])
        j += 1
    j = 0
    for i in range(s,e+1):
        arr[i] = tmp[j]
        j += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    # arr = merge_sort(arr)
    merge_sort2(arr,0,N-1)
    # print(arr)
    print(f'#{tc} {arr[N // 2]} {cnt}')