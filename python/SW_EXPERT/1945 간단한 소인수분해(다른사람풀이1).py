T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0                   # a,b,c,d,e를 각 0으로 할당
    while N != 1:                                   # N이 1이 아니라면 while문 실행
        if N % 2 == 0:                              # N/2 나머지가 0이라면
            a += 1                                  # a에 1을 더하자.
            N = N // 2
        elif N % 3 == 0:                            # N/3 나머지가 0이라면
            b += 1                                  # b에 1을 더하자.
            N = N // 3
        elif N % 5 == 0:                            # N/5 나머지가 0이라면
            c += 1                                  # c에 1을 더하자.
            N = N // 5
        elif N % 7 == 0:                            # N/7 나머지가 0이라면
            d += 1                                  # d에 1을 더하자.
            N = N // 7
        elif N % 11 == 0:                           # N/11 나머지가 0이라면
            e += 1                                  # e에 1을 더하자.
            N = N // 11
    print(f"#{test_case} {a} {b} {c} {d} {e}")      # f 스트링을 이용해서 a b c c d e를 출력