'''
sample_list = [11, 22, 33, 55, 66]
'''
# 주어진 리스트의 4번째 자리에 있는 항목을 제거하고 변수에 할당해 주세요
'''
a = sample_list.pop(3)  #.pop() 괄호에 들어갈 것은 몇번째 인덱스 인지.
print(a)
print(sample_list)
'''
'''
print("original list:", sample_list)

elem = sample_list.pop(3)

print('list after:', sample_list)
print('elem:', elem)

# sample_list의 가장 뒤에 44를 추가해보세요
sample_list.append(77)


# 할당해놓은 변수의 값을 sample_list의 2번 index에 추가해보세요.
sample_list.insert(2, elem)     # index 2번 자리에 위에서 할당해놓은 elem을 추가
print(sample_list)
'''

'''
my_tuple = (11, 22, 33, 44, 55, 66)
# 주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당해보세요.

a = (list(my_tuple)).pop(3)
b = (list(my_tuple)).pop(4)
new_tuple = (a, b)
print(new_tuple)


# new_tuple = my_tuple[3:5]
new_tuple = my_tuple[3:-1]      이렇게도 됨
print(new_tuple)
'''
'''
test_list = [1,2,3,7,4,6,5]
test_list.sort()
print(test_list)

scores = [('eng', 88), ('sci', 90), ('math', 80)]
# 정렬
# print(scores)
# scores.sort()       # 리스트 내 튜플의 맨 앞에 있는 녀석을 기준으로 정렬됨
# print(scores)
# 리스트 내 튜플의 뒷 값을 기준으로 정렬하고 싶다면???

# def check(x):
#     return x[1]

# print(scores)
# scores.sort(key=check)  # check 함수 1번만 쓸건데 def도 해주긴 너무 번거롭다?!
# print(scores)

print(scores)
scores.sort(key=lambda x : x[1])     # lambd 매개변수 : 행위
print(scores)
'''

'''

a = 'hello'.upper() # 이런 데이터와 같이 쓸 수 있는 것. 요론 것을 객체라고 함
print(a)
a = 100    # 100은 객체, 정확히 a에는 100이 저장되는 것이 아닌 100의 주솟값이 저장되어있음.
b = 100    # 이러면 다른 id주소
b = a      # 이러면 같은 id 주소
a = 101    # 새로운 객체의 주솟값을 a에 기입
print(a,b) # b는 기존의 객체 id를 입력, a는 새로운 객체의 id를 입력한 후 출력
print(id(a),id(b))

a = 257
b = 257
print(id(a),id(b))

a = 'hello'
b = 'hello'
print(id(a), id(b))

a = []
b = []
print(id(a),id(b))

a = []
b = a
print(id(a),id(b))

a = []
b = []
a = [1,2,3]
print(a, b)
print(id(a),id(b))  # 이러면 a와 b는 다름

a = []
b = a
a.append(a)
print(a, b)
print(id(a),id(b))  # 같은 리스트를 공유하고 있는데 a에다가 새로운 것을 하니 같은 게 나온다.

a = (1,2)       # 튜플의 특징: 불변!!!
b = (1,2)
print(id(a), id(b))     # 불변한 것이니까 덩어리 하나 만들어두면 그놈 주소 그대로 사용

a = []
b = a       # 할당을 하게 되면 a의 주솟값 그대로 가져오는 것이기 때문에 결국 같은 값임

# 싫으면
a = []
b= a[:]     # a랑 똑같은 모양의 b가 생성됨
print(id(a),id(b))

a = [[1,2,3],4,5]
b = a[:]            # 리스트내 리스트의 것은 원소를 복사하는 게 아닌 리스트의 주소를 복사한 것이여서 제대로된 복사는 아니게됨
print(id(a[0]),id(b[0]))
# 슬라이싱은 완전한 deepcopy는 아니지만 그럴만 하다.

import copy
a = [[1,2,3],4,5]
b = copy.deepcopy(a)
print(id(a[0]),id(b[0]))
##########################
'''
'''
# 재귀함수 이용 리스트안에 리스트안에 리스트안에 리스트안에 있는 리스트까지 깊은 복사를 해보자.
def my_deep_copy(target):
    target_copy = []
    for e in target:
        if type(e) == int or type(e) == str:    # 요소가 숫자나 문자열일 경우는... 그냥 복사
            target_copy.append(e)
        elif type(e) == list:                   # 요소가 리스트 >>> 이것도 복사해야함.
            copied_list = my_deep_copy(e)
            target_copy.append(copied_list)
    return target_copy

arr = [1,2,[10,20,30,[1000,2000,3000]],5,[100,200,300]]
arr_copy = my_deep_copy(arr)
arr[2][3][0] = -1000
print('원본')
print(arr[2][3][0])
print('=======================')
print('복사본')
print(arr_copy[2][3][0])
'''