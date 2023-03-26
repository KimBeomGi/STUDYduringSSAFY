'''
# 부분집합의 합
def f(i, k, key):
    if i == k:                  # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]       # 부분집합의 합
        #         print(A[j], emd='')
        # print()
        # print(bit, s)
        if s == key:    # 합이 Key와 같은 부분집합을 출력
            # for j in range(k):
            #     if bit[j]:
            #         print(A[j], end=' ')
            # print()
            return 1
        else:
            return 0
    else:
        bit[i] = 1
        if f(i+1, k, key):
            return 1
        bit[i] = 0
        if f(i+1,k, key):
            return 1
        return 0

A = [1,2,3,4,5,6,7,8,9]
N = len(A)
key = 10
bit = [0]*N
print(f(0, N, key))
'''
'''
# 부분집합의 합2
def f(i, k, s, t):      #i원소, k 집합의 크기, s i-1까지 고려된 합, t 찾고자하는 합(목표)
    global cnt
    global fcnt
    fcnt += 1
    if s > t:           # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t:        # 남은 원소를 고려할 필요가 없는 경우
        cnt += 1
        return
    elif i == k:        # 모든 원소 고려
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함



N = 10
# A = [1,2,3,4,5,6,7,8,9,10]
A = [i for i in range(1, N+1)]
key = 1
cnt = 0
bit = [0]*N
fcnt = 0

f(0, N, 0, key)
print(cnt, fcnt)          # 합이 key인 부분집합의 수
'''

'''
# 순열

def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            # p[i]결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]


p = [1,2,3]
N= len(p)
f(0, N)
'''


#분할정복