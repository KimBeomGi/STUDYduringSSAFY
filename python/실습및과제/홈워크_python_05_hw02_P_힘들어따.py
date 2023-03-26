# 목표
# 학습주제파이썬 개발 환경에 대한 이해파이썬 예외처리 기본 방식에 대한 이해
# 학습목표모듈 동작 방식에 대해 이해한다.파이썬 자료 구조의 구조 및 동작 방식에 대해 이해한다.예외처리 방식 및 활용 방식에 대해 이해한다.
# 문제
#  1.  어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.       
#  예를 들어 d(91) = 9 + 1 + 91 = 101일 때, n을 d(n)의 제네레이터(generator)라고 한다. 함수 fn_d(n)을 정의하여 보라
#  2.  어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.      
#  반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.     
#  예를 들어 1, 3, 5, 7, 9, 20, 31 은 셀프 넘버들이다.
#  셀프넘버를 판별하는 함수 is_selfnumber(n)를 앞서 작성한 fn_d(n) 을 사용하여 작성하라.


# fn_d(91) 
# 출력 예시 
# 101

# [문제풀이]
# 1. d(n)을 각 자리수 숫자들과 n자신을 더한 숫자이므로
# 1-1 각자리수를 떨어뜨려 더해주면서, 자신 또한 더하는 함수 fn_d(n)을 만든다.
# 2. 제네레이터가 작동하는 방식의 최댓값을 알아내고 그 이전까지 반복문을 돌려낸다.
# 2-1 


# def fn_d():

def fn_d(funcNum):             # 제너레이터 함수 완성
    num_gen_list = []
    # funcNum = int(input('제네레이터를 이용하려면 숫자를 입력하세요 :'))
    num = funcNum
    num2 = num
    while num % 10 != 0:
        num_gen_list.append(num % 10)
        # print(num_gen_list)
        num = num // 10
    return (sum(num_gen_list)+num2)

'''
def is_selfnumber():
    is_s_num = int(input()) # 숫자 입력하면 셀프넘버 판별할 숫자
    is_s_num1 = is_s_num
    i =0
    while is_s_num1 % 10 != 0:      # 자릿수 구하기
        is_s_num1 = is_s_num1 // 10
        i += 1

    num = 1
    while num <= is_s_num:     # 자릿수만큼 9를 구한다음 넣은 숫자를 더해준다.
        if fn_d(num) == is_s_num:
            return('해당숫자는 selfnumber가 아닙니다.')
            break
        elif num != is_s_num:
            num += 1
        elif num == is_s_num:
            return('해당숫자는 selfnumber입니다.')
'''     
def is_selfnumbers():
    is_s_num = int(input('selfnumber인지 확인하려는 숫자를 입력하세요 :'))
    for i in range(1, is_s_num+1):   #fn_d() 함수를 이용, i로 돌리자, 내가 만들어진 수라면 나를 만드는 수보단 무조건 크므로 내가 제일 큼
        if fn_d(i) == is_s_num:      # 내가 만들어진 수라면 1부터 n-1수 중에는 있을테니 fn_d(i)로 돌리기
            return('해당숫자는 selfnumber가 아닙니다.')
            break
        elif i == is_s_num:             # 내 차례까지 왔는데 없다면 내가 바로 selfnumber
            return('해당숫자는 selfnumber입니다!!!!!!')        
            break



print(fn_d(int(input())))
print(is_selfnumbers()) # 입력한 수가 셀프넘버인지 출력!