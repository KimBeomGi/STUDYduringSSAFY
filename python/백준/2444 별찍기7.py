N = int(input())

for i in range(1,N+1):
    print(' '*(N-i), end='')
    print('*'*i, end='')
    print('*'*(i-1))

for i in range(1,N):
    print(' '*(i), end='')
    print('*'*(N-i), end='')
    print('*'*(N-i-1))