# 문제
# The PLU football coach must submit to the NCAA officials the names of all players that will be competing in NCAA Division II championship game. Unfortunately his computer keyboard malfunctioned and interchanged the letters ‘i’ and ‘e’. Your job is to write a program that will read all the names and print the names with the correct spelling.

# 입력
# The file contains a list of names, and each name will be on a separate line.

# 출력
# Print the same list of names with every ‘i’ replaced with an ‘e’, every ‘e’ replaced with an ‘i’, every ‘I’ replaced with an ‘E’, and every ‘E’ replaced with an ‘I’.\

import sys

while True:
    try:
        team_name = list(sys.stdin.readline().strip())
    except:
        break
    # team_name = list(sys.stdin.readline().strip())
    # if not team_name:
    #     break
    for char in range(len(team_name)):
        if team_name[char] == 'i':
            team_name[char] = 'e'
        elif team_name[char] == 'I':
            team_name[char] = 'E'
        elif team_name[char] == 'e':
            team_name[char] = 'i'
        elif team_name[char] == 'E':
            team_name[char] = 'I'
    # print('------------------------------------')
    print(*team_name)
    # print('------------------------------------')
    # print('------------------------------------')

import sys

for line in sys.stdin:
    s = line.strip()
    for i in range(len(s)):
        if s[i] == 'i':
            s = s[:i] + 'e' + s[i+1:]
        elif s[i] == 'e':
            s = s[:i] + 'i' + s[i+1:]
        elif s[i] == 'I':
            s = s[:i] + 'E' + s[i+1:]
        elif s[i] == 'E':
            s = s[:i] + 'I' + s[i+1:]
    print(s)