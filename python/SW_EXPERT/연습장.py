'''
A, B, C, D = map(int, input().split())
print(C,A,B, D)
'''

int_num = int(input())
sum = 0
for i in range(0,4):
    sum+=int_num%10
    int_num = int_num//10
print(sum)