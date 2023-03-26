# [문제]
# 아래 코드와 같이 국적을 출력할 수 있는 클래스 Nationality를 작성하시오.

# korea_nationality = Nationality("대한민국")
# print(korea_nationality) # 나의 국적은 대한민국

class Nationality:
    def __init__(self, nation):
        self.nation = nation

    def __str__(self):                      # __str__ 매직메서드 이용하기
        return f'나의 국적은 {self.nation}'


korea_nationality = Nationality("대한민국")
print(korea_nationality)