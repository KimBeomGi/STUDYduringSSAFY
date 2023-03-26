# [문제]
# 아래의 명세를 읽고 Python 클래스를 활용하여 PublicTransport을 표현하시오.

# A. PublicTransport는 이름 name과 요금 fare을 인스턴스 속성으로 가진다.
# B. 탑승 get_in, 하차 get_off하는 메서드를 필요로 한다,
#   1. 이 때, passenger의 수를 받는다.
# C. 현재 탑승자 수를 알 수 있어야 한다.
# D. 최종 수익을 계산하는 메소드 profit은 요금과 전체 탑승자 수를 곱해서 계산한다.


class PublicTransport:
    now_passenger_num = 0                           # 탑승자 수를 확인할 수 있게 하는 클래스 변수
    all_passenger_num = 0                           # 모든 탑승자수를 확인할 수 있는 클래스 변수
    all_profit = 0                                  # 최종 수익
    def __init__(self, name, fare):                 # PublicTransport클래스의 인스턴스 생성시 name, fare가 필요.
        self.name = name
        self.fare = fare

    def get_in(self):                               # 클래스 변수를 이용하므로 PublicTransport.를 앞에 붙여주고 이용.
        PublicTransport.now_passenger_num += 1      # 현재 탑승 승객 수에 +1
        PublicTransport.all_passenger_num += 1      # 총 탑승 승객 수에 +1
        PublicTransport.all_profit += self.fare     # 총 수익에 승객이 내는 비용을 기입
        print(PublicTransport.now_passenger_num)    # 현재 탑승자 수를 알 수 있어야 하므로 print(PublicTransport.now_passenger_num)이용
        
    def get_off(self):
        PublicTransport.now_passenger_num -= 1      # 현재 탑승 승객 수에 -1
        print(PublicTransport.now_passenger_num)    # 현재 탑승자 수를 알 수 있어야 하므로 print(PublicTransport.now_passenger_num)이용

    def profit():
        PublicTransport.all_profit = PublicTransport.all_passenger_num * PublicTransport.all_profit # 최종 수익을 계산하는 메소드 profit은 요금과 전체 탑승자 수를 곱해서 계산이므로.
        return PublicTransport.all_profit

a = 1000
passenger1 = PublicTransport('키미노', a)
passenger2 = PublicTransport('나마에', a)
passenger3 = PublicTransport('너의', a)
passenger4 = PublicTransport('이름은', a)

passenger1.get_in()
passenger2.get_in()
passenger3.get_in()
passenger2.get_off()
print(PublicTransport.profit())