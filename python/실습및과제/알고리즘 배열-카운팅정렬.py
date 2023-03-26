# 카운팅 정렬
# 요소의 개수를 세어서 위치 찾기
# [0,4,1,3,1,2,4,1]이 있다면
# [0,1,1,1,2,3,4,4] 로 정렬가능케하는 숫자일 경우 사용가능한 정렬
# 만약 알파벳 문자라면??? 그때는 그때는 아스키코드를 이용해보는 것도 좋겠지?
# print(ord('A')), print(chr(78))와 같은 형식으로 말이지.
'''
testcase = [5, 6, 1, 3, 4, 7, 9, 8, 2]      # 테스트케이스
N = len(testcase)                           # 테스트케이스의 길이
count = [0]*(N+1)                           # 각 숫자에 해당하는 값을 받을 카운트 리스트[0]~[N]까지 받아야해서 N+1개가 필요

# testcase의 정렬
sorted_testcase = [0]*N                     # 정렬 완료된 testcase가 들어갈 리스트

for i in range(N):                          # 테스트케이스의 길이만큼 반복
    count[testcase[i]] +=1                  # 각 숫자에 해당할 값을 받을 카운트 리스트에 각 해당 값 인덱스에 +1하기

for i in range(1, len(count)):              # 누적합을 구해서 나중에 사용하기 위해 0이 아닌 1부터 시작한다.
    count[i] += count[i-1]                  # 이전값과 현재값의 합을 현재값으로 만들면서 누적합을 구한다.

print(testcase)
print(count)
print(sorted_testcase)

for i in range(N):                          # testcase의 길이만큼 반복하면서
    count[testcase[i]] -=1
    sorted_testcase[count[testcase[i]]] = testcase[i]  
    print(i, count)
    print(i, sorted_testcase)
'''
# 다시 한번 카운팅 정렬해보기

testcase = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N= len(testcase)
count = [0]*(N+1)
sorted_testcase = [0]*N

# 카운트 리스트에 갯수 집어넣기
for i in range(N):
    count[testcase[i]] += 1

# 이후 카운트리스트를 이용하기 위해 카운트 리스트내에서 누적합 구해주기
for i in range(1, len(count)):
    count[i] += count[i-1]

for i in range(N):
    count[testcase[i]] -= 1
    sorted_testcase[count[testcase[i]]] = testcase[i]

print(testcase)
print(sorted_testcase)


'''
# 아래는 오프라인 강의간 작성한 기록 내용

# 카운팅 정렬
# 요소의 개수를 세어서 위치 찾기
# 각 요소의 개수를 저장
# → 숫자가 너무 들쯕 날쭉하면 제한, 그리고 숫자로 표현해야 가능함.
# 빠아름 근데 앞서 위처럼 제약사항이 있다.
# 1. 개수 세기
# 2. 누적합 구하기(위치 구한거)
# 3. 원래 배열 돌면서 위치 찾아서 넣어주기
# 정렬대상
arr = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N = 9
# 각 요소가 몇개씩 나왔는지 개수세는 배열
count = [0]*10                  # 0번부터 9번 인덱스 까지 사용해야하므로 10개
# 정렬된 요소가 들어갈 배열
sorted_arr = [0]*9
#1. 개수세기
for i in range(N):
    count[arr[i]] += 1          # count배열에 arr[i]가 있으면 +1
#2. 누적합 구하기
# 내 앞 요소 값 + 내 값
for i in range(1, len(count)):
#     count[i] = count[i-1] + count[i]
    count[i] += count[i-1]      # 이제 카운트는 배열 요소들의 위치가 된다.
#3.원래 배열 돌면서 위치 찾아서 넣어주기
for i in range(N):
    count[arr[i]] -= 1          # count[arr[i]] 내가 들어갈 위치 찾음!! -1 해주는 이유는 인덱스에 들어가야하니까
    sorted_arr[count[arr[i]]] = arr[i]

print(sorted_arr)
'''