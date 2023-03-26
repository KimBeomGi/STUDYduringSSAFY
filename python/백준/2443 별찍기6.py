N = int(input())

for i in range(N):
    print(' '*i, end='')
    print('*'*(N-i),end='')
    print('*'*(N-i-1))