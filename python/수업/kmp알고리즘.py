def kmp(t, p):                                          # KMP알고리즘 작동 함수
    N = len(t)                                          # t는 확인대상인 전체문장
    M = len(p)                                          # P는 확인하려는 예시
    lps = [0] * (M+1)                                   # p(패턴) + 1개 만큼의 0으로 이루어진 리스트 생성
    # preprocessing
    j = 0                                               # 일치한 개수== 비교할 패턴 위치
    lps[0] = -1                                         # 이후 이용하기 위해서 패턴의 맨 앞 값을 -1로 명명해서 언제든 처음으로 돌아갈 수 있게 함
    for i in range(1, M):                               # 1~패턴의 길이만큼 작동하는 반복문 for
        lps[i] = j          # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j <= M:
        if j==-1 or t[i]== p[j]:     # 첫글자자 불일치했거나, 일치하면
            i += 1
            j += 1
        else:               # 불일치
            j = lps[j]
        if j==M:    # 패턴을 찾을 경우
            print(i-M, end = ' ')    # 패턴의 인덱스 출력
            j = lps[j]

    print()
    return


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = "AAAAABAAABA"
p =  "AAAA"
kmp(t, p)
t = "AAAAABAAABA"
p =  "AA"
kmp(t, p)