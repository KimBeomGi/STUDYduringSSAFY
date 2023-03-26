'''
a, b = map(int, input().split())
player = {}
player[a] = "A"
player[b] = "B"
winner = ""
if(a == 1 and b==3 or a==3 and b==1):
  minNum = min(a,b)
  winner = player[minNum]
else:
  winner = player[max(a,b)]
 
print(winner)
'''

A,B = map(int, input().split())
player = {}
player[A] = "A"
player[B] = "B"
winner = ''
if(A == 1 and B ==3 or A==3 and B==1):
    minNum = min(A,B)
    winner = player[minNum]
else:
    winner = player[max(A,B)]

print(winner)