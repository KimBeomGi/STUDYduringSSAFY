def find_set(x):        # x가 속한 집항의 대표 리턴
    while x != rep[x]:  # x==rep[x]까지
        x= rep[x]
    return x

def union(x,y):         # y의 대표원소가 x의 대표원소를 가리키도록 함
    rep[find_set(y)] = find_set(x)
    # rep[y] = find_set(x)


    pass



# makeset()
rep = [i for i in range(6)]
print(rep)