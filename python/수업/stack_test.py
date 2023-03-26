class MyStack:
    def __init__(self, lenth):
        self.s = [0]*lenth
        self.top = -1

    # 만들어야 할 기능
    # push, pop, peek, is_full, is_empty
    
    # 맨 뒤에 집어 넣기
    def push(self, data):
        if not self.is_full():                      # 가득 차있지 않으면
            self.top += 1
            self.s[self.top] = data
        else:                                       # 가득 차 있으면
            raise IndexError('가득차 있습니다.')

    # 마지막 요소를 삭제하며서 반환
    def pop(self):
        if not self.is_empty():
            last = self.top
            self.top -= 1
            return self.s[last]
        raise IndexError('스택이 비었습니다.')

    # 현재 마지막 요소 반환, 단 요소가 있을면 반환
    def peek(self):
        if not self.is_empty():
            return self.s[self.top]
        raise IndexError('스택이 비었습니다.')
        

    # 가득 차있으면 True, 아니면 False 반환
    def is_full(self):
        if self.top == len(self.s)-1:
            return True
        return False

    # 비어있으면 True, 아니면 False 반환
    def is_empty(self):
        if self.top == -1:
            return True
        return False


stack = MyStack(5)
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(0)       # 여기서 에러! 왜냐! 칸이 다 찼거든
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())  # 여기서 에러! 왜냐! 꺼낼게 없거든!