'''
# 거품 정렬
arr = [5,6,1,3,4,7,9,8,2]
N = 9
# 두 개 비교해서 뒤로 보내기
for _ in range(N-1):
    for i in range(0,N-1):
        if arr[i]> arr[i+1]:        # 앞에 애가 더 크면 자리 바꿔야하니까
            arr[i], arr[i+1] = arr[i+1], arr[i]         # ,로 구분되어있으므로 튜플

print(arr)

# 거품 정렬
arr = [5,6,1,3,4,7,9,8,2]
N = 9
# 두 개 비교해서 뒤로 보내기
for j in range(N-1):
    for i in range(0, N-1-j):       # 맨 마지막은 이미 완료 되었으니, j번 덜 돌아도 됨 
        if arr[i]> arr[i+1]:        # 앞에 애가 더 크면 자리 바꿔야하니까
            arr[i], arr[i+1] = arr[i+1], arr[i]         # ,로 구분되어있으므로 튜플

print(arr)
'''
'''
# 선택 정렬
# 제일 앞쪽부터 인덱스[0]에 들어갈 숫자를 찾아서 집어넣고,
# 그다음 인덱스[1]에 들어갈 숫자를 찾아서 집어넣고를 반복.
# → 제일 작은애 선택해서 자리에 넣어주기
arr = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N=9
# 제일 작은 애 위치 찾기
min_idx = 0         # 일단 그냥 제일 앞 녀석이 작은 것으로 치자
for i in range(N):
    if arr[i] < arr[min_idx]:
        min_idx = i
# 제일 작은애의 위치 min_idx
arr[0], arr[min_idx] = arr[min_idx], arr[0]

print(arr)

arr = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N=9
# 제일 작은 애 위치 찾기
min_idx = 1         # 일단 그냥 제일 앞 녀석이 작은 것으로 치자
for i in range(1,N):
    if arr[i] < arr[min_idx]:
        min_idx = i
# 제일 작은애의 위치 min_idx
arr[1], arr[min_idx] = arr[min_idx], arr[1]

print(arr)
'''
'''
#선택정렬
arr = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N=9
# 0번 부터 N-2번까지 위치에 들어갈 작은 숫자 찾긴
for j in range(0, N-1):          # 위치 j
    min_idx = j  # 일단 그냥 제일 앞 녀석이 작은 것으로 치자
    for i in range(j, N):
        if arr[i] < arr[min_idx]:
            min_idx = i
    # 제일 작은애의 위치 min_idx
    arr[j], arr[min_idx] = arr[min_idx], arr[j]

    print(arr)

print(arr)
'''
'''
# 카운팅 정렬
# 요소의 개수를 세어서 위치 찾기
# 각 요소의 개수를 저장
# → 숫자가 너무 들쯕 날쭉하면 제한, 그리고 숫자로 표현해야 가능함.
# 빠아름 근데 앞서 위처럼 제약사항이 있다.
# 1. 개수 세기
# 2. 누적합 구하기(위치 구한거)
# 3. 원래 배열 돌면서 위치 찾아서 넣어주기
# 정렬대상
arr = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N = 9
# 각 요소가 몇개씩 나왔는지 개수세는 배열
count = [0]*10                  # 0번부터 9번 인덱스 까지 사용해야하므로 10개
# 정렬된 요소가 들어갈 배열
sorted_arr = [0]*9
#1. 개수세기
for i in range(N):
    count[arr[i]] += 1          # count배열에 arr[i]가 있으면 +1
#2. 누적합 구하기
# 내 앞 요소 값 + 내 값
for i in range(1, len(count)):
#     count[i] = count[i-1] + count[i]
    count[i] += count[i-1]      # 이제 카운트는 배열 요소들의 위치가 된다.
#3.원래 배열 돌면서 위치 찾아서 넣어주기
for i in range(N):
    count[arr[i]] -= 1          # count[arr[i]] 내가 들어갈 위치 찾음!! -1 해주는 이유는 인덱스에 들어가야하니까
    sorted_arr[count[arr[i]]] = arr[i]

print(sorted_arr)
'''