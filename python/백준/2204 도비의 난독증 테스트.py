T = int(input())
while T != 0:
    words = []
    words2 = []
    for i in range(T):
        word = input()
        words.append(word)
        words2.append(word.upper())
    words2.sort()
    # print(words)
    # print(words2)
    for j in range(T):
        if words[j].upper() == words2[0]:
            print(words[j])
    T = int(input())