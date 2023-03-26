# 함수       함수 실행목적은 값을 얻어오고 싶을 때.
# 값을 주는 함수를 이미 사용해봤습니다. len(arr) : 리스트 요소 갯수
#자주쓰는 코드를 따로 저장해놓고 불러서 사용
# print('안녕하세요')
# print('반갑습니다.')
# print('저는 홍길동입니다.')
# print('잘 부탁드립니다.')

# print('안녕하세요')
# print('반갑습니다.')
# print('저는 김싸피입니다.')
# print('잘 부탁드립니다.')

# print('안녕하세요')
# print('반갑습니다.')
# print('저는 박싸피입니다.')
# print('잘 부탁드립니다.')

# def 함수이름():     #def = define
#     함수 내용
# 함수를 실행할 때 이름이 다른데?? 이름이 필요합니다.
# 함수를 실행하기 위해서 필요한 값을 받아올 수 있습니다!
# 매개변수(파라미터, parameter)를 이용해서

# def greeting():     # 함수정의
#     print('안녕하세요')
#     print('반갑습니다.')
#     print('저는 김싸피입니다.')
#     print('잘 부탁드립니다.')

# greeting()          #함수호출
# greeting()
# greeting()
# greeting()

def greeting(name):     #name은 매개변수로 선언한 것 파라미터.
    print('안녕하세요')
    print('반갑습니다.')
    print(f'저는 {name}입니다.')
    print('잘 부탁드립니다.')

greeting('김싸피')      #함수 호출할 때 넣어주는 값: 인자(argument) 알규먼트
greeting('이싸피')
greeting('박싸피')
greeting('최싸피')

# 두 정수를 더해서 그 결과를 출력하는 add라는 함수만들기
a =3
b =5
print(a+b)

def add(a,b):
    print(a+b)
    # return None #쓰든 안쓰든 함수의 맨마지막은 항상 return None이다.
    return a+b
# add(3,5)
int(input)
add(5,10)

a=add(5,10) #얘는 아무것도 안줌. NONE 데이터만 줌.
# 그렇다면 합을 받아오기 위해서는 함수가 결과를 반환해야 한다.
print(f'a={a}')

# 정수하나를 제곱하여 그 값을 반환하는 함수 square를 작성하고
# 정수의 제곱을 출력합니다.
# 출력 예시는 '5의 제곱은 25입니다.'