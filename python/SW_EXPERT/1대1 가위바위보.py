'''
A와 B가 가위바위보를 하였다.

가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.

A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

 

[입력]

입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.

 
 

[출력]

A가 이기면 A, B가 이기면 B를 출력한다.


입력값: 3 2
출력값: A
'''

#풀이

A,B = map(int, input().split()) #map으로 여러 값을 넣을 수 있으며, split을 이용 띄어쓰기 구분을 할 수 있다.
player = {}
player[A] = "A"
player[B] = "B"
winner = ''
if(A == 1 and B ==3 or A==3 and B==1):		#가위(1)와 보(3)은 숫자가 작은 가위가 이기기 때문
    minNum = min(A,B)
    winner = player[minNum]
else:
    winner = player[max(A,B)]			#가위(1)와 바위(2), 바위(2)와 보(3)은 숫자가 큰 쪽이 이기기 때문

print(winner)