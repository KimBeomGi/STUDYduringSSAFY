# 선택정렬
# 0~ N-2번까지위치에 들어갈 작은 숫자 찾기
'''
# 따라하기
testcase = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N = len(testcase)
for i in range(0, N-1):     # [0]~[N-2] 즉, 뒤에서 2번째까지 검사하기 위해
    min_idx = i             # 우선 최솟값을 제일 앞에 녀석이라 하고 보자.
    for j in range(i, N):   # [i]~[N-1] 현재 값 포함 뒤에 있는 녀석 모두 검사
        if testcase[min_idx] > testcase[j]:
            min_idx = j
    testcase[i], testcase[min_idx] = testcase[min_idx], testcase[i]
print(testcase)
'''
# 혼자서 연습해보기
testcase = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N= len(testcase)

for i in range(N-1):
    min_idx = i
    for j in range(i, N):
        if testcase[min_idx] > testcase[j]:
            min_idx = j
    testcase[min_idx], testcase[i] = testcase[i], testcase[min_idx]
print(testcase)