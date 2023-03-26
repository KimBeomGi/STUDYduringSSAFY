'''
def my_magic_func(n):
	return n * 10

my_list = [1, 2, 3, 4, 5]

rlt = map(my_magic_func, my_list)   # 이대로 하면 주소가 나오니 리스트로 만들어서 이용!
rlt = list(map(my_magic_func, my_list))
print(rlt)
'''
'''
name_list = ['신동민,', '서재현', '박명서', '이태성', '정예원', '이은서']
age_list = [17, 18, 22, 24, 25, 19]

for each in zip(name_list, age_list):    #반복 가능한 개체 2개를 넣음 이상인가?
	print(each)
    '''
'''
def my_magic_func(n):
	return n * 10

map_obj = map(my_magic_func, [1, 2, 3])
rlt = list(map_obj)

print(rlt)
'''
'''
# lambda x: x * x
# =
# def pow(x):
#     return x * x
# print((lambda x: x * x)(4))     # 소괄호 열고 닫고 함수 실행

# rlt = (lambda x: x * x)(4)

# my_func = lambda n : n * 2
# my_func(2)


def my_magic_func(n):
    return n * 10
map_obj = map(my_magic_func, [1,2,3])
rlt = list(map_obj)
print(rlt)

map_obj = map(lambda x : x*10, [1,2,3])
rlt = list(map_obj)
print(rlt)
'''
'''
def fac(n):
    if n == 0 :
        return 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    return n*fac(n-1)

print(fac(5))
# 재귀의 형태를 띄고 있다. 머릿속에서만 돌리긴 힘드니
# 그림을 그려봐라!
# 계산은 맨 마지막 부터
'''
# 패킹/언패킹 *
'''
패킹
x, y = 1, 2
z = 1, 2, 3

a, *b = 1, 2, 3, 4  # a에는 1을 넣고 나머지는 모두 b에 넣어!
print(a,b)
'''
'''
# 언패킹
def my_sum(a,b,c):
    return a + b + c

num_list = [10, 20, 30]

# rlt = my_sum(num_list[0], num_list[1], num_list[2])
rlt = my_sum(*num_list)     # 패킹 되어 있는 것 앞에 *을 붙여 *패킹을 하면 언패킹
'''
'''
# def test(*values):
#     for value in values:
#         print(value)

# test(1)
# test(1, 2)
# test(1, 2, 3, 4)


def my_sum(*agrs):
    rlt = 0
    for value in agrs:
        rlt += value
    return rlt

my_sum()
my_sum(1, 2, 3)
'''

numbers = [1,2,3]
numbers = list(map(str,numbers))
print(numbers)
new_numbers = ''.join(numbers)
print(new_numbers)