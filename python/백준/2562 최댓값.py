max_value = 0
max_idx = 0
for i in range(1,10):
    value = int(input())
    if max_value < value:
        max_value = value
        max_idx = i

print(max_value)
print(max_idx)