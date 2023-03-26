

def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]


queue = [0]*10
front = -1
rear = -1


rear += 1       # enqueue(1)
queue[rear] = 1
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
print(dequeue())
if front != rear:       # front가 rear 와 일치하지 않으면, 즉. 출력할 값이 있으면
    print(dequeue())
if front != rear:
    print(dequeue())


q = []
q.append(10)
q.append(20)
q.append(39)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
