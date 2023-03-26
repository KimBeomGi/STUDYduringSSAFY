'''
# 선택정렬!!!
'''
# 7
# 7 2 4 3 4 6 4
'''

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1):                # 작업 구간의 시작 인덱스
    minIdx = i                     # 맨 앞이 최소라 가정
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]
print(arr)
'''
'''

arr = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]
N = 5
r,c = 0,0
while r < 5:
    print(arr[r][c])
    if r == 2:
        while True:
            if arr[r][c] == 3:
                break
            print(arr[r][c])
            c += 1
    r += 1
print('끝')
'''
