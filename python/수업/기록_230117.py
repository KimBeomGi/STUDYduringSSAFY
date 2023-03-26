'''
num = input()
# s = int(num)
if int(num) % 2 == 0:
    print("짝수")
else :
    print("홀수")
'''

'''
grades = {'peter':  80, 'jake': 90}
for key in grades:
    print(grades[key])

for key in grades.keys():
    print(grades[key])

for key,value in grades.items():      # 요 아이템 하나가 
    print(f'{key} : {value}')
'''

'''
# [1,2,3,4,5,6,7,8,8,9.10]
# lst = [expression for 변수 in iterable]
# lst = [num for 변수 in iterable]        # iterable을 돌면서 생길 변수를 난 num으로 이용하겠다.
lst = [num for num in range(1,11)]
print(lst)

lst = [num for num in range(1,11) if num %2 ==0]
print(lst)

[0]*100
lst = [0 for _ in range(100)]   # _를 이용한 이유는 변수로서 활용하지 않으려고 할 때는 _를 사용한다.
# 
lst = [[0]*3 for _ in range(4)]     # 2차원 사각형 만들때 쓰이는데(예: 0짜리 3개 있는거 4개 만들기)
# 아래 이거 만들 때!!!!
# [[0,0,0]
# [0,0,0]
# [0,0,0]
# [0,0,0]]
# [[0]*3]*4 → 이렇게하면안돼요

lst = [x for x in range(1,6)]
lst =[list(range(x,x+3)) for x in range(1,6)]
print(lst)
# ↓이거만들때
# # 123
# 234
# 456
# 567
'''


# for-else :
# for문:
#     xxxx
#     xxxx
# else:       # for문이 break 없이 전체 반복완료했을 때 수행
#   문장1

lst = [2,4,6,8,10]
# 홀수 만나면 break 하기
for num in lst:     # lst 안의 num을 순서대로 꺼내올 것임
    print(num, end=' ') # end='',에서 ''사이에 띄어쓰기를 하면 나중에 그만큼 띄어서 다음내용이 출력된다.
    if num % 2 == 1:
        print('홀수다!')
        break
else:       #for문 끝나자마자 else가 와야만 for-else를 제대로 이용가능하다.
    print('홀수가 없습니다.')

#for-else가 없다면...?
#홀수가 없다라는 상태를 알 수 있는 변수가 필요함(flag 변수)
is_odd = False      #홀수가 있다없다에서 홀수가 있으면 True로 바뀌도록!

lst = [2,4,6,8,10]

for num in lst:
    print(num, end=' ')
    if num % 2 == 1:
        print('홀수다!')
        is_odd = True
        break
if not is_odd:
    print('홀수가 없습니다.')