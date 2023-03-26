sci = 1
rock = 2
paper = 3

A,B = map(int, input().split())

if A == sci and B== rock:
    print('B')
elif A == sci and B== paper:
	print('A')
elif A == rock and B== paper:
	print('B')
elif A == rock and B== sci:
	print('A')
elif A == paper and B== sci:
	print('B')
elif A == paper and B== rock:
	print('A')
else:
    print('DRAW')