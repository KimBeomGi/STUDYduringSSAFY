N, M = map(int, input().split())
lst = []
for i in range(N):
    a = input()
    for j in range(M-1,-1,-1):
        print(a[j], end='')
    print()

# n, m = map(int, input().split())

# for i in range(n):
#     shape = input()
#     print("".join(reversed(shape)))