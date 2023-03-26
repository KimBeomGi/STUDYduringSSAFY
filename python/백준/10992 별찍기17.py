N = int(input())

for i in range(1,N+1):
    if i == N:
        print('*'*(2*i-1))
    print(' '*(N-i),end='')
    
    if i!=N:
        print('*',end='')
        print(' '*(2*(i-1)-1), end='')
        if i==1:
            print()
        else:
            print('*')