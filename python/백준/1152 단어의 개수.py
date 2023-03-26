string = input()
N = len(string)
K = 0
for i in range(N):
    if i< (N-1):
        if string[i] == ' ' and string[i+1] == ' ':     # 현재 값도 띄어쓰기 다음값도 띄어쓰기면
            break                                       # 더 볼 필요 없으니 종료
        elif string[i] != ' ' and string[i+1] == ' ':   # 현재값이 띄어쓰기가 아니고 다음 값이 띄어쓰기면
            K += 1                                      # 단어 하나가 있는 것이니 k + 1 해주기
    if i == (N-1) and string[i] != ' ':     # 마지막에서 띄어쓰기가 없어서 문자로 끝나면?
        K += 1                              # 끝났으니까 더해주자.
print(K)