A, B = map(str, input().split())

# 뒤집기
A_r = ''
B_r = ''
for i in range(len(A)-1, -1, -1):
    A_r += A[i]
for i in range(len(B)-1, -1, -1):
    B_r += B[i]

print(max(int(A_r), int(B_r)))