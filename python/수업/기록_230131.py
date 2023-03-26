'''
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

def en_hello(name):
    print(f'Hello, {name}!')

def add_emoji(name, func):
    func(name)
    print('^~^//')


add_emoji('dhkd', ko_hello)
add_emoji('dhkd', en_hello)
# print(ko_hello('왕'))
# print(en_hello('왕'))
'''
'''
def emoji_decoratr(func):
    def wrapper(name):          # wrapper 라는 함수를 만들었다.
        func(name)              # wrapper로 이름 변수를 받아서 emoji_decorator에서 받은 함수를 실행
        print('^~^//')

    return wrapper

def ko_hello(name):
    print(f'안녕하세요, {name}님!')

def en_hello(name):
    print(f'Hello, {name}!')

# new_func = emoji_decoratr(ko_hello)     #new_func에는 wrapper 함수가 들어가게됨 그것도 ko_hello가 실행되게끔.
# new_func('왕')                          # 이때 매개변수는 name이 들어가게 된다.
(emoji_decoratr(en_hello))('김')
'''

'''
def emoji_decoratr(func):
    def wrapper(name):          # wrapper 라는 함수를 만들었다.
        func(name)              # wrapper로 이름 변수를 받아서 emoji_decorator에서 받은 함수를 실행
        print('^~^//')

    return wrapper

@emoji_decoratr
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

@emoji_decoratr
def en_hello(name):
    print(f'Hello, {name}!')

ko_hello('왕')
'''
'''
class MyClass:

    def method(self):
        return 'instance method'
    
    @classmethod
    def classmethod(cls):
        return 'class method'

    @staticmethod
    def staticmethod():
        return 'static method'

my_class = MyClass()    # 인스턴스 만들기
print(my_class.method())
print(my_class.classmethod())
print(my_class.staticmethod())
'''
'''
class Person:
    def __init__(self):
        self._age = 0           # protected

    @property
    def age(self):          # getter
        print('getter 호출!')
        return self._age
    
    @age.setter
    def age(self, age):     # setter
        print('setter 호출!')
        self._age = age


p1 = Person()
p1.age = 25
print(p1.age)
'''
# 예외를 처리하는 방법
# 1. 애초에 예외사항을 만들지 않는 것.
# if, for, while 등 조건문이 들어가는 구문을 통해 예외사항을 막음.
# lst = [1,2,3,4]
# idx = -5
# if -len(lst) <= idx < len(lst):
#     print(lst[idx])
# else:
#     print('끝')

'''
# 2. 예외가 발생하면 무슨일을 해야할지 알려주기
# try - except 구문
lst = [1,2,0,4]
try:
    # 실행할 문장 여기
    print('0',2/lst[0])
    print('2',2/lst[2])
    print('3',2/lst[3])
    print('1',2/lst[1])
    print('4',2/lst[4])
    print('5',2/lst[5])

except ZeroDivisionError as err:
    # 예외 발생시 실행할 문장
    print(f'{err}ZeroDivisionError 발생')
except IndexError as err:
    # 예외 발생시 실행할 문장
    print(f'{err}IndexError 발생')
except Exception as err:                       # 파이썬 내장 예외의 클래스 게층 구조에서 에러들의 부모
    print(f'{err}뭔 에런지 모르겄는디...')
finally:
    print('FINALLY')
print('진짜 끝')
'''
'''
def test_func():
    try:
        print('try')
        a = 10/0
    except Exception:
        print('Exception')
        return
    finally:
        print('FINALLY')
    
    print('끝')
    return

print(test_func())
'''
'''
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'안녕하세요 저는 {self.name}입니다.')

class Student(Person):
    def work(self):
        print('열심히 공부해야지')

class Professor(Person):
     def work(self):
        print('열심히 강의해야지')



gildong = Student('홍길동')
# gildong.greeting()
# gildong.work()

kimssafy = Professor('김싸피')
# kimssafy.greeting()
# kimssafy.work()

def person_work(p1):
    # p1 : Person의 instance
    p1.greeting()
    p1.work()

#어떤 인간을 인사, 일을 시키자
person_work(gildong)
person_work(kimssafy)

class Worker:                           #worker 클래스를 완성하기 위해서는 person 클래스가 필요함
                                        # → 이런 건 worker는 person에 의존한다.
    def __init__(self,person:Person):
        self.person = person            # Person 클래스에서 인스턴스 받아오므로 이를 의존성 주입이라함. 얘는 약한 결합.
    def person_work(self):
        self.person.greeting()
        self.person.work()

# 강한 결합? 약한 결합? 뭐시당가...

worker1 = Worker(gildong)               #person 인스탄스의 제어권을 worker가 가지지 않고 worker를 사용하는 상위 모듈로 제어권을 넘김
worker2 = Worker(kimssafy)              # 이것을 제어 역전이라고 한다. (Inversion of control)
worker1.person_work()
worker2.person_work()
'''

# encaptulation(캡슐화)
# 외부에서 내부속성을 변경하거나 사용하게 되면 문제가 발생할 수 있음
# 건드려도 되는 것만 건드리게 하는거...
# (다른언어)public, protected, pirvate 등 접근 제어자를 통해서 제어할 수 있음.
# '__'등을 이용해서 만들 수 있긴한데.... 암묵적인 룰이다.
# 외부에서 내부 변수(멤버 변수)를 마음대로 변경하지 못하게 하기 위해서
# getter, setter를 사용
# @property, @setter 라는 데코레이터를 이용하면 됨
'''
class Person:
    def __init__(self, age):
        self._age = 20
    
    @property
    def age(self):
        return self._age 


    @age.setter
    def age(self,age):
        if age <= 19:
            raise ValueError('너무 어림')        # 내가 ValueError를 만들어내겠다는 것.
        else:
            self._age = age


kimssafy = Person(20)
print(kimssafy.age)
print(f'kimssafy는 {kimssafy.age}살')

kimssafy.age = 17
print(f'kimssafy는 {kimssafy.age}살')
'''

class Person:
    def __init__(self, age):
        self.__age = 20             # 내부에서만 쓸 수 있음
    
    @property                       # 내가 가진 __age의 값을 보여주는 창 역할을 하는 getter를 만들어냄
    def age(self):                  # 외부에서 __age를 볼 수 있도록 속성지정
        return self.__age 


    @age.setter
    def age(self,age):
        if age <= 19:
            raise ValueError('너무 어림')        # 내가 ValueError를 만들어내겠다는 것.
        else:
            self.__age = age


kimssafy = Person(20)
# print(kimssafy.age)
print(f'kimssafy는 {kimssafy.age}살')           # 값을 가지고 올때는 getter

kimssafy.__age = 24                           # 값을 집어넣을 때는 setter
print(f'kimssafy는 {kimssafy.age}살')