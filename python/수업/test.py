# 리스트에서 [map split 방법과, append 방법]


in_str = '1 2 3 4 5 6 7 8 9 10'


arr1 = list(map(int, in_str.split()))
print(arr1)

new_arr = []
for e in in_str.split():
    new_arr.append(int(e))

print(new_arr)