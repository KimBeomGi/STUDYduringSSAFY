# [문제]
# 1번이 줄을 선다. 1번이 한 개의 마이쮸를 받는다.
# 1번이 다시 줄을 선다.. 새로 2번이 들어와 줄을 선다.
# 1번이 두 개의 마이쮸를 받는다. 1번 다시 줄을 선다. 새로 3번이 들어와 줄을 선다.
# 2번이 한 개의 마이쮸를 받는다. 2번이 다시 줄을 선다. 새로 4번이 들어와 줄을 선다.
# 1번이 세 개의 마이쮸를 받는다. 1번이 다시 줄을 선다. 새로 5번이 들어와 줄을 선다.
# 3번이 한 개의 마이쮸를 받는다.
# ...
# 20개의 마이쮸가 있을 때 마지막 것을 누가 가져갈까?

my_chu_N = 20
front = -1
rear = -1
my_chu = [0]*my_chu_N

num = 1
give = 0
num1_give = 0
while my_chu_N > 0:                         # 마이쮸가 남아있다면
    num = 1                                 # 1번이 이제 받아야지
    num1_give += 1                          # 1번이 받는건 갈 수록 늘어나니까
    give = num1_give                        # give변수를 이용하기 위해서
    for k in range(1,give+1):               # 1~give까지
        rear += 1                           # rear에 +1 해주기
        my_chu[rear] = num                  # my_chu[rear]에 누가 마이쮸 받았는지 기록
        front += 1                          # front에 +1 해줘서 마이쮸는 이미 받았음을 기록
        my_chu_N -=1
        if my_chu_N == 0:
            break
        
    while give > 0:
        num += 1                    # 다음 번호가 이제 받아야지
        give -=1
        for k in range(1,give+1):   # 1~give까지
            rear += 1               # rear에 +1 해주기
            my_chu[rear] = num      # my_chu[rear]에 누가 마이쮸 받았는지 기록
            front += 1              # front에 +1 해줘서 마이쮸는 이미 받았음을 기록
            my_chu_N -=1
            if my_chu_N == 0:
                break
print(my_chu[-1])