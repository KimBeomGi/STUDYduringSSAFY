# [문제]
# 이진수는0,1로모든수를표현하는방식이다. 
# 일상생활에서사용하는십진수숫자를이진수로변경하기위해서는
# 2로나눈몫을2로나누는과정을반복하며나오는나머지들을사용한다.

# 십진수숫자n을받아이진수로변환하여문자열로반환하는함수dec_to_bin을완성하시오.
# (단, 반드시재귀를이용하여구현한다.)

#[문제풀이]
# 1. 2진수 몫이 1이거나 0이 나올때까지 돌려야하므로 반복문을 이용해준다.
# 2. 나머지와 몫을 하나의 리스트에 집어넣어주고 거꾸로 출력시켜준다.


# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.

def dec_to_bin(number):
    digit_list = []
    while number > 0:
        digit_list.append(number % 2)       # 2로 나눈 나머지를 digit_list에 입력   
        number = number // 2
    digit_list = digit_list[::-1]           # 2진법 읽는 순서가 반대로 입력되어서 반대로 출력
    digit_list2 = []
    for i in digit_list:                    # 출력되야 하는 값을 만들기 위해 ''.join()을 이용하려 for문 이용str()로 변환
        digit_list2.append(str(i))
    return ''.join(digit_list2)



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010