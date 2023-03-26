'''
#주어진 문자열에서 숫자, 문자, 기호가 각각 몇개인지를 판단하는 함수를 작성해보세요.

def check(target_str):
	string_dic = {}
    for char in target_str:
        if type(char) == str:
            string_dic['문자'] += 1
        elif type(char) == int:
            string_dic['숫자'] += 1
        else:
            string_dic['기호'] += 1
    return string_dic


# 문자: 10개, 숫자:2개, 기호: 7개 → 딕셔너리로 만들어야겠군

print(check('whois1st!'))
'''
'''
arr = [1, 2, 3]    # 첫번째 갔다가 2번재갔다가 3번재갔다가 4번째 갔다가 5번째 가는 함수
N = 3
# idx = 작업을 수행할 리스트의 인덱스
def recur(idx):
# 더 이상 작업이 수행되지 않는 시점 선언 필요.
    if idx == N:
        # if문에 해당하면 함수의 이 아래쪽은 수행하지마!(break걸어!)
        return    # 함수에서 return을 만나면 즉시 종료. 원래는 return None을 적어야하나 None은 생략 가능
#    arr[idx] = arr [idx]**2
    arr[idx] **= 2
    recur(idx + 1)
    return None    # 이 리턴논은 내가 할 일은 끝났으.

recur(0)
print(arr)
'''
'''
#이번엔 팩토리얼!

# factorial():
def factorial(n):
    # 기저영역 그러니까 기본값을 설정하고, 더이상 재귀가 호출 되지 않게 해야함.
    if n == 0:
        return 1        # 이 반환값이 마지막이므로 아주 중요.
    return n * factorial(n-1)

# 5factorial의 결과를 알고 싶을때 아래와 같이 수행
result = factorial(5)
print(result)
'''
'''
# sum 함수를 만들어보자.
# 인자를 두개 받을 것

N = 5
def sum_v(n, tmp_result):
    if n == 1:
        return tmp_result + 1
    return sum_v(n-1, tmp_result+n)

result = sum_v(5, 0) # 1,2,3,4,5의 합을 얻고 싶음!
print(result)
'''
'''
#이것처럼 반복문에 반복문을 써야할 경우 재귀를 써야할 때도 있다.
for i in range(N):
    for j in range(M):
        for k in range(L):
            for l in range(O):
                pass
'''
def my_max(*args):
    result = args[0]
    for e in args:
        if result < e:
            result = e
    return result
print(my_max(-1,5,4,-8,9,10))