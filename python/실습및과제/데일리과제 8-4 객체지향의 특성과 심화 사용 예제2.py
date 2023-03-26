# [문제]
# 스택(Stack)은 LIFO(Last in First Out)으로 구조화된 자료구조를 의미한다. 아래 구성요소를 포함하는 Stack class를 생성하라.

# 구성요소(메서드)
# 1. __init__():인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다.
# 2. empty(): 스택이 비었다면 True을 반환하고, 그렇지 않다면 False를 반환한다.
# 3. top(): 스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환한다.
# 4. pop(): 스택의 가장 마지막 데이터의 값을 반환하고, 해당 데이터를 삭제한다. 스택이 비었다면 None을 반환한다.
# 5. push(): 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.
# 6. __repr__: 현재 스택의 요소들을 보여준다.


class Stack:
    # Stack_var = []                                        # 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다????????????
    def __init__(self):
        # self.something = something                        # 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다????????????
        # self.something = self.something.Stack_var         # 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다????????????
        self.name = []

    def empty(self):
        if len(self.name) == 0:
            return True
        else:
            return False

    def top(self):
        if len(self.name) == 0:
            return
        else :
            return self.name[-1]

    def pop(self):
        if len(self.name) == 0:
            return
        else:
            a = self.name[-1]
            del self.name[-1]
            return a

    def push(self, what):
        return self.name.append(what)

    def __repr__(self):
        return ''.join(self.name)

testObject = Stack()
print(testObject.empty())
testObject.push('A')
testObject.push('B')
testObject.push('C')
print(testObject)
print(testObject.empty())
print(testObject.pop())
print(testObject)
