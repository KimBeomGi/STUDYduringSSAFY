# # 문제
# # 동호와 규완이는 212호에서 문자열에 대해 공부하고 있다. 규완이는 팰린드롬을 엄청나게 좋아한다. 팰린드롬이란 앞에서부터 읽으나 뒤에서부터 읽으나 같게 읽히는 문자열을 말한다.

# # 동호는 규완이를 위한 깜짝 선물을 준비했다. 동호는 규완이가 적어놓고 간 문자열 S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬을 만들려고 한다. 동호는 가능하면 가장 짧은 문자열을 만들려고 한다.

# # 동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력하는 프로그램을 작성하시오.

# # 입력
# # 첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 최대 50이다.

# # 출력
# # 첫째 줄에 동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력한다.

# # 입력값
# abab
# abacaba
# qwerty
# abdfhdyrbdbsdfghjkllkjhgfds

# # 출력값
# 5
# 7
# 11
# 38

# 문제풀이
# 1. 팰린드롬을 만들기 위한 문제로 어떤 문자열을 준다.
# 1-1. 이 문자열에 최소한의 문자들을 덧대서 팰린드롬 수를 만들면 된다.
# 1-2. 맨 뒤에서부터 가운데 까지 팰린드롬의 가능 여부를 확인한다.
# 1-3. 중간부터 확인해봤자 완벽하지 않으면 추가해야하므로 확인 만 더 하기 때문
# 1-4. 앞의 모든 문자의 갯수만큼을 추가하면 팰린드롬이 완성 가능하다.
# 2. 우리가 팰린드롬을 만들필요는 없이 문자의 갯수만 확인하면 된다.


# first_string = input()      # 입력받음
# N = len(first_string)       # 최초 문자의 길이를 입력 받음

# if N % 2 == 0:              # 길이가 짝 수일 때:
#     for i in range(N-1,N//2-1,-1):
#         for j in range(1,N-i):
            
#             pass

# else:                       # 길이가 홀 수 일 때:
#     pass


# 뒤에서 부터 확인하기 위한 is_palindrome 함수
def is_palindrome(string):
    return string == string[::-1]

# 최소 몇개의 문자를 추가해야하는지 찾는 함수
def get_min_additional_chars(string):
    N = len(string)                     # 문자길이를 N으로 입력
    for i in range(N):                  # 0~ N-1을 i로 배정
        if is_palindrome(string[i:]):   # 팰린드롬 여부를 i 인자 부터 확인하기. 어차피 끝에까지 맞는거 몇개 있는지 확인해야하니까.
            return N - len(string[i:])  # 최소를 확인할 수 있는 값이 생기면? 길이 - len(string[i]) 를 하면 그 값이 된다.
                                        # asdfgg같은 경우는 asdf만 추가하면된
    # 위에서 중간 팰린드롬이 없으면 전체 길이를 추가해줘야함. 근데 abcdef면 f가 자기자신을 팰린드롬해서 위의 if에서 걸림
    return N                            

first_string = input()
result = get_min_additional_chars(first_string)
print(len(first_string)+result)