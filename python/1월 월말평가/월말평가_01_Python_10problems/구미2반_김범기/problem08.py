# [문제]
# 아스키코드는미국ANSI에서표준화한정보교환용부호체계이다. 총128개의부호가사용되며,
# 다음페이지의표는알파벳이포함된65~122까지의아스키코드의일부를나타낸것이다.
# python 에서는아스키코드를활용할때ord(char)을 이용하여 해당문자에 대응하는10진수값을확인할수있다. 
# 반대의경우chr(int)를사용한다. 
# 또한문자열의대문자및소문자여부는.islower(), .isupper() 메서드를사용하여확인할수있다

# 문장의각알파벳을일정한양의 정수n만큼 밀어서다른알파벳으로바꾸는암호화방식을시저암호라고한다. 
# 입력받은문자열word를양의정수n만큼밀어완성된시저암호를반환하는함수caesar를제공된아스키코드표를참고하여완성하시오. 
# 자세한조건은아래와같다.

# 소문자는소문자로대문자는대문자로암호화한다.
# •암호화된결과는반드시알파벳구성이어야한다.
# •알파벳범위(z 또는Z) 를벗어나면다시처음으로(a 또는A)돌아가서남은범위만큼계산한다. 예)z를3번밀게된다면c가된다.

# [문제풀이]
# 1. 아스키코드를 이용한암호화 문제이다.
# 2. 소문자는 그대로 소문자가 되도록, 대문자는 대문자가 되도록 변경 없게 해야하며,
# 3. ord()로 숫자로 변경후 작업한 뒤 알파벳으로 바꿔주는 chr()을 이용
# 4. +n 만큼 밀었을 때 Z에 부딪혀 더 넘어간다면 다시 A로 돌아가도록 작성
# 5. 우선 문자열을 하나씩 분리한 뒤 리스트에 넣고, 각각 ord()이후 n처리 다시 chr(), 합치기를 이용.


# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    replace_list = []
    for char in word:
        replace_char = (ord(char)+n)        #문자를 아스키 코드 숫자로 바꾸고 n을 더함
        if 65 <= ord(char) <= 90:           #알파벳 대문자일시 할 일
            if 90 < replace_char:           # 대문자의 숫자를 n을 더했을때 넘어갈때
                replace_char = replace_char-26
                replace_list.append(chr(replace_char))
            else:
                replace_list.append(chr(replace_char))
        elif 97 <= ord(char) <= 122:        # 알파벳 소문자일시 할 일
            if 122 < replace_char:          # 소문자의 숫자를 n을 더했을때 넘어갈때
                replace_char = replace_char-26
                replace_list.append(chr(replace_char))
            else:
                replace_list.append(chr(replace_char))
    return ''.join(replace_list)




# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx

