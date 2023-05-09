# 아스키코드 이용
string = input()                # 입력받음
string = string.upper()         # 대문자로 만듬, 대문자를 출력해야하니까
list_ord = [0]*91               # 65~90만 활용
for i in string:                # 문자열의 인자를 이용해서 반복
    list_ord[ord(i)] += 1       # 해당 반복문에 해당하는 인덱스값 +1 해주기
max_num = 0                     # 가장 많이 쓰인 수를 찾기 위한 max_num
max_ord_num = 0                 # 가장 많이 쓰인 수를 나타내는 각 대문자 알파벳의 아스키코드 번호
print_string = ''               # 출력할 문자를 표현하기 위한 변수

for i in range(65,91):          # 65~90만 활용하니까
    if list_ord[i] > max_num:   # max_num보다 list_ord[i]가 더 크면
        max_num = list_ord[i]   # 이게 이제 max_num
        max_ord_num = i         # i가 max_ord_num

count = 0                       # 가장 많이 사용된 알파벳이 몇갠지 확인하기 위함
for i in range(65,91):          # 65~95만 활용
    if list_ord[i] == max_num:  # list_ord[i]가 max_num과 같다면
        count += 1              # count에 +1해주기
    if count > 1:               # count가 1보다 커졌으면????
        print_string = '?'      # ?로 출력값을 바꿔주고 반복 종료
        break
if print_string:                # print_string에 값이 있으면
    print(print_string)         # 출력 그러니까 ?를 출력하기
else:                           # 없으면?
    print(chr(max_ord_num))     # 값을 출력해야지.


# 다른 사람이 한 풀이
word = input().upper()
oneword = list(set(word))

c_list = []
for i in oneword:
    c_list.append(word.count(i))
    
if c_list.count(max(c_list)) != 1 :
    print("?")
else:
    max_index = c_list.index(max(c_list))
    print(oneword[max_index])