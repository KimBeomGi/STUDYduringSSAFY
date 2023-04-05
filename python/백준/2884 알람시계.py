H, M = map(int, input().split())
0 <= H < 24
0 <= M < 60

if M - 45 < 0:
    if H == 0:
        H = 23
        M = 60-(45-M)
    else:
        H -= 1
        M = 60-(45-M)
else:
    M -= 45
print(f'{H} {M}')