'''
# 함수에서!!!

def hello(p1, p2):    # 함수를 수행하기 위한 데이터는 파라미터(매개 변수)로 받아오면 된다.
    print(f'안녕하세요. {p1}입니다.')
    print(f'반갑습니다.')
    print(f'앞으로 잘 지내봐요. {p2}씨')
    #return xxx
    # return None # return 값을 안적어주면 return None과 같기 때문에 None 쓸거면 안적어줘도 됨
    # return    # return만 적고 값을 안적어줘도 return None과 같다.

# # 김철수 → 이싸피
# print('안녕하세요 김철수입니다.')
# print('반갑습니다.')
# print('앞으로 잘 지내봐요 이싸피씨')

# # 이싸피 → 김철수
# print('안녕하세요 이싸피입니다.')
# print('반갑습니다.')
# print('앞으로 잘 지내봐요 김철수씨')

# # 이싸피 → 최싸피
# print('안녕하세요 이싸피입니다.')
# print('반갑습니다.')
# print('앞으로 잘 지내봐요 최싸피씨')


a = hello('최씨', '박씨')
# hello('최씨', '박씨')
# hello('최씨', '박씨')
print(a) # return 값 안 적어주면 None값으로 반환
# # 반복되는 문장에서 필요한 문장! 함수를 수행하기 위한 데이터!

# # 두 정수를 더해서 결과를 출력하는 함수
def add(a,b):
    print(f'{a} + {b} = {a+b}')
    return a+b

rst1 = add(3,5)
rst2 = add(3,9)
rst3 = add(5,18)
rst4 = add(6,209123)
print(rst1+rst2+rst3+rst4)


arr = [1,2,3,4,5]

# a = len(arr)
# print(a)
'''
# ==========================
'''
# 파이썬의 특징 중 하나 언팩킹!
a, b, c = 1,2,3,
print(a)
a = 1,2,3
print(a)
'''
# =======================
'''
# def add(x,y):
#     return x+y

# result = add(7, x=3)    # 이러면 에러가남 이유는 y자리에 x가 들어있는 것을 보고 아니 이게 무슨 말이야 하기 때문
# result = add(7, 3)  # positional argument
# result = add(x=7, y=3)
# # 제한! 앞에 keyword argument를 쓰면 그 이후에는 positional argument를 사용할 수가 없다.
# print(result)

def add(x,y=0):
    print(f'x:{x}','y:{y}')
    return x+y

result = add(7)
print(result)

print('hello', end=' ')
print('hello')
'''
# ===================================

# LEGB

x=10
def func1():
    x=100
    def func():    
        nonlocal x  #이러면 enclosing에 있는 변수를 사용 가능
        # x = 5
        print(x)
    func()

func1()
print(x)