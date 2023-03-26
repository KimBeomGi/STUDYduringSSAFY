N = 5
queue = [None] * N
# 큐의 현재 맨 앞 요소와 맨 뒷요소의 인덱스를 가지고 있는 변수
# front: 맨 앞요소의 -1 인덱스,
# rear: 맨 뒷요소의 인덱스

front = rear = 0

# enQueu(data) 큐의 맨 뒤에 data 삽입
def enQueue(data):
    global rear
    if not is_full():   # 가득차지 않았으면
        rear = (rear+1) % N
        queue[rear] = data
    else:
        raise IndexError('큐가 가득찼습니다.')

# deQueue() 큐의 맨 앞에서 데이터 반환 및 삭제
def deQueue():
    global front
    if not is_empty():
        front = (front+1) % N
        return queue[front]
    else:
        raise IndexError('큐가 비었습니다.')
# is_empty() : 큐가 비었는지 확인하는 함수,
def is_empty():  # 큐가 비었으면 True를 반환 아니면, False를 반환
    # front랑 rear랑 같으면 비어있는 것.
    if front ==  rear:
        return True
    return False
    
# is_full() : 큐가 가득 찼는지 확인하는 함수
def is_full(): #
    # 원형큐에서는 rear가 움직일 다음칸이 front라면 가득 차있음.
    if (rear+1)%N == front:
        return True
    return False
    
'''
# A,B,C,D,E
enQueue('A')
enQueue('B')
enQueue('C')
enQueue('D')
enQueue('E')

print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
# deQueue 하나 더하면? 비어있는데 출력이 되는 군
# 안되게 만들어봅시다. is_empty()를 활용
# print(deQueue())    # 초기에 넣어둔 None이 출력
enQueue('E')
enQueue('E')
enQueue('E')
enQueue('E')
enQueue('E')
enQueue('E')
print(is_full())
print(is_empty())
'''

enQueue('A')
enQueue('A')
enQueue('A')
enQueue('A')
enQueue('A')
enQueue('A')
enQueue('A')
enQueue('A')