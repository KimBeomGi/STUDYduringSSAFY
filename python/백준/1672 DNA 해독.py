N = int(input())
base = list(str(input()))
# print(base)
i = N-1
while i > 0:
    # T
    if base[i] == 'T' and base[i-1] == 'T':
        base.pop()
        base.pop()
        base.append('T')
    elif base[i] == 'T' and base[i-1] == 'C':
        base.pop()
        base.pop()
        base.append('G')
    elif base[i] == 'T' and base[i-1] == 'G':
        base.pop()
        base.pop()
        base.append('A')
    elif base[i] == 'T' and base[i-1] == 'A':
        base.pop()
        base.pop()
        base.append('G')
    # C
    elif base[i] == 'C' and base[i-1] == 'T':
        base.pop()
        base.pop()
        base.append('G')
    elif base[i] == 'C' and base[i-1] == 'C':
        base.pop()
        base.pop()
        base.append('C')
    elif base[i] == 'C' and base[i-1] == 'G':
        base.pop()
        base.pop()
        base.append('T')
    elif base[i] == 'C' and base[i-1] == 'A':
        base.pop()
        base.pop()
        base.append('A')
    # G
    elif base[i] == 'G' and base[i-1] == 'T':
        base.pop()
        base.pop()
        base.append('A')
    elif base[i] == 'G' and base[i-1] == 'C':
        base.pop()
        base.pop()
        base.append('T')
    elif base[i] == 'G' and base[i-1] == 'G':
        base.pop()
        base.pop()
        base.append('G')
    elif base[i] == 'G' and base[i-1] == 'A':
        base.pop()
        base.pop()
        base.append('C')
    # A
    elif base[i] == 'A' and base[i-1] == 'T':
        base.pop()
        base.pop()
        base.append('G')
    elif base[i] == 'A' and base[i-1] == 'C':
        base.pop()
        base.pop()
        base.append('A')
    elif base[i] == 'A' and base[i-1] == 'G':
        base.pop()
        base.pop()
        base.append('C')
    elif base[i] == 'A' and base[i-1] == 'A':
        base.pop()
        base.pop()
        base.append('A')
    i -= 1
    # print(base)
print(''.join(base))