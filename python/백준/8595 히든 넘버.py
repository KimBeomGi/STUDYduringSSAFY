# 문제
# 단어에 숫자가 숨어있다. 이 숫자를 히든 넘버라고 한다. 알파벳 대/소문자와 숫자로 이루어진 단어가 주어졌을 때, 모든 히든 넘버의 합을 구하는 프로그램을 작성하시오.
# 단어와 히든 넘버는 아래와 같은 성질을 갖는다.

# 연속된 숫자는 한 히든 넘버이다.
# 두 히든 넘버 사이에는 글자가 적어도 한 개 있다.
# 히든 넘버는 6자리를 넘지 않는다.

# 입력
# 첫째 줄에 단어의 길이 n (1 ≤ n ≤ 5,000,000)이 주어진다. 둘째 줄에는 단어가 주어진다. 단어는 알파벳 대/소문자와 숫자(0-9)로 이루어져 있다. 

# 출력
# 입력으로 주어진 단어에 숨어있는 모든 히든 넘버의 합을 출력한다. 만약, 히든 넘버가 없는 경우에는 0을 출력한다.

# 입력값
# 14
# ab13c9d07jeden

# 출력값
# 29

# 풀이
# 1.

import sys

n = int(sys.stdin.readline().strip())
word = sys.stdin.readline().strip()

number = ['0','1','2','3','4','5','6','7','8','9']
temp = ""
summary = 0
for i in range(len(word)):  # 단어의 철자를 확인
    # print(word[i])
    if word[i] in number:
        temp = temp + word[i]
    elif temp:
        summary += int(temp)    # 합에다가 임시 저장 hidden값을 넣어주고
        temp = ""                # 새로운 hidden 값을 받기 위해 temp로 만들어주기
    else:
        temp = ""
# 끝나면?
if temp:    # temp값이 있으면
    summary += int(temp)    
print(summary)