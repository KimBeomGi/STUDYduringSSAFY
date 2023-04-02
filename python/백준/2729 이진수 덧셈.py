T = int(input())
for testcase in range(1, T+1):
    A, B = map(str, input().split())
    A_dec = int(A, 2)
    B_dec = int(B, 2)
    C_dec = A_dec + B_dec
    C_tmp = bin(C_dec)
    print(C_tmp[2:])