A, B = map(str, input().split())    # A, B를 입력받음

A_dec = int(A,2)
B_dec = int(B,2)
C_dec = A_dec + B_dec

C_bin = bin(C_dec)
print(C_bin[2:])