N = list(map(int,input()))
while N != [0]:
    width = 1
    for number in N:
        if number == 1:
            width += 2
        elif number == 0:
            width += 4
        else:
            width += 3
        width +=1
    print(width)
    N = list(map(int, input()))