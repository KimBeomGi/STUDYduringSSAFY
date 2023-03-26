N = int(input())
card_list=[]
for i in range(1,N+1):
    card_list.append(i)

card_throw = []
while len(card_list) > 1:
    card_throw.append(card_list.pop(0))
    card_list.append(card_list.pop(0))

for i in card_throw:
    print(i, end=' ')
print(card_list[0])


#이건 다른방법
N = int(input())
lst = []
for i in range(1, N+1):
    lst.append(i)
while len(lst) > 1:
    aa = lst.pop(0)
    print(aa, end=' ')
    a = lst.pop(0)
    lst.append(a)
print(*lst)