# tmp_input_value = list(input())
# N= len(tmp_input_value)
# input_v = []
# for i in range(N-1, -1, -1):
#     input_v.append(tmp_input_value[i])

# V = 0
# for i in range(N):
#     V += 8**i*int(input_v[i])

# binary_v = ''
# while V >0:
#     remainder = V % 2
#     binary_v += str(remainder)
#     V //=2
# binary_v = binary_v[::-1]
# print(binary_v)


# 8진수를 2진수로 변환하는 코드
octal_num = input()
# octal_num = '72'
decimal_num = int(octal_num, 8)
binary_num = bin(decimal_num)

# print(binary_num)
print(binary_num[2:])


#####################
# 참고!
# 124를 3진법으로 변환할 때는 아래처러
# x = 124
# result = ''
# while x > 0:
#     remainder = x % 3
#     result = str(remainder) + result
#     x = x // 3
# print(result)
