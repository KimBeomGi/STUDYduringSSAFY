import random
#로또 번호 생성 프로그램 작성
# 1이상 45 이하의 정수 중 중복하지 않는 무작위 숫자 6개 뽑기
lotto_number = set()
while len(lotto_number) < 6:
    lotto_number.add(random.randint(1,45))
print(lotto_number)
# 정렬하기
lotto_number = list(lotto_number)
lotto_number.sort()
# 생성된 숫자 출력하기
print(lotto_number)

# 위는 절차지향의 방식
