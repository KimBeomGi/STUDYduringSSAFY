T = int(input())
for testcase in range(1, T+1):
    # A = int(input())
    # A_bin_tmp = bin(A)
    # A_bin = A_bin_tmp[2:]

    A = int(input())
    A_bin = ''
    while A > 0:
        remainder = A % 2   
        A_bin = A_bin + str(remainder)
        A = A // 2

    for i in range(len(A_bin)):
        if A_bin[i] == '1':
            print(i, end=' ')
    print()