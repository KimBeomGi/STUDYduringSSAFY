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

# 인스턴스가 이용하면 self를 적어야하고, 그것이 아니면 self 미작성.

class Person:
    def __init__(self, name, age):                  # 인스턴스 생성시 이름과 나이가 필요하므로 __init__(self, name, age)
        self.name = name                            # 매개변수 name을 self.name에 할당
        self.age = age                              # 매개변수 age을 self.age에 할당
    
    def get_age(name, year):                        # 해당 메서드는 내용을 받아서 Person 클래스의 객체로 반환해주는 메서드이기 때문에 self를 사용하지 않음
        return Person(name, 2023 - year + 1)        # Person 클래스의 객체로 반환
    
    def check_age(self):                            # 미성년자 여부 확인하는 check_age 메서드
        if self.age > 19:
            return True
        else:
            return False

person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())