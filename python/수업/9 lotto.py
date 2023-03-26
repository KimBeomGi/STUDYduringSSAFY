# 1이상 45이하 자연수 중에서 임의의 중복되지 않는 숫자 6개를 뽑는 것.

# 5,9,11,17,24,36
'''
import random
l_n_r = range(1,46)
thisweek_number = random.sample(l_n_r,6)
print(thisweek_number)

thisweek_number.sort(reverse=False) #로또 번호 오름차순
print("\nthisweek_number.sort(reverse=False)")
print(thisweek_number)

thisweek_number.sort(reverse=True) #로또 번호 내림차순
print("\nthisweek_number.sort(reverse=True)")
print(thisweek_number)
'''
#------------------------------------------------------------------------------------------------------------------
# 1. 로또 숫자 입력하면 컴퓨터가 로또 몇개 맞췄는지 알려주는 프로그램
#     new_arr = []
# for e in in_str.split():
#     new_arr.append(int(e))

# num_list = []

# while len(num_list)<5:
#     num = int(input())
#     if num in num_list:
#         continue
#     num_list.append(num)
    
# print(num_list)

# ----------------------------
import random

new_arr=[]  #내가 숫자 6개를 입력해보기 #내가 예상하는 이번 로또 숫자

i=0
while i<6:
    a= int(input("1부터 46까지 숫자를 입력하세요: "))   # a라는 변수를 정해주고 값을 만든다.
    if 0<a<=46:
        new_arr.append(a)
        i+=1
    elif input in new_guess:      #여기가 중복값 못 넣게 하는 것
        
    else:
        print("값을 다시 적어주세요")
new_arr.sort(reverse=False) #로또 번호 오름차순
# print("\nnew_arr.sort(reverse=False)")
print(new_arr)

# 2. 로또 추첨 번호 컴퓨터로 생성하기.
l_n_r = range(1,47)
thisweek_number = random.sample(l_n_r,6)
thisweek_number.sort(reverse=False) #로또 번호 오름차순
# print("\nnew_arr.sort(reverse=False)")
print(thisweek_number)

# 3. 내 로또번호 == 컴퓨터의 로또 번호 여부 확인
new_arr_set = set(new_arr)
thisweek_number_set = set(thisweek_number)
intersection = new_arr_set & thisweek_number_set
print(intersection)
# print(new_arr_set & thisweek_number_set) # 얘를 써도 중복되는 값 찾을 수 있음.
# print(new_arr_set.intersection(thisweek_number_set)) # 얘를 써도 중복되는 값 찾을 수 있음.