string = input()
string = string.upper()
list_ord = [0]*91       # 65~90만 활용
for i in string:
    list_ord[ord(i)] += 1
max_num = 0
max_ord_num = 0
print_string = ''

for i in range(65,91):
    if list_ord[i] > max_num:
        max_num = list_ord[i]
        max_ord_num = i

count = 0
for i in range(65,91):
    if list_ord[i] == max_num:
        count += 1
        pass
    if count > 1: 
        print_string = '?'
        break
if print_string:
    print(print_string)
else:
    print(chr(max_ord_num))


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