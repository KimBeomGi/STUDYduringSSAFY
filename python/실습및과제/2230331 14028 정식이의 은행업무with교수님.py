import sys
sys.stdin=open('2230331 14028 정식이의 은행업무.txt','r')

def solve():
    for i in range(len(b_data)):    # 이진수의 각 자리를 바꾸기
        for e in ['1','0']:
            if b_origin[i] == e:
                continue
            else:
                b_data[i] = e
        # b_data 한자리를 바꿈
        # 3진수 한자리씩 바꿔가면서.. 비교
        b_num = int(''.join(b_data),2)
        for j in range(len(t_data)):
            for e in ['0','1','2']:
                if t_origin[j] == e:
                    continue
                else:
                    t_data[j] = e
                #### 여기가.... 2진수와 3진수 모두 교환한 시점
                # 두 숫자가 같은지 비교 해봅시다.
                t_num = int(''.join(t_data),3)
                if b_num == t_num:
                    return b_num
            t_data[j] = t_origin[j]
        b_data[i] = b_origin[i]


T= int(input())
for testcase in range(1, T+1):
    # 문자열 배열 >>>> ['1','1','0']
    b_data = list(input())
    t_data = list(input())
    b_origin = b_data[:]
    t_origin = t_data[:]
    result = solve()
    print(f'#{testcase} {result}')
    