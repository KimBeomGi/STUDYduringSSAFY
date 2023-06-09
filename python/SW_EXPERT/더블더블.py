# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.

# 입력
# 8

# 출력
# 1 2 4 8 16 32 64 128 256

A = int(input())        # 횟수 입력
if A < 30:              # 첫 조건
    i=0                 # while 문 사용을 위한 인자
    while i <= A:       # while 조건문의 무한반복을 방지하기 위해걸어둔 조건
        print(2**i, '', end='')     # 2를 곱한 값을 계속하므로 제곱수를 뜻하는 **를 이용. 또 띄어쓰기를 이용하기에 '',end='' 사용
        i+=1            # while 의 무한반복 방지

else:
    print("다시 실행해서 30이하의 숫자를 넣어주세요.")