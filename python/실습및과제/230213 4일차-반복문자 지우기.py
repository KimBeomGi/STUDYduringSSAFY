# 문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
# 반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
# 다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
# CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
# CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
# CAA 연속 문자 AA를 지운다.
# C 1글자가 남았으므로 1을 리턴한다.
 

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
# 다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.
 
# [출력]
# #과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

import sys
sys.stdin = open('230213 4일차-반복문자 지우기.txt','r')
# [문제풀이]
# 0. 같은 문자가 바로 반복되면 지운다 이때 2개씩 확인하고 지우며, 만약 2개가 지워지면
# 0-1. 다시 확인한 그 인덱스에서 확인을 하고 반복되지 않으면 다음 인득스를 확인하도록 한다.
# 0-2. 따라서  [0]인 경우에만 i = 0으로 하고, 그 외에는 i -=1이 되도록 한 후 다시 검사하도록 한다.
# 1. 반복문자를 지우고 이전 인덱스로로 돌아가서 다시 확인해야하므로 for문이 아닌 while문을 이용한다.
# 2. 여기서는 스택을 배웠으니까 스택을 이용해보자. 그리고 for 문을 이용해보자.

T = int(input())
for testcase in range(1, T+1):
    string_list = list(map(str, input()))                               # 붙어있는 문자열로 받았고, 인덱스를 제대로 이용하기 위해서.
    stack_string_list = [0]*(len(string_list)+1)                            # 스택 생성
    top = -1                                                            # 스택을 이용하기 위한 top
    for i in range(len(string_list)):                                   # string_list의 길이만큼 반복
        if i == 0:                                                      # [0]일때는
            top += 1                                                    # top에 1을 더해주고
            stack_string_list[top] = string_list[i]                     # stack에 넣어주기
        else:                                                                       # i가 0이 아닐때는
            top += 1                                                                # 우선 top += 1을 시도
            stack_string_list[top] = string_list[i]                                 # [top]에 [i]를 넣는다.
            if stack_string_list[top] == stack_string_list[top-1] and top > 0:      
                # 그리고 stack내에서 [top] = [top-1]면 반복이므로(and 이유는 top이 1은 되어야 비교가 가능하므로)
                top -= 2                                                # 2개씩 비교하는 반복문을 없앤것으로 하기 위해 top -2 하기
    
    print(f'#{testcase} {top+1}')
    # 왜 top+1이냐면 stack_string_list[0]~[top]까지가 반복되지 않고 남은 문자가 되는데
    # top은 [top]이어서 인덱스니까 그 수를 구하려면 top+1이 되야하니까.