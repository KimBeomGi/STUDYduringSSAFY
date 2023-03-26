# 선택 정렬
# 목적은 배열의 인덱스를 잘 활용하는 연습을 하자
# 알고리즘 설명 
# 각 자리에 맞는 수를 선택해서 자리에서 넣어주기
# ex) 제일 앞자리에는 제일 작은 수 선택해서 넣어주기
# 0번 부터 N-2번까지 자리에 들어갈 요소 선택해서 넣어주기

arr = [5,6,1,4,3,7,8,2,9]
N = 9
for i in range(0, N-1): #0부터이므로 그냥(n-1)해도됨
    # i번부터, N-1번 요소 중에 제일 작은 애 찾기
    min_idx =  i
    for j in range(i+1, N):   # i번부터 n-1까지 검사가 필요. 그러나 i는 가장 작은 값으로 했으니 i+1
        if arr[min_idx] > arr[j]:
            min_idx = j
    # 제일 작은 요소 찾았으니, 자리 찾아 교환해주기
    arr[min_idx], arr[i] = arr[i], arr[min_idx]
print(arr)

arr = [5,6,1,4,3,7,8,2,9]
N = 9
for i in range(N-1):
    min_dix = i
    for j in range(i+1, N):
        if arr[min_idx]>arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]
print(arr)




arr = [9,8,7,6,5,4,3,2,1]
N = 9

for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]
print(arr)



arr = [9,8,7,6,5,4,3,2,1]
N = 9

for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]