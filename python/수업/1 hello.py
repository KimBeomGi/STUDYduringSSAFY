# 파이썬아.. 화면에 Hello world! 라는 문자열을 출력해줘
print('Hello World!')
# 'Hello world!'라는 문자열을 greeting 이라는 이름의 변수에 저장하고
# greeting 변수에 들어있는 값을 출력하기
# 값을 변수에 저장하는 것을 '할당(assignment)'이라고 함.
# 변수 = 값 (왼쪽 변수에 오른쪽 값이 들어감)
# #을 쓰는 것은 '주석(comments)'임 그러면 실행 대상에서 제외 됨
# 프로그램에 대한 설명이나, 메모 같은 것을 주석으로 작성
a = 5 # a라는 변수에 5라는 값이 들어감
greeting = 'Hello World!'
greeting = "Hello World!"
# 변수 이름을 쓰면 걔가 그냥 값이다.
print(greeting)
a = greeting #a라는 변수에 greeting이 가진 값을 넣어주는 것.
print(a)
# print(Greeting) 얘가 실행안된다면 이유는 Greeting에 대한 변수 정의가 안되었기 때문.
# 파이썬에서의 변수 정의 : 파이썬은 별도의 변수 정의는 없고, 변수에 값을 넣어주면 된다.

# 파이썬은 문자열과 문자를 구분하지 않음. >> 문자열을 쓸 때는 따옴표를 쓰면 된다.
# 자바에서는 'A'는 문자 A, "A"는 문자열 A




# 안녕하세요! 10번 출력
# 안녕하세요 1
# 안녕하세요 2
# 안녕하세요 3
# ~
# 안녕하세요 10
'''
i=1
while i < 11:
    print('안녕하세요!',i)
    i+=1

i=0
while i < 10:
    i+=1
    print('안!녕하세요~',i)

while i < 10:
    i+=1
    print('안!녕하세요',i)
    if i == 11:
        break

for i in range(1,11):
    print('안녕!하세요!',i)
'''

i=1
while i<= 1:
    print(f'안녕하세요 {i}') # 문자열 안에 내가 가진 변수값을 집어 넣고 싶을 때 f string을 사용
    i+=1