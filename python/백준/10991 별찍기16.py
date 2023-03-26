N = int(input())

for i in range(1,N+1):
    print(' '*(N-i), end='')
    for J in range(i):
        print('*', end=' ')
    print()