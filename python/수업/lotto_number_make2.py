# 이번에는 객체지향의 방식
# 이런 역할을 하는 객체를 만들기
# 1. 랜덤한 숫자뽑기
# 2. 정렬하기
# 3. 출력하기
# 로또 번호 생성하기
# 로또 번호 생성기
# 생성기가 가져야할 기능
# 무작위 번호 생성, 출력, 정렬
import random
class LottoNumberMaker:
    def __init__(self):         # __init__은 데이터 선언!!!~
        self.lotto_number = set()
    def make_numbers(self):
        while len(self.lotto_number) < 6:
            self.lotto_number.add(random.randint(1,45))
    def print_numbers(self):
        print(self.lotto_number)
    def sort_numbers(self):
        self.lotto_number = list(self.lotto_number)
        self.lotto_number.sort()

maker = LottoNumberMaker()
# 랜덤한 숫자 생성
maker.make_numbers()
# 정렬
maker.sort_numbers()
# 출력
maker.print_numbers()