# 이거는 같은 길이일 때 가능한 얘기다
T = int(input())
for testcase in range(1, T+1):
    arr = [input() for _ in range(5)]
    arr_t = list(zip(*arr))
    ans = ''
    for lst in arr_t:
        ans += "".join(lst)
    print(f'#{testcase} {ans}')


# 이게 방법
T = int(input())
for testcase in range(1, T+1):
    arr = [input() for _ in range(5)]
    ans = ''
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                ans += arr[i][j]
    print(f'#{testcase} {ans}')

# 이것도 방법
T = int(input())
for testcase in range(1, T+1):
    arr = [input() for _ in range(5)]
    ans = ''    
    for j in range(15):
        for i in range(5):
            try: ans +=arr[i][j]
            except: pass
    print(f'#{testcase} {ans}')