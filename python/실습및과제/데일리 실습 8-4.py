# [문제]
# 앞서 제작한 PublicTransport의 subclass Bus클래스를 만들어라
# A. 탈 수 있는 인원을 제한하기 위한 인스턴스 변수를 추가해라.
# B. get_in 메서드를 오버라이딩하여 탈 수 있는 인원보다 많은 인원이 탑승하려고 한다면 '더이상 탑승할 수 없습니다.'라는 문구를 출력하고 종료해라.

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


class Bus(PublicTransport):                         # PublicTransport가 부모클래스
    def get_in(self):
        if can_abroad > PublicTransport.now_passenger_num:      # 현재 탑승 승객수가 탑승 가능 인원보다 작다면
            PublicTransport.now_passenger_num += 1              # 현재 탑승 승객 수에 +1
            PublicTransport.all_passenger_num += 1              # 총 탑승 승객 수에 +1
            PublicTransport.all_profit += self.fare             # 총 수익에 승객이 내는 비용을 기입
            print(PublicTransport.now_passenger_num)            # 현재 탑승자 수를 알 수 있어야 하므로 retunr
        else:                                                   # 현재 탑승 승객수가 can_abroad 변수보다 많다면
            print('더이상 탑승할 수 없습니다.')                   # '더이상 탑승할 수 없습니다.' 출력
            return                                              # 종료


can_abroad = 10
can_abroad > PublicTransport.now_passenger_num

a = 1000
passenger1 = Bus('키미노', a)
passenger2 = Bus('나마에', a)
passenger3 = Bus('너의', a)
passenger4 = Bus('what', a)
passenger4 = Bus('is', a)
passenger4 = Bus('his', a)
passenger5 = Bus('name', a)
passenger6 = Bus('who', a)
passenger7 = Bus('are', a)
passenger8 = Bus('you', a)
passenger9 = Bus('김석전', a)
passenger10 = Bus('하동관', a)
passenger11 = Bus('유재석', a)                                  # 11명의 승객을 입력

passenger1.get_in()
passenger2.get_in()
passenger3.get_in()
passenger4.get_in()
passenger5.get_in()
passenger6.get_in()
passenger7.get_in()
passenger8.get_in()
passenger9.get_in()
passenger10.get_in()                                            # 탑승 가능 인원 10명 완료
passenger11.get_in()                                            # 탑승 가능 인원 10명을 넘음. '더이상 탑승할 수 없습니다.' 출력됨.