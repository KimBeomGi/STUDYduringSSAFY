#[문제]
# 김해피는 구슬치기 대회에 참가하였다. 모든 인원은 참가 번호를 부여받는데,
# 자신과 같은 참가번호를 가진 사람과 구슬치기 게임을 진행하여야 한다.
# 단, 반드시 짝이 없는 한 명의 깍두기가 존재한다. 참가자들의 참가 번호 정보가 리스트로 주어질 때, 깍두기의 참가 번호를 출력하시오.

# A. 참가자 번호는 1번부터 시작합니다.
# B. 깍두기는 한 명만 존재합니다.
# C. 깍두기를 제외한 모든 참가자는 자신의 짝(자신과 같은 수)이 존재합니다.



# participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
#

# [문제풀이]
# 1. 리스트 내 반복문을 돌려 리스트 내 같은 값이 없다면 해당 번호를 출력
# 2. 클래스 문제인 만큼 클래스로 풀어보자.

class marble:
    def __init__(self, who):
        self.who = who
    def kkak(self):
        for player in range(len(self.who)):
            if self.who[player] not in self.who[:player] and self.who[player] not in self.who[player+1:]:
                return self.who[player]

participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
participants= marble(participants)
print(participants.kkak())
