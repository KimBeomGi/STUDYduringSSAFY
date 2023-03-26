# [문제]
# 맞는 비밀번호를 입력할 때까지 반복하는 코드를 작성하시오.
# 단, 비밀번호를 3회 이상 틀리면, 입력 기회가 종료된다.

# [문제 풀이]
# 1. 맞는 비밀번호를 입력할 때까지 이므로 for 또는 while문의 반복문을 이용해 작성.
# 2. 비밀번호를 3회 이상 틀리면, 입력 기회가 종료되므로 총 3번의 기회만 주변된다.

password = 'qlalfqjsgh'
for pass_opportunity in range(1,4):
    opportunity = input()
    if opportunity == password:
        print('잠금이 해제되었습니다.')
    elif pass_opportunity == 3 and opportunity != password:
        print('시도 횟수를 모두 이용했습니다. 해당 계정은 5분간 잠금상태가 됩니다.')
    else:
        print(f'비밀번호가 틀렸습니다.{3-pass_opportunity}회 남았습니다.')