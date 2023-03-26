'''
# 리스트 생성

arr = []    # 요롷게 쓰는 것으로 권장   # 비어있는 리스트 생성
# arr = list()
arr = [1, 2, 3, 4, 5]       #리스트의 요소가 초기화(initailize)된 형태로 생성   #변수에 최초로 값을 넣는 행위를 초기화(initailize)이다.
#리스트는 변수에 타입을 지정하지 않아 다양한 타입의 데이터가 들어갈 수 있다.
#리스트를 사용하는 이유가 애초에 많은 데이터를 한 번에 처리할 수 있도록 하기 위함
arr = [1, 'ABC', 3.0, [1,2,3]] # 잘 쓰진 않지만 써야 할 때도있다.

arr1 = [0,0,0,0,0,0,0,0,0,0] #각 요소가 0으로 초기화된 크기 10짜리의 리스트
arr2 = [0]*10    # 이것도 된다. 된다고해서 모든 경우에 *연산을 사용하면 안됨

arr1[3] = 100
arr2[3] = 100

print(arr1[0],arr1)
print(arr2[0],arr2)
arr3 = [[1,2,3],[1,2,3],[1,2,3]]
arr3[0][1] = 100
print(arr3[0][1])
print(arr3)
arr4=[[1,2,3]]*3    #[1,2,3]이 원소이므로 []안에 넣어준것임
arr4[0][1] = 100
print(arr4)
'''
'''
boxes = ['A', 'B', ['apple', 'banana', 'cherry']]
print(len(boxes))
print(boxes[2])
print(boxes[2][-1])
print(boxes[-1][1][0])  
#문자열도 인덱스에 접근이 가능하다. 그리고 불변이지만,  컨테이너는 아니다.
'''

'''
#튜플 생성하기
tp = (1,2,3)
# print(tp[0],tp[1],tp[2])
print(tp[-1],tp[-2],tp[-3])
# tp[1]=100   #튜플이라 가변 안됨
# TypeError: 'tuple' object does not support item assignment
tp = (1) # 이러면 int로 인식
tp = (1,) # 이러면 튜플로 인식
tp= tuple([1,2,3]) # tuple 함수 이용하면 tuple 생성가능
# 반복 가능한 형태를 iterable이라함
print(type(tp))
'''
'''
#range 연습
# range(end)
print(list(range(10))) #0 1 2 3 4 5 6 7 8 9
# range(start,end)
print(list(range(1,10))) #1 2 3 4 5 6 7 8 9
# range(start,end, step)
print(list(range(1,10, 3))) #1 4 7
'''
'''
#슬라이싱 연습
arr = [0,1,2,3,4,5,6,7,8,9,10]
# 시퀀스[start:end:step]    #(start또는 end)와 step은 생략 가능하다.
a = arr[4:] # end 생략
print(a)
print(arr)
b= arr[:4]  # start 생략, 4번 이전까지 잘라서 복사
print(b)
# 둘다 생략, 처음부터 끝까지 잘라서 복사
c= arr[:]   # 이게 필요한가요???
print(c)

lst = [1,2,3]
lst1 = lst
lst[0] = 100
print(lst)
print(lst1)
# ↑와 ↓는 다른 결과가 나옴
lst = [1,2,3]
lst1 = lst[:]
lst[0] = 100
print(lst)
print(lst1)

d=arr[::2]  #여기서는 0 2 4 6 8 10이 출력됨
print(d)
d=arr[::-2] #역순으로 해당 스텝으로 출력된다.
print(d)
'''
'''
# dictionary 생성
# {} 또는 dict() 의 방법으로 생성
my_dict = {}
print(type(my_dict))
my_dict = dict()
print(type(my_dict))

my_dict = {'key':'value'}   #문자열일 필요는 없다.
# my_dict = {'key':'value', 'key':'value', 'key':'value', 'key':'value'}    #여러개 쓰면 쉼표를 쓰고 더 쓰면 된다.
my_dict = {'a':'apple', 'b':'bananan', 'listt':[1,2,3]}
print(type(my_dict))
print(my_dict['a'])
print(my_dict.get('a'))
'''
'''
# 명시적인 형 변환
# int(), float(), str()
a= int('123')
print(type(a))
a= float('123')
print(type(a))
print(a)
s= str(123.1235)
print([s])
print(type(s))
'''
'''
# 각 자리수 합
str_num = '12345'
print(type(str_num))
# 다른 언어에서는!
# '12345'
# 12345 / 10  1234,5
# 1234 / 10   123,4
# 123 / 10    12,3
# 12 / 10     1,2
# 1 / 10      
###################
# 파이썬에서는?
# 각 자리수를 자르기 >> 각 자리수의 문자열을 숫자로 변경
# map(int, 시퀀스) >>
print(map(int, str_num))   #문자열의 한자리 한자리 한자리를 잘라서 int로 바구는 것
print(type(map(int, str_num)))
print(sum(map(int, str_num)))
'''
'''
#set
# 집합 자료형
# ★중복되지 않는 데이터★를 가지는 자료형
# {} << 얘는 dictionary라서 set()함수를 이용해야한다.

# a=set() #또는 아래처럼
# a = {1,2,3}
# print(type(a))

a= set()
print(type(a))
a.add(1)
a.add(2)
a.add(3)
a.add(1)
print(a)
'''
#str to list, tuple, set
str1='hello'
a = list(str1)
b = tuple(str1)
c = set(str1)
print(a,b,c)

#list to tuple, set
list1 = [1,2,3,1,1]
a = tuple(list1)
b = set(list1)
print(a,b)

#range to list, tuple, set
range1 = range(5)
a = list(range1)
b = tuple(range1)
c = set(range1)
print(a,b,c)

#set to list, tuple
set1 = {1,2,3,4,5,6}
a= list(set1)
b= tuple(set1)
print(a,b)

#dictionary to list, tuple, set
dict1 = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
#dictionary는 형 변환 시 key 값만 변환이 가능하다.
a = list(dict1)
b = tuple(dict1)
c = set(dict1)
print(a,b,c)
