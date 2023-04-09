# 문제
# 음이 아닌 b진법 정수 p와 m이 주어졌을 때, p를 m으로 나눈 나머지를 b진법으로 구하는 프로그램을 작성하시오.

# p를 m으로 나눈 나머지란 임의의 정수 a에 대해서 p = a*m + k를 만족하는 가장 작은 k를 말한다.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 3개의 정수가 한 줄로 이루어져 있다. 첫 번째 숫자는 b이고, 2보다 크거나 같고, 10보다 작거나 같은 값을 가진다. 두 번째 숫자는 p이고, 세 번째 숫자는 m이다. p와 m은 0과 b-1사이의 수로만 이루어져 있고, p의 최대 길이는 1000, m의 최대 길이는 9이다.

# 마지막 줄에는 0이 하나 주어진다.

# 출력
# 각 테스트 케이스에 대해서, p를 m으로 나눈 나머지를 b진법으로 출력한다.

# import sys

# b, p, m = map(str, sys.stdin.readline().strip().split())
# b = int(b)
# dec_p = int(p,b)
# dec_m = int(m,b)
# print(dec_p)
# print(dec_m)
# dec_answr = dec_p % dec_m

# bin_answer= bin(dec_answr)
# print(bin_answer)



import sys

K = list(map(str, sys.stdin.readline().strip().split()))

while len(K) == 3:
    # B진법으로 10진법으로 바꿔서 나머지 
    K[0] = int(K[0])
    dec_p = int(K[1],K[0])
    dec_m = int(K[2],K[0])
    dec_answr = dec_p % dec_m

    # 답을 B진법으로 바꾸기
    # answer= bin(dec_answr)
    answer = ''
    if dec_answr == 0:
        answer = '0'
    else:
        while dec_answr > 0:
            remainder = str(dec_answr % K[0])
            answer = remainder + answer
            dec_answr = dec_answr // K[0]

    print(answer)    
    K = list(map(str, sys.stdin.readline().strip().split()))


# import sys

# K = list(map(str, sys.stdin.readline().strip().split()))
# K[0] = int(K[0])
# dec_p = int(K[1],K[0])
# dec_m = int(K[2],K[0])
# print(dec_p)
# print(dec_m)
# print(dec_p % dec_m)