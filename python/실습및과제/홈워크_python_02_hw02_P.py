# [문제]
# 1. 아이스 음료 주문이 몇 개 들어왔는지 확인하세요.
# 2. 메뉴 별 주문 수를 출력하세요

# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

#[문제풀이]
# 1. 우선 문자열을 list(map(str, orders.split())을 이용해 리스트로 만들어준다.
# 2. 리스트로 만들어준 것에서 아이스 음료 주문이 몇 개 들어왔는지 찾아주기 위해, for문을 이용해준다.
# 3. 문제 2번에서 메뉴 별 주문 수를 출력하세요. 라고 적혀있지만 이것이 리스트인지 딕셔너리인지 형식은 정해져있지 않다.
# 4. 이왕이면 딕셔너리로 키:값으로 만들어보자.

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
list_orders = list(map(str,orders.split(',')))              # ,을 기준으로 문자열을 나누고 리스트로 만들어 준다.
list_orders = sorted(list_orders, reverse=True)             # 리스트를 내림차순으로 정렬
# print(list_orders)                                        # 리스트로 잘 만들어졌는지 확인
ice_menu_order = []                                         # 아이스 음료 주문이 몇 개 들어갔는지 확인을 위한 리스트
for ice in list_orders:                                     # for 반복문으로 리스트의 인데스에서 아이스가 들어가면 ice_menu_order에 넣은뒤 len을 이용해 수를 확인 할 것임
    if ice[0:3] == '아이스':
        ice_menu_order.append(ice)
print(len(ice_menu_order))                                  # 문제 1 완료.


orders_menu_count={}                                        # 주문한 메뉴 별 주문 수 확인을 위한 딕셔너리
for drink in list_orders:                                   # 리스트 내 인덱스를 for 반복문으로 돌리기
    try: orders_menu_count[drink] += 1                      # 리스트 내 인덱스를 orders_menu_count에 기입하고 그게 있다면 값에다가 +1을 해준다.
    except: orders_menu_count[drink]=1                      # 리스트 내 인덱스를 orders_menu_count에 기입하고 그게 없다면 값으로 1을 해준다.
print(orders_menu_count)                                    # 문제 2 완료