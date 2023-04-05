A = int(input())
B = int(input())
C = int(input())
value = [0]*10
multi = str(A*B*C)
for i in range(len(multi)):
    value[int(multi[i])] += 1

for i in range(10):
    print(value[i])