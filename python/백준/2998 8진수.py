bin_to_oct = {
    '000' : 0, '001' : 1, '010' : 2, '011' : 3, '100' : 4, '101' : 5, '110' : 6, '111' : 7, 
              }

A = input()
while len(A) % 3 !=0:
    A = '0' + A
# print(A)

answer = ''
for i in range(0, len(A), 3):
    answer =  answer + str(bin_to_oct[A[i:i+3]])
print(answer)