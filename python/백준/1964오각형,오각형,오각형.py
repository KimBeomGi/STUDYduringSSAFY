# 점의 갯수
# 1단계: 5개
# 2단계: 12개 7개차이
# 3단게: 22개 10개차이
# 4단게: 35개 13개 차이
# 5단계? 51개겠지

# 갈수록 값의 차가 3씩 증가하는 계차수열임
N = int(input())

value = 5
diff = 7
for i in range(N-1):
    value += diff
    diff += 3

print(value%45678)

# 다른 방법
a = int(input())
b = (a*5)+(1-a+(3*a*(a-1))//2)
print(b%45678)