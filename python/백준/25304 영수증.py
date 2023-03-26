X = int(input())        # 영수증에 적힌 총 금액
N = int(input())        # 물건의 종류의 수 N
total = 0               # 총 합을 구할 변수
for i in range(N):      # N만큼 반복
    A, B = map(int, input().split())    # 물건의 가격과 수량 받음
    total += A*B        # 물건의 가격과 수량을 곱해서 더해줌.
if X == total:          # 영수증에 적힌 것과 값이 같으면 Yes 출력
    print('Yes')
else:                   # 아니면 No 출력
    print('No')