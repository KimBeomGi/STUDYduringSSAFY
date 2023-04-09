
# import sys

# N = int(sys.stdin.readline().strip())

# sum_value = 2
# fraction = []

# while len(fraction) < N:
#     if sum_value % 2 == 0:
#         for i in range(sum_value-1,0,-1):
#             fraction.append(f'{i}/{sum_value-i}')
#     else:
#         for i in range(1,sum_value):
#             fraction.append(f'{i}/{sum_value-i}')
#     sum_value += 1
# print(fraction[N-1])



### 꼭 다시 풀기
import sys

x = int(sys.stdin.readline().strip())

if 1<=x<=10000000:
    fn=i=0
    while 1:
        fn=fn+i
        if fn>=x:
            break
        i+=1
num = x - fn +i

if i ==1:
    print("1/1")
elif i%2 == 0:
    print(num,end='')
    print("/",end='')
    print(i+1-num,end='')
else:
    print(i+1-num,end='')
    print("/",end='')
    print(num,end='')