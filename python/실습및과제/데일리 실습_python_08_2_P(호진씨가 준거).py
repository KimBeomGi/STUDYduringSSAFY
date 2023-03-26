# [문제]
# 아래의 명세를 읽고 Pyton 클래스를 활용하여 사람(Person)을 표현하시오
# 1. 사람은 이름과 나이를 가진다.
# 2. 사람을 인스턴스를 생성하는 방법은 2가지다.
#     A. 생성자
#         1. 이름과 나이를 인자로 받는다.
#     B. get_age 클래스 메서드
#         1. 이름과 태어난 연도를 받아 나이로 변환하고, 새로운 Person 객체를 반환한다.
# 3. 인스턴스의 나이를 확인하는 메서드 check_age를 만든다.
#     A. 미성년자의 기준을 미성년자 여부를 True, False로 반환한다. 미성년자는 19세를 기준으로 한다.


class Person:   # Person class 생성
    def __init__(self, name, age):  # 생성자
        self.name = name
        self.age = age

    def get_age(name, year):    # 인자에 self는 인스턴스 자기 자신을 입력하는 것인데, get_age 메서드는 인스턴스가 사용하는 것이 아니라, 새로운 객체를 만들어서 반환하니까 self를 안 넣고 나이와 연도만 받아왔습니다.
        return Person(name, (2024-year))    # 받아온 이름과 연도를 이용해 새로운 Person 객체를 만들어서 반환합니다.

    def check_age(self):    # 이 메서드는 객체(인스턴스)가 이용하니까 self를 인자로 넣어줍니다.
        return self.age < 20    # return에 조건식을 넣으면, 조건에 따라 True, False를 반환해줍니다.

person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age)
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())