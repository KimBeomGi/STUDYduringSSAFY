A, B = map(int, input().split())
if A > B:
    A, B = B, A

sum_value = ((B-A+1)*((2*A)+(B-A)*1))/2
print(int(sum_value))