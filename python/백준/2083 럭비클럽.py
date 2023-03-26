A, B, C = map(str, input().split())
while "A" != '#' or "B" != '0' or "C" != '0':
    B = int(B)
    C = int(C)
    if B > 17 or C >= 80:
        print(A, 'Senior')
    else:
        print(A, 'Junior')
    A, B, C = map(str, input().split())
    if A == '#' and B == '0' and C =='0':
        break