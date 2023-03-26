
N = input()
# M = int(N)
nums = [N]
i = 0
while True:
    if int(nums[i]) < 10:
        nums[i] = '0'+nums[i]
    plus_value = str(int(nums[i][0])+int(nums[i][1]))
    if nums[i][1] != '0':
        new_value = nums[i][1] + plus_value[-1]
    else:
        new_value = plus_value[-1]
    nums.append(new_value)
    i+=1
    if int(nums[0]) == int(nums[i]):
        break
print(i)