import sys
sys.stdin = open('2230329 5204 병합정렬.txt', 'r')

# [문제풀이]
# 0. left = L[0:N//2], right = L[(N//2):N] 로 슬라이싱으로 구분해준다.
# 1. 모든 정렬이 끝난 뒤 L[N//2]원소를 출력하도록 한다.
# 2. 병합정렬을 이용해야한다.


# # 각 왼쪽 오른쪽 나눠진 조각들을 합치는 작업
# def merge(left, right):
#     global count                                    # 글로벌 변수를 사용
#     merged_array = []                               # 합치면서 정렬하기위해 만들어진 리스트
#     if left[-1] > right[-1]:                        # 문제 답 출력을 위해 왼쪽의 끝 값이 오른쪽 끝 값보다 크면
#         count +=1                                   # count +1 해주기
#     # 왼쪽 오른쪽 합체!
#     while left and right:                           # 왼쪽 오른쪽 둘다 값이 있으면 반복
#         if left[0] < right[0]:                      # 왼쪽의 0가 오른쪽 0보다 작으면
#             merged_array.append(left.pop(0))        # 왼쪽의 0를 빼서 merged_array에 추가
#         else:                                       # 왼쪽의 0가 오른쪽 0보다 크면
#             merged_array.append(right.pop(0))       # 오른쪽의 0를 빼서 merged_array에 추가

#     # 합체하려했는데 한쪽 없으면???
#     while left:                                     # 왼쪽이 있으면
#         merged_array.append(left.pop(0))            # 왼쪽거 순서대로 넣기
#     while right:                                    # 오른쪽이 있으면
#         merged_array.append(right.pop(0))           # 오른쪽거 순서대로 넣기
#     return merged_array                             # 다 넣었으니 합체시킨 merged_array를 뱉어내기

# # 정렬을 하기 위한 사전 작업(쪼개기)
# def merge_sort(array):
#     if len(array) ==1:                              # 끝까지 쪼개서 인자가 1개만 남았으면?
#         return array                                # 해당 인자를 담은 리스트를 뱉어냄
#     # return하고 나면 아래 left = merge_sort(left)의 left가 되거나
#     # right= merge_sort(right)의 right가 됨
    
#     middle = len(array)//2                          # 중간을 정의
#     left = array[:middle]                           # 왼쪽은 중앙의 왼쪽
#     right = array[middle:]                          # 오른쪽은 중앙부터 오른쪽

#     left = merge_sort(left)                         # 왼쪽에 대해서 다시 나누기
#     right= merge_sort(right)                        # 오른쪽에 대해서 다시 나누기

#     return merge(left, right)                       # 구해진 left와 right를 합체해주기

# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())                                # 갯수 N
#     array = list(map(int, input().split()))         # 리스트로 입력받기
#     count = 0                                       # 문제의 답을 출력시키기 위한 count
#     array = merge_sort(array)                       # 병합정렬 실시!
#     print(f'#{testcase} {array[N//2]} {count}')

#########################################

# 각 왼쪽 오른쪽 나눠진 조각들을 합치는 작업
# def merge(array, start, middle, end):
#     global count
#     temp = []
#     i = start                               # 왼쪽 값은 start ~ middle
#     j = middle + 1                          # 오른쪽 값은 middle+1 ~ end
#     if array[middle] > array[end]:          # 문제 답 출력을 위해 왼쪽의 끝 값이 오른쪽 끝 값보다 크면
#         count += 1                          # count +1 해주기
    
#     # 왼쪽 오른쪽 합체!
#     while i <= middle and j <= end:         # i가 middle보다 작고, j가 끝위치보다 작을때(즉. 왼쪽 오른쪽 부분의 각 [0]~[-1]을 확인함
#         if array[i] < array[j]:             # array[i]가 array[j]보다 작다면
#             temp.append(array[i])           # temp에 array[i](왼쪽의 값)를 추가
#             i += 1                          # 그리고 왼쪽 부분은 다음 인자 확인하기
#         else:                               # array[i]가 array[j]보다 크거나 같다면
#             temp.append(array[j])           # temp에 array[j](오른쪽의 값)를 추가
#             j += 1                          # 그리고 오른쪽 부분은 다음 인자 확인하기
#     # 합체하려했는데 한쪽 없으면???
#     while i <= middle:                      # 왼쪽 값만 가능할때
#         temp.append(array[i])               # 하나씩 넣어주자
#         i += 1
#     while j <= end:                         # 오른쪽 값만 가능할때
#         temp.append(array[j])               # 하나씩 넣어주자
#         j += 1
#     x = 0                                   # array에 temp에 넣어준 값을 대입하기 위해 사용될 인자 x
#     for i in range(start,end+1):            # start~end까지
#         array[i] = temp[x]                  # 예로 array[0]~[N-1]까지 temp[0]~[N-1]의 값을 각 대입해줌
#         x += 1

