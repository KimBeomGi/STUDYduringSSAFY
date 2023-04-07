# 문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

import sys

string = sys.stdin.readline().strip()
N = len(string)
how_many = 0
i = 0
while  i < N:
    if i <= N-2 and string[i] == 'c':
        if string[i+1] == '=':
            how_many += 1 
            i += 2
            continue
        elif string[i+1] == '-':
            how_many += 1 
            i += 2
            continue
    elif string[i] == 'd':
        if i <= N-3 and string[i+1] == 'z' and string[i+2] == '=':
            how_many += 1
            i += 3
            continue
        elif i <= N-2 and string[i+1] =='-':
            how_many += 1
            i += 2
            continue
    elif i <= N-2 and string[i] == 'l' and string[i+1] =='j':
        how_many += 1
        i += 2
        continue
    elif i <= N-2 and string[i] == 'n' and string[i+1] =='j':
        how_many += 1
        i += 2
        continue
    elif i <= N-2 and string[i] == 's' and string[i+1] =='=':
        how_many += 1
        i += 2
        continue
    elif i <= N-2 and string[i] == 'z' and string[i+1] =='=':
        how_many += 1
        i += 2
        continue
    i += 1
    how_many += 1
print(how_many)    



######
# 딕셔너리로 해볼까했는데 오 이 방법도 있네
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
i = 0
answer = 0
while i < len(word): 
    if word[i:i+3] == 'dz=' and i + 2 <= len(word) - 1:
        i += 3
    elif word[i:i+2] in cro and i + 1 <= len(word) - 1:
        i += 2
    else:
        i += 1
    answer += 1
    
print(answer)