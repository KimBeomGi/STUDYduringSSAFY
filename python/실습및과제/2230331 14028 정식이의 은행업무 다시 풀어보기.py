import sys
sys.stdin = open('2230331 14028 정식이의 은행업무.txt', 'r')

def solve():
    for i in range(len(b_data)):
        for e in ['1','0']:
            if b_origin[i] == e:
                continue
            else:
                b_data[i] = e
        b_num = int(''.join(b_data),2)  # 2진수를 10진수로 바꿔줌
        
        for j in range(len(t_data)):
            for e in ['0','1','2']:
                if t_origin[j] == e:
                    continue
                else:
                    t_data[j] = e
                t_num = int(''.join(t_data),3)
                if b_num == t_num:
                    return b_num
            t_data[j] = t_origin[j]             # 확인끝났으면 원상복귀
        b_data[i] = b_origin[i]                 # 확인 끝났으면 원상복귀
        


T = int(input())
for testcase in range(1, T+1):
    b_data = list(input())
    t_data = list(input())
    b_origin = b_data[:]
    t_origin = t_data[:]
    result = solve()
    print(f'#{testcase} {result}')