# # # 정렬을 하기 위한 사전 작업(쪼개기)
# def merge_sort(array, start, end):
#     if start == end:
#         return
    
#     middle = (start + end) // 2                # 중간값 인자는 (start+end)//2
#     merge_sort(array, start, middle)           # 왼쪽 쪼개기
#     merge_sort(array, middle+1, end)           # 오른쪽 쪼개기
#     merge(array, start, middle, end)           # 왼쪽 오른쪽 합체!


# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())                                # 갯수 N
#     array = list(map(int, input().split()))         # 리스트로 입력받기
#     count = 0                                       # 문제의 답을 출력시키기 위한 count
#     merge_sort(array, 0, N-1)                       # 병합정렬 실시!
#     print(f'#{testcase} {array[N//2]} {count}')


###################################################


# 각 왼쪽 오른쪽 나눠진 조각들을 합치는 작업
def merge(left, right):
    global count                                    # 글로벌 변수를 사용
    merged_array = []                               # 합치면서 정렬하기위해 만들어진 리스트
    if left[-1] > right[-1]:                        # 문제 답 출력을 위해 왼쪽의 끝 값이 오른쪽 끝 값보다 크면
        count +=1                                   # count +1 해주기
    # 왼쪽 오른쪽 합체!
    i = 0                                           # 왼쪽 조각에서 사용될 인자
    j = 0                                           # 오른쪽 조각에서 사용될 인자
    l_l = len(left)
    l_r = len(right)
    # 참고로 여기서 사용되는 것은 인자이므로 i <= l_l이나 j <= l_r이 되면 INDEX ERROR가 뜬다.
    while i < l_l and j < l_r:                      # i와 j인자가 리스트를 벗어나지 않을때만 반복
        if left[i] < right[j]:                      # left[i]가 left[j]보다 작으면
            merged_array.append(left[i])            # left[i]값을 merged_array에 추가
            i+=1
        else:                                       # left[i]가 left[j]보다 크거나 같으면
            merged_array.append(right[j])           # right[j]값을 merged_array에 추가
            j+=1

    # 합체하려했는데 한쪽 없으면???
    while i < l_l :                                 # 왼쪽이 있으면(i가 왼쪽 조각의 끝을 안넘었으니까)
        merged_array.append(left[i])                # 왼쪽거 순서대로 넣기
        i+=1
    while j < l_r :                                 # 오른쪽이 있으면(j가 오른쪽 조각의 끝을 안넘었으니까)
        merged_array.append(right[j])               # 오른쪽거 순서대로 넣기
        j+=1
    return merged_array                             # 다 넣었으니 합체시킨 merged_array를 뱉어내기

# 정렬을 하기 위한 사전 작업(쪼개기)
def merge_sort(array):
    if len(array) ==1:                              # 끝까지 쪼개서 인자가 1개만 남았으면?
        return array                                # 해당 인자를 담은 리스트를 뱉어냄
    # return하고 나면 아래 left = merge_sort(left)의 left가 되거나
    # right= merge_sort(right)의 right가 됨
    
    middle = len(array)//2                          # 중간을 정의
    left = array[:middle]                           # 왼쪽은 중앙의 왼쪽
    right = array[middle:]                          # 오른쪽은 중앙부터 오른쪽

    left = merge_sort(left)                         # 왼쪽에 대해서 다시 나누기
    right= merge_sort(right)                        # 오른쪽에 대해서 다시 나누기

    return merge(left, right)                       # 구해진 left와 right를 합체해주기

T = int(input())
for testcase in range(1, T+1):
    N = int(input())                                # 갯수 N
    array = list(map(int, input().split()))         # 리스트로 입력받기
    count = 0                                       # 문제의 답을 출력시키기 위한 count
    array = merge_sort(array)                       # 병합정렬 실시!
    print(f'#{testcase} {array[N//2]} {count}')