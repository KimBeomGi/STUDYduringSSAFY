# 문제
# 1. 레스토랑의 종업원이라고 가정하자. 손님이 스테이크를 주문하였을 때, 메뉴 가격 외에 VAT가 반영되었음을 설명해야 한다.
# 단, 이때 string interpolation과 서식명세를 사용하라
# 2. 스테이크의 가격은 50,000원/VAT는 15%이다.
# 3. 원래의 스테이크 가격과 VAT,VAT가 포함된 실제 결제 금액을 계산하여, 아래와 같이 출력하라.
# 4. 출력결과


# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

# [문제풀이]
# 1. 스테이크의 가격과 그 스테이크에 붙는 VAT가 15% 이므로 각 가격을 정하고 계산해준다.
# 2 string interpolation이므로 .format을 이용하면 된다.

steak = 50000
vat = round(steak * 0.15)
price = steak + vat

print('스테이크    {:,}\n+ VAT       {:,}\n총계 \\      {:,}'.format(steak, vat, price))