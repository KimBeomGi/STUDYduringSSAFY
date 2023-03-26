# 이번에는 객체지향의 방식
# 이런 역할을 하는 객체를 만들기
# 1. 랜덤한 숫자뽑기
'''
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
'''
'''
class Person():
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1


p1 = Person('길동')
p2 = Person('사임당')
p3 = Person('순신')

print(p1.name)
# print(p2.population)                # 왠만하면 인스턴스를 통해서 클래스 변수를 사용하진 않음
print(Person.population)
p1.population = 100                 # 인스턴스.클래스변수 = ~~ 해도 클래스 변수를 건들이지는 않는다.
print(Person.population)            # 어림도 없지 여전히 3이지!!!
print(p1.population)
Person.population = 100             # 할거면 이렇게 해보시지
print(Person.population)
'''


class Person():
    population = 0
    def __init__(self, name):                      # 생성자 Constructor : 인스턴스 변수 초기화(initialize) -변수 선언 및 최초로 값을 넣어두는 것을 초기화라함.
        self.name = name
        Person.population += 1

    # 매직메서드: 특수한 목적을 수행하기 위해 미리 정의되어있는 메서드
    def __str__(self):                                  # 인스턴스를 문자열로 만들때, 반환할 문자열 정의
        return f'싸피고등학교 {self.name}'

    def say_hello(self, friend_name):                            # 인스턴스 메서드
        print(f'안녕! 나는 {friend_name}(야)아! 나는 {self.name}이야 반가워')

    @classmethod
    def get_population(cls):                                         # 클래스 변수에 접근해서 동작 수행, 매개변수만 바꾼다고 뭐가 바뀌진 않는다. 
        print(f'현재 인스턴스의 수는 : {cls.population}입니다.')        # 그래서 위에 데코레이터(여기선 @classmethod)를 달아주면 파이썬이 이놈은 클래스메서드군 하고 알아먹음
        # 이제 여기서 cls는 클래스를 가리키는 변수가 된다.
    
p1 = Person('홍길동')
print(p1.name)
p1.say_hello('철수')                                 # 인스턴스 메서드는 
# Person.say_hello(p1)                                # 이렇게 해도 가능은 한데 굳이? 이렇게 쓰지는 않는다.

a = str(p1)
print(f'a: {a}')



# lst = [1,2,3,4,5]
# print(lst)          # '[1,2,3,4,5]'
Person.get_population