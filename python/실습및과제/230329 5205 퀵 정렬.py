# import sys
# sys.stdin = open('230329 5205 퀵 정렬.txt','r')


def quick_sort(array, left, right):
    if left >= right:
        return

    # 인덱스 정의
    i = left
    j = right
    # 피봇은?! array[N//2]가 아닌 이유는 재귀 쓸 거임
    pivot = array[(left + right) // 2]
    # 왼쪽
    while i<= j:            # 왼쪽 인덱스가 오른쪽 인덱스보다 작을때 까지 진행
        while array[i] < pivot:     # 왼쪽에 있는 값이 pivot 보다 작다면
            i += 1                  # i에 +1 해주기
        while array[j] > pivot:     # 오른쪽에 있는 값이 pivot 보다 크다면
            j -= 1                  # j에 -1 해주기
        if i <= j:                  # 위 2개의 while문 이후에 i가 j보다 작다면(역전되지 않은 상태)
            array[i], array[j] = array[j], array[i]     # 값을 바꿔주기
            i += 1                  # 값을 바꿔줬으니 i에 1을 더해 다음 값을 확인하고
            j -= 1                  # 값을 바꿔줬으니 j에 1을 빼서 다음 값을 확인하기
    
    # 여기까지 온 것은 i와j가  역전되었음을 의미
    quick_sort(array,left, j)       # 피벗값을 기준으로 정해진 곳의 왼쪽에 대해서 퀵 정렬
    quick_sort(array, i, right)     # 피벗값을 기준으로 정해진 곳의 오른쪽에 대해서 퀵 정렬


T = int(input())
for testcase in range(1,T+1):
    N = int(input())                        # 정수의 갯수 N
    array = list(map(int, input().split())) # 배열 생성
    quick_sort(array, 0, N-1)               # 퀵 정렬 시작
    # print(array)
    print(f'#{testcase} {array[N//2]}')     # 출력

# [5,1,3,4,2]
# 5
# 2
# [5,1,3,4,2,6]
# 6
# 3